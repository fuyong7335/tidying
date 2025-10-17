import streamlit as st

# 質問と選択肢（マークなしバージョン）
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

# メルマガ登録ページURL（安全な入口）
MAGAZINE_LINK = "https://www.reservestock.jp/subscribe/221907"

# UIスタート
from PIL import Image
logo = Image.open("logo.jpg")
st.image(logo, width=150)

st.header("🧹 おかたづけタイプ診断")
st.write("5問に答えるだけで、あなたの“おかたづけタイプ”が分かります！")

# フォーム表示
with st.form("diagnosis_form"):
    for idx, (q, options) in enumerate(questions):
        st.radio(q, options, key=f"q{idx}")
    submitted = st.form_submit_button("診断する")

# 回答後の誘導
if submitted:
    target_url = "https://www.reservestock.jp/subscribe/221907"
    js = f"""
    <script>
        window.location.href = "{target_url}";
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)

   