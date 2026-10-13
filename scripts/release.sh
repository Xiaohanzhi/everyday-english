#!/usr/bin/env bash
# =============================================================================
# release.sh —— 每次功能提交后一键创建 GitHub Release
#
# 用法:
#   ./scripts/release.sh --dry-run              # 预览：检测未发布提交 + 建议版本（不执行）
#   ./scripts/release.sh                         # 自动：按建议版本打 tag 并创建 Release
#   ./scripts/release.sh --version v1.2.0        # 手动指定版本号
#   ./scripts/release.sh --notes-file notes.md   # 从文件补充 Release notes（可选，默认用 git log）
#
# 原理: 对比最近一个 tag 到 HEAD 的提交 → 按语义化版本建议递增
#       （feat/新增 → MINOR+1；chore/修复/文档 → PATCH+1）→ git tag + push tag
#       → 用 GitHub API 创建 Release（中文 notes 取自 commit message）
# 依赖: git + curl + 已配置的 ~/.git-credentials（github.com 的 PAT，需有 repo 权限）
# =============================================================================
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

DRY_RUN=0
VERSION=""
NOTES_FILE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    --version) VERSION="$2"; shift 2 ;;
    --notes-file) NOTES_FILE="$2"; shift 2 ;;
    *) echo "未知参数: $1（支持 --dry-run / --version / --notes-file）"; exit 1 ;;
  esac
done

# ---------- 1. 检测未发布提交 ----------
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")
if [[ -z "$LAST_TAG" ]]; then
  BASE="$(git rev-list --max-parents=0 HEAD)"
  COMMITS=$(git log --oneline "$BASE"..HEAD)
else
  COMMITS=$(git log --oneline "$LAST_TAG"..HEAD)
fi

if [[ -z "$COMMITS" ]]; then
  echo "✅ 自 $LAST_TAG 以来没有新的提交，无需发布。"
  exit 0
fi

echo "=== 自上次发布(${LAST_TAG:-无})以来的提交 ==="
echo "$COMMITS"
echo ""

# ---------- 2. 建议版本号（语义化版本） ----------
if [[ -z "$VERSION" ]]; then
  if [[ -z "$LAST_TAG" ]]; then
    VERSION="v1.0.0"
  else
    MAJOR=$(echo "$LAST_TAG" | sed 's/v\([0-9]*\)\..*/\1/')
    MINOR=$(echo "$LAST_TAG" | sed 's/v[0-9]*\.\([0-9]*\)\..*/\1/')
    PATCH=$(echo "$LAST_TAG" | sed 's/v[0-9]*\.[0-9]*\.\([0-9]*\).*/\1/')
    if echo "$COMMITS" | grep -qiE 'feat|新增|add:|feature'; then
      MINOR=$((MINOR + 1)); PATCH=0
    else
      PATCH=$((PATCH + 1))
    fi
    VERSION="v$MAJOR.$MINOR.$PATCH"
  fi
  echo "建议版本号: $VERSION（可用 --version 覆盖）"
fi

# ---------- 3. Release notes（默认从 commit message 生成中文摘要） ----------
if [[ -n "$NOTES_FILE" ]]; then
  NOTES=$(cat "$NOTES_FILE")
else
  NOTES="# Release $VERSION"
  NOTES+=$'\n\n## 变更\n'
  while IFS= read -r line; do
    NOTES+="- $line"$'\n'
  done <<< "$COMMITS"
fi

echo ""
echo "=== 即将执行 ==="
echo "  tag:    $VERSION"
echo "  target: HEAD ($(git rev-parse --short HEAD))"
echo "  notes:"
echo "$NOTES" | sed 's/^/    /'
echo ""

if [[ "$DRY_RUN" == "1" ]]; then
  echo "（--dry-run 预览结束，未执行任何操作）"
  exit 0
fi

# ---------- 4. 打 tag 并推送 ----------
git tag "$VERSION"
git push origin "$VERSION"

# ---------- 5. 用 GitHub API 创建 Release ----------
TOKEN=$(python3 -c "
import re, os
cred = open(os.path.expanduser('~/.git-credentials')).read()
for line in cred.strip().splitlines():
    m = re.match(r'https?://([^:]+):([^@]+)@github\.com/?', line)
    if m: print(m.group(2)); break
")
if [[ -z "$TOKEN" ]]; then
  echo "❌ 未在 ~/.git-credentials 找到 github.com 凭据"; exit 1
fi

REPO_URL=$(git remote get-url origin)
REPO=$(echo "$REPO_URL" | sed -E 's#https?://[^/]*/##; s#\.git$##')
BODY_JSON=$(python3 -c "
import json, sys
print(json.dumps({'tag_name': sys.argv[1], 'name': sys.argv[1], 'body': sys.argv[2], 'draft': False}))
" "$VERSION" "$NOTES")

HTTP_CODE=$(curl -s -o /tmp/release_resp.json -w '%{http_code}' \
  -X POST "https://api.github.com/repos/$REPO/releases" \
  -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "User-Agent: eea-release-bot" \
  -d "$BODY_JSON")

if [[ "$HTTP_CODE" == "201" ]]; then
  URL=$(python3 -c "import json; print(json.load(open('/tmp/release_resp.json')).get('html_url',''))")
  echo "✅ Release $VERSION 已创建: $URL"
else
  echo "❌ 创建 Release 失败 (HTTP $HTTP_CODE):"
  head -c 500 /tmp/release_resp.json; echo ""
  echo "提示: 若为 403，请在 GitHub → Settings → Developer settings → Personal access tokens 中确认 PAT 含 repo 权限（Releases 需要）"
  exit 1
fi
rm -f /tmp/release_resp.json
