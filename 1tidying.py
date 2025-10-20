import streamlit as st
from PIL import Image

# フォントを明朝体に
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Serif JP', serif;
    }
    </style>
""", unsafe_allow_html=True)

# ロゴ画像（ファイル名を適宜変更してね）
logo = Image.open("logo.jpg")
st.image(logo, width=150)

# タイプの内部キー
TYPES = {
    'freeze': '思考フリーズタイプ',
    'emotion': '感情ためこみタイプ',
    'burnout': '一気に燃え尽きタイプ',
    'family': '散らかされタイプ'
}

# 質問（タイプ記号は表に出さず、裏でスコア加算）
questions = [
    ("Q1. 片づけが進まないとき、どう感じる？",
     {"やるべきことが多すぎて動けない": "freeze",
      "昔のものを手に取ると手が止まる": "emotion",
      "一気に片付けて、疲れてやめてしまう": "burnout",
      "誰かが散らかしていてやる気が出ない": "family"}),

    ("Q2. 片づけをしようと思ったとき、まず何をする？",
     {"片付け本やSNSを探してしまう": "freeze",
      "懐かしいものを見返してしまう": "emotion",
      "やる気の波が来たときだけ一気にやる": "burnout",
      "自分のスペース以外が気になってしまう": "family"}),

    ("Q3. 収納を考えるとき、どうなる？",
     {"情報を調べすぎて決められない": "freeze",
      "収納すると見えなくなりそうで不安": "emotion",
      "とりあえず買って一気に整えたい": "burnout",
      "家族の物が多くて思うようにできない": "family"}),

    ("Q4. モノを手放すときに感じることは？",
     {"本当に必要ないのか自信が持てない": "freeze",
      "感情が揺れてなかなか判断できない": "emotion",
      "思い切って捨てたあとに後悔しがち": "burnout",
      "人のものは勝手に触れないので進まない": "family"}),

    ("Q5. 理想の片付け状態は？",
     {"何がどこにあるかすぐ分かる状態": "freeze",
      "思い出の品も大切にしながらすっきり": "emotion",
      "掃除もラクで効率的な状態": "burnout",
      "家族も使いやすく散らからない空間": "family"}),

    ("Q6. 「片付けなきゃ」と思った時の反応は？",
     {"どこから始めればいいか迷ってやめる": "freeze",
      "写真や手紙を見て手が止まる": "emotion",
      "気分が乗ったら一気にやりたくなる": "burnout",
      "自分だけが片付けていて不満が募る": "family"}),

    ("Q7. 片付け後、どう感じることが多い？",
     {"もっとやるべきだったか不安になる": "freeze",
      "思い出を処分したことに罪悪感": "emotion",
      "達成感よりもどっと疲れる": "burnout",
      "すぐに家族がまた散らかしてしまう": "family"}),

    ("Q8. モノが多い原因は？",
     {"取捨選択が苦手で残ってしまう": "freeze",
      "思い出が多すぎて減らせない": "emotion",
      "捨てたり残したりを一気にやるから": "burnout",
      "自分の意思で管理できない物が多い": "family"}),

    ("Q9. 片付けに関してよく検索することは？",
     {"収納アイデアや片付けのコツ": "freeze",
      "捨て方・思い出の整理方法": "emotion",
      "ビフォーアフター写真や短時間掃除法": "burnout",
      "子どもや家族が散らかさない工夫": "family"}),

    ("Q10. 自分の中で片付けの最大のテーマは？",
     {"決断すること": "freeze",
      "感情と向き合うこと": "emotion",
      "やる気を持続させること": "burnout",
      "人との関係性を整えること": "family"}),
]

# 診断結果文（簡易表示）
RESULTS = {
    'freeze': "あなたは『思考フリーズタイプ』かもしれません。",
    'emotion': "あなたは『感情ためこみタイプ』かもしれません。",
    'burnout': "あなたは『一気に燃え尽きタイプ』かもしれません。",
    'family': "あなたは『散らかされタイプ』かもしれません。"
}

# メルマガ登録用URL
MAGAZINE_LINK = "https://www.reservestock.jp/subscribe/221907"

# UI開始
st.title("🧹 おかたづけタイプ診断")
st.write("10問に答えるだけで、あなたの「おかたづけ傾向」がわかります。")

# スコア初期化
scores = {'freeze': 0, 'emotion': 0, 'burnout': 0, 'family': 0}

with st.form("diagnosis_form"):
    for idx, (q, options) in enumerate(questions):
        choice = st.radio(q, list(options.keys()), key=f"q{idx}")
        selected_type = options[choice]
        scores[selected_type] += 1
    submitted = st.form_submit_button("診断する")

if submitted:
    max_type = max(scores, key=scores.get)
    st.markdown("### 診断結果")
    st.markdown(RESULTS[max_type])
    st.markdown("---")
    st.markdown("▼あなたにぴったりのアドバイスは、こちらから受け取れます👇")
    st.markdown(f"[📩 おかたづけアドバイスを受け取る]({MAGAZINE_LINK})")
