import streamlit as st
from PIL import Image

# タイプごとのスコア管理用辞書
TYPES = {
    '🌀': '思考フリーズタイプ',
    '💭': '感情ためこみタイプ',
    '💥': '一気に燃え尽きタイプ',
    '🧺': '散らかされタイプ'
}

# 質問と選択肢（各選択肢にタイプを割り当て）
questions = [
    ("Q1. 家が散らかる原因として一番しっくりくるのは？",
     ["方法がよく分からない",
      "思い出や感情が絡んで捨てられない",
      "一気にやろうとして途中で燃え尽きる",
      "家族が原因で片付けが進まない"]),

    ("Q2. 『片付けなきゃ』と思うとき、まず感じることは？",
     ["何から始めればいいのかわからない",
      "モノに罪悪感や愛着があって迷う",
      "面倒だけどやるときはガッとやる",
      "自分だけが頑張ってる気がしてしんどい"]),

    ("Q3. 自分の片付けスタイルは？",
     ["情報を見てるだけで手が止まる",
      "思い出に浸って進まない",
      "とにかく一気にやって終わらせたい",
      "いつも誰かに邪魔される"]),

    ("Q4. 捨てる時に感じるのは？",
     ["いるかいらないかの判断ができない",
      "手放すと後悔しそうで怖い",
      "勢いで捨ててしまいがち",
      "他の人のモノは勝手に捨てられない"]),

    ("Q5. 理想の片付け状態は？",
     ["何がどこにあるか一目で分かる",
      "思い出は大事にしつつスッキリ",
      "手間なくきれいがキープされる",
      "家族も使いやすく、散らからない"]),
]

# 結果文（タイプ別）※ここでは簡易表示のみ
RESULTS = {
    '🌀': "あなたは『思考フリーズタイプ』かもしれません",
    '💭': "あなたは『感情ためこみタイプ』かもしれません",
    '💥': "あなたは『一気に燃え尽きタイプ』かもしれません",
    '🧺': "あなたは『散らかされタイプ』かもしれません"
}

# メルマガ登録用URL
MAGAZINE_LINK = "https://www.reservestock.jp/subscribe/221907"

# UIスタート（ロゴ画像表示）
logo = Image.open("logo.jpg")  # logo.png でもOK
st.image(logo, width=150)

st.title("🧹 おかたづけタイプ診断")
st.write("5問に答えるだけで、あなたの片付けタイプが分かります！")

# 回答カウント用
scores = {'🌀': 0, '💭': 0, '💥': 0, '🧺': 0}

with st.form("diagnosis_form"):
    for idx, (q, options) in enumerate(questions):
        choice = st.radio(q, options, key=f"q{idx}")
        if choice == options[0]:
            scores['🌀'] += 1
        elif choice == options[1]:
            scores['💭'] += 1
        elif choice == options[2]:
            scores['💥'] += 1
        elif choice == options[3]:
            scores['🧺'] += 1

    submitted = st.form_submit_button("診断する")

# 診断後の表示
if submitted:
    if submitted:
    max_type = max(scores, key=scores.get)

    st.markdown(f"<h4>あなたは『{TYPES[max_type]}』かもしれません</h4>", unsafe_allow_html=True)
    st.write("あなたにぴったりのアドバイスは、こちらでご紹介しています👇")
    st.markdown(f"👉 [おかたづけタイプ別のアドバイスをみる](https://www.reservestock.jp/subscribe/221907)")
    st.caption("※タイプに合わせたアドバイスが見られるページにつながります")
