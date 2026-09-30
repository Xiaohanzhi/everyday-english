/* ===== 打字自测 ===== */
let drillState=null;
function drillItems(u){
  const items=[];
  u.steps.forEach((s,i)=>items.push({kind:"step",idx:i+1,en:s.en,zh:s.zh,src:`assets/audio/u${pad(u.id)}_s${i+1}.mp3`}));
  u.dialogue.forEach((d,i)=>items.push({kind:"dial",idx:i+1,en:d.en,zh:d.zh,src:`assets/audio/u${pad(u.id)}_d${i+1}.mp3`,speaker:d.speaker}));
  return items;
}
function norm(s){return s.toLowerCase().replace(/[^a-z0-9\s']/g,"").replace(/\s+/g," ").trim()}
function openDrill(u){
  const box=$("#drillbox");
  const items=drillItems(u);
  const item=items[Math.floor(Math.random()*items.length)];
  drillState={u:u.id,item:item,mode:"cn"};
  box.innerHTML=`
    <div class="drill">
      <div class="q">看中文，打出英文：“${esc(item.zh)}”</div>
      <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
        <button class="pbtn" style="background:var(--primary)" data-src="${item.src}" type="button">${ICON.play}</button>
        <button class="abtn" id="drill-mode" type="button">切换：听音频打字</button>
      </div>
      <input id="drill-input" placeholder="在这里输入英文句子…" autocomplete="off" spellcheck="false"/>
      <div class="controls">
        <button class="abtn primary" id="drill-check" type="button">检查</button>
        <button class="abtn" id="drill-next" type="button">换一句</button>
      </div>
      <div class="res" id="drill-res"></div>
    </div>`;
  const p=box.querySelector(".pbtn[data-src]");p&&p.addEventListener("click",()=>playSrc(p.dataset.src,p));
  const modeBtn=$("#drill-mode");
  modeBtn.addEventListener("click",()=>{
    drillState.mode=drillState.mode==="cn"?"audio":"cn";
    box.querySelector(".q").textContent=drillState.mode==="audio"?"听音频，打出英文（点喇叭可重听）":"看中文，打出英文：“"+item.zh+"”";
    modeBtn.textContent=drillState.mode==="audio"?"切换：看中文打字":"切换：听音频打字";
  });
  $("#drill-check").addEventListener("click",()=>{
    const input=$("#drill-input").value;
    const ok=norm(input)===norm(item.en);
    const res=$("#drill-res");
    res.className="res "+(ok?"ok":"no");
    res.innerHTML=ok?"✓ 完全正确！继续加油～":"差一点点：正确答案是 “"+esc(item.en)+"”";
  });
  $("#drill-next").addEventListener("click",()=>openDrill(u));
  $("#drill-input").addEventListener("keydown",e=>{if(e.key==="Enter"){$("#drill-check").click()}});
  box.querySelector("#drill-input").focus();
}

/* ===== 随机卡片复习 ===== */
let reviewQ=[],reviewI=0;
function renderReview(){
  const pool=EEA_DATA.units.flatMap(u=>u.steps.map((s,i)=>({u,en:s.en,zh:s.zh,src:`assets/audio/u${pad(u.id)}_s${i+1}.mp3`})));
  if(!pool.length){$("#view").innerHTML='<div class="empty">还没有可复习的内容</div>';return}
  reviewQ=pool.sort(()=>Math.random()-.5);reviewI=0;
  showReviewCard();
}
function showReviewCard(){
  const it=reviewQ[reviewI%reviewQ.length];
  $("#view").innerHTML=`
    <section class="review-card">
      <div class="stats" style="justify-content:center;margin:0 0 8px"><div class="stat"><b>${reviewI+1}/${reviewQ.length}</b><span>随机复习 · 全册句子</span></div></div>
      <button class="big-play" id="rplay" type="button">${ICON.play}</button>
      <div class="en">${esc(it.en)}</div>
      <div class="zh hide" id="rzh">${esc(it.zh)}</div>
      <div class="review-actions">
        <button class="abtn" id="rflip" type="button">显示中文</button>
        <button class="abtn primary" id="rnext" type="button">下一张</button>
        <a class="abtn" href="#unit/${it.u.id}">去学本单元</a>
      </div>
    </section>`;
  const play=$("#rplay");play.addEventListener("click",()=>playSrc(it.src,play));
  $("#rflip").addEventListener("click",()=>{$("#rzh").classList.toggle("hide")});
  $("#rnext").addEventListener("click",()=>{reviewI++;showReviewCard()});
}

/* ===== 跟读打分 ===== */
function initRecog(){
  const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  if(!SR)return null;
  const r=new SR();r.lang="en-US";r.interimResults=false;r.maxAlternatives=1;
  return r;
}
function openMic(u){
  const box=$("#drillbox");
  if(!initRecog()){box.innerHTML='<div class="drill"><div class="res no">当前浏览器不支持语音识别（建议使用 Chrome 或 Edge），无法进行跟读打分。</div></div>';return}
  const items=drillItems(u);
  const item=items[Math.floor(Math.random()*items.length)];
  box.innerHTML=`
    <div class="drill">
      <div class="q">跟读这句（先听一遍，再按“开始跟读”朗读）</div>
      <div class="en" style="font-size:17px;font-weight:700">${esc(item.en)}</div>
      <div style="display:flex;gap:10px;margin-top:10px;flex-wrap:wrap">
        <button class="pbtn" style="background:var(--primary)" data-src="${item.src}" type="button">${ICON.play}</button>
        <button class="abtn primary" id="mic-go" type="button">${ICON.mic} 开始跟读</button>
        <button class="abtn" id="mic-again" type="button">换一句</button>
      </div>
      <div class="res" id="mic-res"></div>
      <p class="micnote">识别结果仅供参考，评分按与原文的单词接近程度估算。</p>
    </div>`;
  const p=box.querySelector(".pbtn[data-src]");p&&p.addEventListener("click",()=>playSrc(p.dataset.src,p));
  $("#mic-again").addEventListener("click",()=>openMic(u));
  const go=$("#mic-go");
  go.addEventListener("click",()=>{
    const r=initRecog();
    let handled=false;
    go.disabled=true;go.textContent="正在听…";
    r.onresult=e=>{
      handled=true;
      const said=e.results[0][0].transcript;
      const score=scoreSpeech(said,item.en);
      const res=$("#mic-res");
      res.className="res "+(score>=70?"ok":"no");
      res.innerHTML="你说了：“"+esc(said)+"”<br/>跟读得分："+score+" 分 "+(score>=90?"（很棒！）":score>=70?"（不错，再练练更棒～）":"（多听几遍再试试）");
      go.disabled=false;go.textContent="再读一次";
    };
    r.onerror=()=>{$("#mic-res").className="res no";$("#mic-res").textContent="没有听清，请确认已允许麦克风权限后重试。";go.disabled=false;go.textContent="开始跟读"};
    r.onend=()=>{if(!handled){go.disabled=false;go.textContent="开始跟读"}};
    try{r.start()}catch(err){$("#mic-res").textContent="麦克风启动失败："+err.message;go.disabled=false;go.textContent="开始跟读"}
  });
}
function scoreSpeech(said,target){
  const a=norm(said).split(" ").filter(Boolean);
  const b=norm(target).split(" ").filter(Boolean);
  if(!a.length||!b.length)return 0;
  const bset=new Set(b);let hit=0;
  a.forEach(w=>{if(bset.has(w)){hit++;bset.delete(w)}});
  return Math.max(0,Math.min(100,Math.round(hit/b.length*100)));
}

/* ===== 打印全册 ===== */
function renderPrintAll(){
  const box=$("#printall");
  let html="";
  EEA_DATA.units.forEach(u=>{
    const sec=SEC[u.section];
    const groups=[["verbs","动词"],["nouns","名词"],["others","其他"]];
    let vhtml="";
    groups.forEach(([g,name])=>{if(u.vocab[g].length){vhtml+='<div style="margin-top:4px"><b>'+name+'：</b>'+u.vocab[g].map(v=>v.w).join("、")+'</div>'}});
    html+=`<section class="printall-unit">
      <h1>${esc(u.en)} <small>${esc(u.zh)}</small></h1>
      <p class="notes-print">${esc(sec.en)} · ${esc(sec.zh)} ｜ 语法：${esc(u.grammar)}（${esc(u.grammarZh)}）</p>
      <img src="${u.img}" alt="" style="max-height:200px;object-fit:cover;border-radius:8px"/>
      <ol class="steps-print">${u.steps.map(s=>`<li><b>${esc(s.en)}</b><br/><span class="notes-print">${esc(s.zh)}</span></li>`).join("")}</ol>
      <div class="vocab-print">${vhtml}</div>
      <div class="notes-print" style="margin-top:6px">特别注释：${u.notes.map(n=>esc(n.en)).join("；")}</div>
    </section>`;
  });
  box.innerHTML=html;
  $("#view").innerHTML=`
    <section class="review-card">
      <h1 style="font-size:22px">打印学习册</h1>
      <p style="color:var(--ink2);margin:10px 0">已生成全部单元的打印版（当前收录 ${EEA_DATA.units.length} 个单元），请在浏览器菜单中选择“打印”，或直接点击下方按钮（建议横向、边距最小）。</p>
      <div class="review-actions">
        <button class="abtn primary" id="go-print" type="button">${ICON.print} 打开打印对话框</button>
        <a class="abtn" href="#home">返回首页</a>
      </div>
    </section>`;
  $("#go-print").addEventListener("click",()=>{document.body.classList.add("print-all");window.print();setTimeout(()=>document.body.classList.remove("print-all"),500)});
}
