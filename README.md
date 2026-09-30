# 情景英语 Everyday English — 学习网页（61 单元完整版）

改编自《English for Everyday Activities: A Picture Process Dictionary》(L. J. Zwier, New Readers Press) 的中英双语日常英语学习站。**61 单元全量完成**：手机/电脑通用、家庭共学、随时访问、学习记录本地保存 + 导出/导入备份。

## 功能清单

- 首页目录：板块分组、单元卡片、搜索、进度统计
- 单元详情：场景插画（AI 原创）+ **竖版分镜漫画**（每格一幕、标注完整英文短句、点击可放大）+ 语法聚焦、分步流程（点句发音 + 关键词高亮）、角色对话、词汇卡（音标默认隐藏可展开）、特别注释、**中国场景对照**
- 发音：豆包语音生成的儿童音色配音（旁白/女孩/店员区分角色），整单元连读
- 学习记录：已学标记、收藏、进度条（localStorage 本地保存，页脚可导出/导入 JSON 备份）
- 练习：打字自测（看中文/听音频）、随机卡片复习、跟读打分（浏览器语音识别）
- 打印：A4 **横向**学习册/单单元学习单——每单元一页、左侧文字说明、右侧竖版分镜漫画；页内"打印本单元"与顶栏"打印学习册"共用同一版式
- 双语切换：中英对照 / 仅英文 / 仅中文

## 目录结构

```
eea-app/
├── index.html          # 单文件应用（内联 CSS/JS/数据），hash 路由
├── units_data.json     # 单元数据（内容源，已内联进 index.html）
├── audio_manifest.json # 配音清单（2532 条，音频文件名的权威依据）
├── build_data.py       # 数据/清单生成脚本
├── extra_js.js         # 页面附加脚本
├── docs/
│   └── 需求大纲-EEA学习网页.md  # 项目需求大纲
└── assets/
    ├── img/            # 61 张单元场景插画 + 61 张竖版分镜漫画（AI 原创，扁平卡通）
    └── audio/          # 2532 条配音 mp3（u001_s1.mp3=单元1步骤1，_d=对话，_v=词汇）
```

## 数据 Schema（units_data.json）

| 字段 | 说明 |
|---|---|
| id | 3 位数字字符串（"001"…"061"） |
| section | 板块编号 1–6 |
| level | 难度等级 |
| en / zh | 单元英文/中文标题 |
| grammar / grammarZh | 语法标签（中英） |
| grammarNote | 语法聚焦（en / zh） |
| steps | 分步场景短句（en / zh） |
| dialogue | 角色对话（speaker / role / en / zh） |
| vocab | 词汇（verbs / nouns / others，含音标 ipa 与中文） |
| notes | 特别注释（en / zh） |
| china | 中国场景对照（en / zh） |

## 本地使用

直接双击打开 `index.html` 即可（数据已内联，音频/图片为相对路径，无需联网）。转发给他人时**连同 assets/ 目录一起发**，否则图片和配音会失效。

## 在线访问

在线链接（豆包云电脑托管，国内可直接访问，手机/电脑通用）：

**https://si2c0v1w8ze.doubaoapps.com/app/app_17ezea00f0p**

> 在线版已将 index.html + 插画 + 配音（assets/）整体打包发布，打开即有图有声。学习记录保存在**访问设备的浏览器本地**（localStorage），页面页脚提供「导出学习记录 / 导入学习记录」可随时备份与恢复。
>
> 更新发布：修改后同步 `_deploy/` 目录（index.html + assets/），执行 `lark-cli apps +deploy --dir ./_deploy --app-id app_17ezea00f0p` 重新发布（同一链接自动更新）。

## 版权与内容说明

- **原书内容**：英文步骤句、词汇等改编自《English for Everyday Activities: A Picture Process Dictionary》（L. J. Zwier, New Readers Press），**原书版权归 New Readers Press 所有**；本仓库为其学习用途的二次创作/改编项目，非逐字复刻；
- **原创内容**：场景插画与分镜漫画全部为 AI 原创绘制；配音为豆包语音合成的儿童音色，均为本项目原创素材；
- **中国场景对照**：每单元附有贴合中国真实生活的场景对照（扫码支付、外卖、自动挡、地铁等），为原创扩展内容；
- 本仓库整体采用 **MIT 协议**开源（见 LICENSE），使用/转载时请同时保留原书版权声明与本说明。

## 后续规划

- [ ] 中国场景拓展单元（扫码支付、外卖、高铁、共享单车等）
- [ ] 按需接入云数据库实现跨设备同步
