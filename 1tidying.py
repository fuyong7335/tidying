import streamlit as st
from PIL import Image

# 📌 フォントスタイルを明朝体に設定
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Serif JP', serif;
    }
    </style>
""", unsafe_allow_html=True)

# 🖼️ ロゴ表示（同じフォルダに logo.jpg または .png が必要）
logo = Image.open("logo.jpg")
st.image(logo, width=150)

# 📝 タイトル（明朝体＆サイズ調整）
st.markdown("<h2>🧹 おかたづけタイプ診断</h2>", unsafe_allow_html=True)
st.write("5問に答えるだけで、あなたの片付けタイプが分かります！")

# 🔢 タイプスコア（絵文字で管理）
scores = {'🌀': 0, '💭': 0, '💥': 0, '🧺': 0}

# 🏷️ 絵文字 → タイプ名の辞書
TYPES = {
    '🌀': '思考フリーズタイプ',
    '💭': '感情ためこみタイプ',
    '💥': '一気に燃え尽きタイプ',
    '🧺': '散らかされタイプ'
}

# 📝 設問と選択肢（記号は非表示に）
questions = [
    ("Q1. 家が散らかる原因として一番しっくりくるのは？",
     ["方法がよく分からない", "思い出や感情が絡んで捨てられない", "一気にやろうとして途中で燃え尽きる", "家族が原因で片付けが進まない"]),

    ("Q2. 『片付けなきゃ』と思うとき、まず感じることは？",
     ["何から始めればいいのかわからない", "モノに罪悪感や愛着があって迷う", "面倒だけどやるときはガッとやる", "自分だけが頑張ってる気がしてしんどい"]),

    ("Q3. 自分の片付けスタイルは？",
     ["情報を見てるだけで手が止まる", "思い出に浸って進まない", "とにかく一気にやって終わらせたい", "いつも誰かに邪魔される"]),

    ("Q4. 捨てる時に感じるのは？",
     ["いるかいらないかの判断ができない", "手放すと後悔しそうで怖い", "勢いで捨ててしまいがち", "他の人のモノは勝手に捨てられない"]),

    ("Q5. 理想の片付け状態は？",
     ["何がどこにあるか一目で分かる", "思い出は大事にしつつスッキリ", "手間なくきれいがキープされる", "家族も使いやすく、散らからない"]),
]

# 🚀 フォーム入力
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

# ✅ 結果表示＋メルマガ誘導
if submitted:
    max_type = max(scores, key=scores.get)

    st.markdown("---")
    st.markdown("### 診断結果")
    st.markdown(
        f"<p style='font-size:20px;'>あなたは <strong>{TYPES[max_type]}</strong> かもしれません。</p>",
        unsafe_allow_html=True
    )

    st.write("▼あなたにぴったりのアドバイスは、こちらから受け取れます👇")

    # 📩 メルマガ登録リンク
    MAGAZINE_LINK = "https://www.reservestock.jp/subscribe/221907"
    st.markdown(f"[📩 おかたづけアドバイスを受けとる]({MAGAZINE_LINK})")
