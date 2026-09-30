# -*- coding: utf-8 -*-
"""生成单元数据 JSON + 音频清单 JSON"""
import json, os

BASE = "/home/user/Doubao/chats/38443904742728450/eea-app"

# ---------- 单元数据 ----------
units = [
{
  "id": 1, "section": 1, "level": 1,
  "en": "First Thing in the Morning", "zh": "清晨起床",
  "grammar": "SIMPLE PRESENT", "grammarZh": "一般现在时",
  "img": "assets/img/unit1.jpg",
  "grammarNote": {
    "en": "We use the simple present to talk about things we usually or often do. Examples: I brush my teeth every day. On Saturdays, Dan sleeps late. I usually eat cereal for breakfast. Time words: every day, in the morning, once a week, usually, often, sometimes, on Sundays.",
    "zh": "一般现在时用来描述经常做、习惯性做的事。例句：I brush my teeth every day.（我每天刷牙。）On Saturdays, Dan sleeps late.（星期六丹会睡懒觉。）常搭配的时间词：every day 每天、in the morning 早上、usually 通常、often 经常、sometimes 有时。"
  },
  "steps": [
    {"en": "Dan's alarm clock rings.", "zh": "丹的闹钟响了。"},
    {"en": "He wakes up.", "zh": "他醒来了。"},
    {"en": "He gets out of bed.", "zh": "他下床了。"},
    {"en": "He goes into the bathroom.", "zh": "他走进浴室。"},
    {"en": "He uses the toilet and flushes it.", "zh": "他使用马桶并冲水。"},
    {"en": "He washes his hands.", "zh": "他洗了手。"}
  ],
  "dialogue": [],
  "vocab": {
    "verbs": [
      {"w":"brush","ipa":"/brʌʃ/","zh":"刷（牙）；刷"},
      {"w":"dry off","ipa":"/draɪ ɔːf/","zh":"擦干"},
      {"w":"eat","ipa":"/iːt/","zh":"吃"},
      {"w":"flush","ipa":"/flʌʃ/","zh":"（马桶）冲水"},
      {"w":"get dressed","ipa":"/ɡet drest/","zh":"穿衣服"},
      {"w":"get out of","ipa":"/ɡet aʊt əv/","zh":"离开；从……出来"},
      {"w":"go into","ipa":"/ɡoʊ ˈɪntuː/","zh":"走进"},
      {"w":"leave","ipa":"/liːv/","zh":"离开"},
      {"w":"make","ipa":"/meɪk/","zh":"做（早餐）；制作"},
      {"w":"ring","ipa":"/rɪŋ/","zh":"（铃）响"},
      {"w":"shave","ipa":"/ʃeɪv/","zh":"刮胡子"},
      {"w":"take a shower","ipa":"/teɪk ə ˈʃaʊər/","zh":"洗淋浴"},
      {"w":"use","ipa":"/juːz/","zh":"使用"},
      {"w":"wake up","ipa":"/weɪk ʌp/","zh":"醒来"},
      {"w":"wash","ipa":"/wɑːʃ/","zh":"洗"}
    ],
    "nouns": [
      {"w":"alarm clock","ipa":"/əˈlɑːrm klɑːk/","zh":"闹钟"},
      {"w":"apartment","ipa":"/əˈpɑːrtmənt/","zh":"公寓"},
      {"w":"bathroom","ipa":"/ˈbæθruːm/","zh":"浴室；卫生间"},
      {"w":"bed","ipa":"/bed/","zh":"床"},
      {"w":"breakfast","ipa":"/ˈbrekfəst/","zh":"早餐"},
      {"w":"hair","ipa":"/her/","zh":"头发"},
      {"w":"hand","ipa":"/hænd/","zh":"手"},
      {"w":"razor","ipa":"/ˈreɪzər/","zh":"剃须刀"},
      {"w":"shaving cream","ipa":"/ˈʃeɪvɪŋ kriːm/","zh":"剃须膏"},
      {"w":"shower","ipa":"/ˈʃaʊər/","zh":"淋浴"},
      {"w":"toilet","ipa":"/ˈtɔɪlət/","zh":"马桶；厕所"},
      {"w":"toilet bowl","ipa":"/ˈtɔɪlət boʊl/","zh":"马桶（便池）"},
      {"w":"tooth (teeth)","ipa":"/tuːθ/ (/tiːθ/)","zh":"牙齿"},
      {"w":"towel","ipa":"/ˈtaʊəl/","zh":"毛巾"}
    ],
    "others": []
  },
  "notes": [
    {"en":"wake up = stop sleeping","zh":"wake up 意思是“停止睡眠、醒来”。"},
    {"en":"wake up + get out of bed = get up. e.g. \u201cWhat time did you get up?\u201d \u201cAt 7:00.\u201d","zh":"wake up（醒来）+ get out of bed（下床）合起来就是 get up（起床）。如问句 What time did you get up?（你几点起床的？）"},
    {"en":"take a shower = wash yourself in a shower. You can also take a bath.","zh":"take a shower 是在淋浴下冲洗身体，也可以说 take a bath（泡澡）。"},
    {"en":"Polite ways to say use the toilet: \u201cgo to the bathroom\u201d, \u201cuse the bathroom\u201d.","zh":"想礼貌地表达“上厕所”，可以说 go to the bathroom 或 use the bathroom。"},
    {"en":"When you flush a toilet, water cleans the toilet bowl.","zh":"冲水（flush）时，水流会把马桶便池冲洗干净。"}
  ],
  "china": [
    {"en":"In China, many people wake up with a phone alarm instead of an alarm clock.","zh":"在中国，很多人用手机闹铃叫自己起床，而不是传统闹钟。可以说 set a phone alarm（定手机闹铃）。"},
    {"en":"\u201cWake up\u201d (wake up) vs \u201cget up\u201d (get out of bed) is a very common pair in daily talk.","zh":"wake up（醒来）和 get up（起床离床）是日常对话里非常常用的一对词，注意区分。"}
  ]
},
{
  "id": 13, "section": 2, "level": 2,
  "en": "Starting Out", "zh": "开车起步",
  "grammar": "SIMPLE PAST", "grammarZh": "一般过去时",
  "img": "assets/img/unit13.jpg",
  "grammarNote": {
    "en": "We use the simple past to tell what happened at a specific time in the past. Regular verbs add -ed (start \u2192 started); irregular verbs change (sit \u2192 sat, put \u2192 put). Time words: yesterday, this morning, last week, at 7:00.",
    "zh": "一般过去时用来叙述过去某个时间发生的事。规则动词加 -ed（start → started）；不规则动词有特殊变化（sit → sat 坐，put → put 放）。常用时间词：yesterday 昨天、this morning 今天早上、last week 上周。"
  },
  "steps": [
    {"en": "Kate sat in the driver's seat, and her friends sat in the passenger seats.", "zh": "凯特坐在驾驶座上，朋友们坐在乘客座位上。"},
    {"en": "She adjusted her seat and the rear-view mirror.", "zh": "她调整了座椅和后视镜。"},
    {"en": "She buckled her seat belt.", "zh": "她系好了安全带。"},
    {"en": "Kate put the key into the ignition.", "zh": "凯特把钥匙插入点火开关。"},
    {"en": "She turned the key.", "zh": "她转动了钥匙。"},
    {"en": "She started the car.", "zh": "她发动了汽车。"},
    {"en": "She looked over her shoulder.", "zh": "她回头看了看（肩膀后方）。"},
    {"en": "She backed out of the driveway.", "zh": "她把车倒出车道。"}
  ],
  "dialogue": [],
  "vocab": {
    "verbs": [
      {"w":"adjust","ipa":"/əˈdʒʌst/","zh":"调整"},
      {"w":"back out of","ipa":"/bæk aʊt əv/","zh":"倒车驶出"},
      {"w":"buckle","ipa":"/ˈbʌkəl/","zh":"扣上（安全带）"},
      {"w":"look","ipa":"/lʊk/","zh":"看"},
      {"w":"put into","ipa":"/pʊt ˈɪntuː/","zh":"插入；放进"},
      {"w":"sit (sat)","ipa":"/sɪt/ (/sæt/)","zh":"坐"},
      {"w":"start","ipa":"/stɑːrt/","zh":"发动；开始"},
      {"w":"start out","ipa":"/stɑːrt aʊt/","zh":"出发；起步"},
      {"w":"turn","ipa":"/tɜːrn/","zh":"转动"}
    ],
    "nouns": [
      {"w":"car","ipa":"/kɑːr/","zh":"汽车"},
      {"w":"driver","ipa":"/ˈdraɪvər/","zh":"驾驶员"},
      {"w":"driveway","ipa":"/ˈdraɪvweɪ/","zh":"（通往房屋的车道）"},
      {"w":"friend","ipa":"/frend/","zh":"朋友"},
      {"w":"ignition","ipa":"/ɪɡˈnɪʃən/","zh":"点火开关；点火"},
      {"w":"key","ipa":"/kiː/","zh":"钥匙"},
      {"w":"passenger","ipa":"/ˈpæsɪndʒər/","zh":"乘客"},
      {"w":"rear-view mirror","ipa":"/ˈrɪr vjuː ˈmɪrər/","zh":"后视镜"},
      {"w":"seat","ipa":"/siːt/","zh":"座位"},
      {"w":"seat belt","ipa":"/siːt belt/","zh":"安全带"},
      {"w":"shoulder","ipa":"/ˈʃoʊldər/","zh":"肩膀"}
    ],
    "others": []
  },
  "notes": [
    {"en":"adjust = move or change something until it is right for you.","zh":"adjust 指“调整”，把某物移动或改变到合适的状态。"},
    {"en":"A driveway is the short road that leads from the street to a house or a parking lot.","zh":"driveway 是连接街道与房屋或停车场的短车道。"},
    {"en":"The ignition is the slot where you put the car key. In other cases, \u201cignition\u201d means starting to burn.","zh":"ignition 是插入车钥匙的孔（点火开关）；在别的语境里也可以指“点燃、起火”。"}
  ],
  "china": [
    {"en":"In China, before starting out you also adjust the seat and mirrors, and you must wear a seat belt.","zh":"在中国开车前同样要先调座椅和后视镜，并且全车人员都必须系安全带。"},
    {"en":"Many cars in China are automatic (自动挡), so people just put it in D, release the brake, and go.","zh":"中国很多车是自动挡，挂 D 挡、松刹车就能起步；手动挡（manual）则需要踩离合挂挡。"},
    {"en":"Before backing up, Chinese drivers also check the rear-view mirror and the blind spot.","zh":"倒车前，中国司机同样要看后视镜和盲区（blind spot），确认安全。"}
  ]
},
{
  "id": 61, "section": 6, "level": 1,
  "en": "Eating at a Fast Food Restaurant", "zh": "在快餐店就餐",
  "grammar": "SIMPLE PAST", "grammarZh": "一般过去时",
  "img": "assets/img/unit61.jpg",
  "grammarNote": {
    "en": "This story uses the simple past: Jenny stood, read, ordered, paid, ate, threw... Irregular verbs in this unit: stand\u2192stood, read\u2192read, pay\u2192paid, eat\u2192ate, take\u2192took, throw\u2192threw, get\u2192got.",
    "zh": "这个故事用一般过去时叙述：stood、read、ordered、paid、ate、threw……本单元的不规则动词：stand→stood、read→read、pay→paid、eat→ate、take→took、throw→threw、get→got。"
  },
  "steps": [
    {"en": "Jenny stood in line and read the menu.", "zh": "珍妮排着队，看了看菜单。"},
    {"en": "She ordered her food and a drink at the counter.", "zh": "她在柜台点了食物和饮料。"},
    {"en": "The clerk put the food on her tray, and Jenny paid her.", "zh": "店员把食物放到托盘上，珍妮付了钱。"},
    {"en": "Jenny took some paper napkins and a straw from the dispensers.", "zh": "珍妮从取用架拿了纸巾和吸管。"},
    {"en": "She ate her lunch at her table.", "zh": "她在自己的桌旁吃了午餐。"},
    {"en": "Other people got their food to go.", "zh": "其他人把食物打包带走。"},
    {"en": "When she finished eating, she threw the empty wrappers in the trash.", "zh": "吃完后，她把空的包装扔进垃圾桶。"}
  ],
  "dialogue": [
    {"speaker":"Jenny","role":"girl","en":"I'd like one Big Burger, a small order of fries, and a medium cola, please.","zh":"我想要一个巨无霸汉堡、一份小薯条和一杯中杯可乐。"},
    {"speaker":"Clerk","role":"clerk","en":"For here or to go?","zh":"堂食还是打包？"},
    {"speaker":"Jenny","role":"girl","en":"For here, please.","zh":"堂食，谢谢。"},
    {"speaker":"Clerk","role":"clerk","en":"That'll be five-twenty.","zh":"一共五块二。"},
    {"speaker":"Jenny","role":"girl","en":"Right.","zh":"好的。"}
  ],
  "vocab": {
    "verbs": [
      {"w":"eat (ate)","ipa":"/iːt/ (/eɪt/)","zh":"吃"},
      {"w":"finish","ipa":"/ˈfɪnɪʃ/","zh":"完成；吃完"},
      {"w":"get (got)","ipa":"/ɡet/ (/ɡɑːt/)","zh":"得到；拿到"},
      {"w":"order","ipa":"/ˈɔːrdər/","zh":"点餐；订购"},
      {"w":"pay (paid)","ipa":"/peɪ/ (/peɪd/)","zh":"付款"},
      {"w":"put on","ipa":"/pʊt ɑːn/","zh":"放上"},
      {"w":"read (read)","ipa":"/riːd/ (/red/)","zh":"阅读"},
      {"w":"stand in line (stood)","ipa":"/stænd ɪn laɪn/","zh":"排队"},
      {"w":"take (took)","ipa":"/teɪk/ (/tʊk/)","zh":"拿；取"},
      {"w":"throw (threw)","ipa":"/θroʊ/ (/θruː/)","zh":"扔"}
    ],
    "nouns": [
      {"w":"clerk","ipa":"/klɜːrk/","zh":"店员"},
      {"w":"counter","ipa":"/ˈkaʊntər/","zh":"柜台"},
      {"w":"dispenser","ipa":"/dɪˈspensər/","zh":"（纸巾/吸管）取用架"},
      {"w":"drink","ipa":"/drɪŋk/","zh":"饮料"},
      {"w":"fast food","ipa":"/fæst fuːd/","zh":"快餐"},
      {"w":"food","ipa":"/fuːd/","zh":"食物"},
      {"w":"lunch","ipa":"/lʌntʃ/","zh":"午餐"},
      {"w":"menu","ipa":"/ˈmenjuː/","zh":"菜单"},
      {"w":"napkin","ipa":"/ˈnæpkɪn/","zh":"餐巾纸"},
      {"w":"paper","ipa":"/ˈpeɪpər/","zh":"纸"},
      {"w":"restaurant","ipa":"/ˈrestərɑːnt/","zh":"餐馆"},
      {"w":"straw","ipa":"/strɔː/","zh":"吸管"},
      {"w":"table","ipa":"/ˈteɪbəl/","zh":"餐桌"},
      {"w":"trash","ipa":"/træʃ/","zh":"垃圾桶；垃圾"},
      {"w":"tray","ipa":"/treɪ/","zh":"托盘"},
      {"w":"wrapper","ipa":"/ˈræpər/","zh":"包装纸；包装盒"}
    ],
    "others": [
      {"w":"empty","ipa":"/ˈempti/","zh":"空的"},
      {"w":"other","ipa":"/ˈʌðər/","zh":"其他的"}
    ]
  },
  "notes": [
    {"en":"In a fast-food restaurant, the menu is usually on a big board on the wall.","zh":"快餐店的菜单通常写在一块很大的墙面上。"},
    {"en":"\u201cFor here\u201d means you eat in the restaurant. \u201cTo go\u201d means you eat outside. You can also say \u201cto take away\u201d or \u201cto take out\u201d.","zh":"For here 表示在店里吃（堂食）；to go 表示带走吃，也可以说 to take away 或 to take out（打包）。"},
    {"en":"Wrappers are the paper or boxes around the food to keep it fresh.","zh":"wrapper（包装）是包在食物外面的纸或盒子，用来保鲜。"}
  ],
  "china": [
    {"en":"In China, you can also pay by scanning a QR code with WeChat Pay or Alipay.","zh":"在中国快餐店，还可以用微信支付或支付宝扫码付款：scan the QR code（扫码）。"},
    {"en":"\u201cFor here or to go?\u201d is just like \u201c堂食还是打包？\u201d in Chinese fast-food restaurants.","zh":"For here or to go? 就相当于中国快餐店的“堂食还是打包？”"},
    {"en":"Many people in China order fast food on their phones and get it delivered.","zh":"中国很多人用手机 App 点快餐外卖（order food delivery），在家就能吃。也可以说 order food on the app。"}
  ]
}
]

