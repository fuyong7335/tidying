import streamlit as st
from PIL import Image

# 📌 フォントスタイルを明朝体に設定（Noto Serif JP）
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Serif JP', serif;
    }
    </style>
""", unsafe_allow_html=True)

# 🖼️ ロゴ表示（ファイル名が logo.jpg の場合）
logo = Image.open("logo.jpg")
st.image(logo, width=150)

# 📝 タイトルを明朝体＋サイズ調整で表示
st.markdown("<h2>🧹 おかたづけタイプ診断</h2>", unsafe_allow_html=True)
st.write("5問に答えるだけで、あなたの片付けタイプが分かります！")

# 🔧 診断質問（タイプ分類は内部処理で記録）
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

# 🔢 タイプのスコアを記録（🌀思考 / 💭感情 / 💥燃え尽き / 🧺周囲）
scores = {'🌀': 0, '💭': 0, '💥': 0, '🧺': 0}

# 🚀 診断フォーム
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

# ✅ 診断結果を表示（簡易タイプのみ）
if submitted:
    max_type = max(scores, key=scores.get)
    st.markdown("---")
    st.subheader("診断結果")
    st.markdown(f"<p style='font-size:20px;'>あなたは <strong>{max_type}</strong> タイプかもしれません。</p>", unsafe_allow_html=True)
    st.write("▼あなたにぴったりのアドバイスは、こちらから受け取れます👇")

    # 📩 メルマガ登録URL（診断詳細はこちらから）
    MAGAZINE_LINK = "https://www.reservestock.jp/subscribe/221907"
    st.markdown(f"[📩 おかたづけアドバイスを受け取る]({MAGAZINE_LINK})", unsafe_allow_html=True)
