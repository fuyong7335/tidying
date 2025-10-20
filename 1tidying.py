import streamlit as st
from PIL import Image

# ロゴ表示（画像ファイル名は適宜調整してね）
logo = Image.open("logo.jpg")
st.image(logo, width=150)

# Googleフォント適用（明朝風フォント）
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Serif JP', serif;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧹 おかたづけタイプ診断")
st.write("10問に答えるだけで、あなたのタイプが分かります！")

# 各タイプのスコア
scores = {'🌀': 0, '💭': 0, '💥': 0, '🧺': 0}

# 診断質問（タイプは内部でスコアに反映される）
questions = [
    ("片づけを始める前にまず思うことは？", 
     ["方法が分からず手が止まる", "思い出の品が気になって進まない", "とりあえず全部出して一気にやる！", "誰かが散らかしてるのに…って感じる"]),
    ("家の中が散らかっていると感じるとき、どんな状況が多い？", 
     ["何から手をつければいいか分からない", "手放せないモノが溜まっている", "何度も一気に片づけるけどリバウンド", "自分のスペース以外が散らかってる"]),
    ("捨てる or 残すの判断基準は？", 
     ["判断に時間がかかりすぎて進まない", "感情的に「捨てられない」", "ノリで全部捨ててあとで後悔する", "家族や他人のモノは勝手に触れない"]),
    ("雑誌やSNSで片づけ情報を見ると…", 
     ["情報が多すぎて混乱する", "憧れるけど凹む", "すぐマネしたくなって突っ走る", "「うちじゃ無理」って思って諦める"]),
    ("片づけに対する理想の姿は？", 
     ["必要なモノがパッと出せる暮らし", "思い出を大切にしつつ整った部屋", "効率的でムダのないシンプル空間", "家族みんなが使いやすく整ってる状態"]),
    ("片づけをしていて「挫折」する瞬間は？", 
     ["全体が見えず、手が止まる", "捨てられない気持ちがあふれる", "中途半端になるとやる気ゼロ", "「また誰かが散らかす」と感じたとき"]),
    ("使っていないけど高かったモノがあるときは？", 
     ["価値が分からず判断に迷う", "罪悪感で手放せない", "勢いで手放してスッキリしたい", "家族の目を気にして放置"]),
    ("家族のモノが散らかっているときの反応は？", 
     ["自分のやる気がそがれる", "遠慮して触れない", "一気に怒ってしまう", "あきらめモード"]),
    ("自分のスペースが散らかってきたときは？", 
     ["片づけなきゃと思うけど動けない", "モノが語りかけてくるようで手が止まる", "限界までためてから一気にやる", "他も片づけないと意味ない"]),
    ("片づけがうまくいったときの気持ちは？", 
     ["やり方が合ってた！とホッとする", "心まで軽くなったように感じる", "達成感あるけど燃え尽きる", "家族の反応が嬉しい"])
]

# スコアに対応するマーク
mark_map = ['🌀', '💭', '💥', '🧺']

with st.form("diagnosis_form"):
    for idx, (question, options) in enumerate(questions):
        answer = st.radio(f"Q{idx+1}. {question}", options, key=f"q{idx}")
        selected_index = options.index(answer)
        scores[mark_map[selected_index]] += 1

    submitted = st.form_submit_button("診断する")

if submitted:
    max_type = max(scores, key=scores.get)

    st.markdown("---")
    st.subheader("診断結果")
    st.write(f"あなたは **{max_type}タイプ** ではないかもしれません。")
    st.write("▼あなたにぴったりのアドバイスは、こちらから受け取れます👇")
    st.markdown("[📩 おかたづけアドバイスを受けとる](https://www.reservestock.jp/subscribe/221907)")