sections = [
  {"id":1,"en":"Starting the Day","zh":"开启一天","desc":"起床、洗漱、穿衣、早餐、出门"},
  {"id":2,"en":"Getting Around","zh":"出行","desc":"公交、开车、火车、出租、步行、骑车"},
  {"id":3,"en":"At Home in the Evening","zh":"晚间居家","desc":"回家、做饭、用餐、洗碗、休闲、就寝"},
  {"id":4,"en":"Managing a Household","zh":"家务管理","desc":"洗衣、打扫、养宠、园艺、修车、购物、银行"},
  {"id":5,"en":"Keeping in Touch","zh":"保持联络","desc":"打电话、留言、写信、寄信"},
  {"id":6,"en":"Having Fun with Friends","zh":"与友同乐","desc":"生日派对、晚宴、看电影、快餐"}
]

data = {"sections": sections, "units": units, "totalUnits": 61, "availableUnits": [u["id"] for u in units]}
with open(os.path.join(BASE, "units_data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

# ---------- 音频清单 ----------
VOICES = {
  "narrator": "一位9岁左右男孩的清脆童声，发音清晰标准的美式英语，语调自然活泼、略带童趣，逐句朗读：",
  "girl": "一位9岁左右女孩的甜美清脆童声，发音清晰的美式英语，用角色扮演的语气朗读：",
  "clerk": "一位11岁左右男孩的童声，发音清晰的美式英语，用店员角色礼貌询问的语气朗读："
}
manifest = []
for u in units:
    uid = u["id"]
    for i, s in enumerate(u["steps"], 1):
        manifest.append({"file": f"assets/audio/u{uid:03d}_s{i}.mp3", "voice": "narrator",
                         "text": s["en"], "src_text": f"unit{uid} step{i}"})
    for i, d in enumerate(u["dialogue"], 1):
        v = "girl" if d["role"] == "girl" else "clerk"
        manifest.append({"file": f"assets/audio/u{uid:03d}_d{i}.mp3", "voice": v,
                         "text": d["en"], "src_text": f"unit{uid} dialogue{i} ({d['speaker']})"})
    vi = 1
    for grp in ("verbs","nouns","others"):
        for v in u["vocab"].get(grp, []):
            manifest.append({"file": f"assets/audio/u{uid:03d}_v{vi}.mp3", "voice": "narrator",
                             "text": v["w"], "src_text": f"unit{uid} vocab {v['w']}"})
            vi += 1

with open(os.path.join(BASE, "audio_manifest.json"), "w", encoding="utf-8") as f:
    json.dump({"voices": VOICES, "outDir": os.path.join(BASE, "assets/audio"), "items": manifest},
              f, ensure_ascii=False, indent=1)

print("units:", len(units), "| audio segments:", len(manifest))
print("out:", os.path.join(BASE, "units_data.json"))
