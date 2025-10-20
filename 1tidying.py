import streamlit as st

# 診断タイプとラベル
TYPES = {
    'freeze': '思考フリーズタイプ',
    'emotion': '感情ためこみタイプ',
    'burnout': '一気に燃え尽きタイプ',
    'scattered': '散らかされタイプ'
}

# 設問と選択肢（10問）
questions = [
    ("Q1. 家が散らかる理由で一番しっくりくるのは？",
     ["やり方がよく分からない（freeze）",
      "思い出がよぎって捨てられない（emotion）",
      "やる気が続かない（burnout）",
      "家族が片づけに協力してくれない（scattered）"]),

    ("Q2. 『片付けしなきゃ』と思うときに感じるのは？",
     ["何から始めればいいかわからない（freeze）",
      "手放すのが心苦しい（emotion）",
      "一気にやりすぎて疲れる（burnout）",
      "家族のモノが多くて進まない（scattered）"]),

    ("Q3. 自分の片付けスタイルを表すなら？",
     ["調べてばかりで手が止まる（freeze）",
      "思い出にひたってしまう（emotion）",
      "勢いで一気に片づける（burnout）",
      "他人のモノが気になって進まない（scattered）"]),

    ("Q4. 捨てるときに感じることは？",
     ["必要かどうか判断できない（freeze）",
      "罪悪感がある（emotion）",
      "とりあえず全部捨ててしまう（burnout）",
      "他人のモノは勝手に捨てられない（scattered）"]),

    ("Q5. 理想の片付け状態は？",
     ["必要な物の場所がすぐ分かる（freeze）",
      "思い出は大切にしながらスッキリ（emotion）",
      "ラクにキレイが保てる（burnout）",
      "家族みんなが使いやすい（scattered）"]),

    ("Q6. 部屋を見渡したとき、気になるのは？",
     ["モノの配置がごちゃごちゃ（freeze）",
      "使ってないけど捨てられない物（emotion）",
      "一時的にキレイでもすぐ散らかる（burnout）",
      "自分以外の物が多すぎる（scattered）"]),

    ("Q7. 片付けにかける時間は？",
     ["始めるまでに時間がかかる（freeze）",
      "迷って時間ばかり過ぎる（emotion）",
      "短時間で一気に済ませたい（burnout）",
      "時間がとれても他人のせいで進まない（scattered）"]),

    ("Q8. 片付けでストレスに感じるのは？",
     ["正解が分からないこと（freeze）",
      "思い出と向き合うこと（emotion）",
      "やってもすぐ散らかること（burnout）",
      "家族が協力してくれないこと（scattered）"]),

    ("Q9. モノを捨てるときの基準は？",
     ["使ってるか分からない（freeze）",
      "思い入れが強い（emotion）",
      "勢いで決めてる（burnout）",
      "他人の物だから手が出せない（scattered）"]),

    ("Q10. あなたにとって片付けとは？",
     ["整理の仕方を学ぶもの（freeze）",
      "心と向き合う時間（emotion）",
      "一気に片をつけたいこと（burnout）",
      "自分以外の影響も大きいこと（scattered）"]),
]

# 結果文
RESULTS = {
    'freeze': "あなたは「思考フリーズタイプ」かもしれません。",
    'emotion': "あなたは「感情ためこみタイプ」かもしれません。",
    'burnout': "あなたは「一気に燃え尽きタイプ」かもしれません。",
    'scattered': "あなたは「散らかされタイプ」かもしれません。"
}

# メルマガ登録リンク
MAGAZINE_LINK = "https://www.reservestock.jp/subscribe/221907"

# UI開始
st.set_page_config(page_title="おかたづけタイプ診断")
st.title("🧹 おかたづけタイプ診断")
st.write("10問に答えるだけで、あなたの片づけ傾向が分かります。")

# スコア初期化
scores = {'freeze': 0, 'emotion': 0, 'burnout': 0, 'scattered': 0}

with st.form("diagnosis_form"):
    for idx, (q, options) in enumerate(questions):
        choice = st.radio(q, options, key=f"q{idx}")
        for key in scores:
            if f"（{key}）" in choice:
                scores[key] += 1
                break
    submitted = st.form_submit_button("診断する")

if submitted:
    max_type = max(scores, key=scores.get)
    st.subheader("診断結果")
    st.markdown(f"{RESULTS[max_type]}")
    st.markdown("▼あなたにぴったりのアドバイスはこちらから受け取れます👇")
    st.markdown(f"[📩 おかたづけアドバイスを受けとる]({MAGAZINE_LINK})")
