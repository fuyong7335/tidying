import streamlit as st

# タイプ判定用キーとラベル
TYPE_LABELS = {
    'freeze': '思考が止まるタイプ',
    'emotion': '感情をためこむタイプ',
    'burnout': '燃え尽きるタイプ',
    'scattered': '周りに散らかされるタイプ'
}

# 診断結果メッセージ
RESULT_MESSAGES = {
    'freeze': "[translate:あなたは「思考が止まるタイプ」です。]\n考えすぎて動けなくなる傾向があります。まずは簡単な一歩を踏み出すことがおすすめです。",
    'emotion': "[translate:あなたは「感情をためこむタイプ」です。]\nモノに思い入れが強い方です。少しずつ手放す練習をしましょう。",
    'burnout': "[translate:あなたは「燃え尽きるタイプ」です。]\n一気にやりすぎる傾向あり。無理せずマイペースで続ける工夫を。",
    'scattered': "[translate:あなたは「周りに散らかされるタイプ」です。]\n家族や他人に左右されがち。まずは自分用のスペースから始めてみましょう。"
}

# メルマガ登録URL
ADVICE_LINK = "https://www.reservestock.jp/subscribe/221907"

# 設問データ
questions = [
    ("家が散らかる理由で一番近いのは？", [
        "やり方が分からず手が止まる（freeze）",
        "思い出にこだわって捨てられない（emotion）",
        "やる気が続かない（burnout）",
        "家族や周囲が協力してくれない（scattered）"
    ]),
    ("片付けしなきゃと思うときの気持ちは？", [
        "何から始めればいいかわからない（freeze）",
        "手放すことが心苦しい（emotion）",
        "一気にやりすぎて疲れてしまう（burnout）",
        "家族のモノが多くて進まない（scattered）"
    ]),
    ("あなたの片付けスタイルは？", [
        "情報収集ばかりで進まない（freeze）",
        "思い出にひたってしまう（emotion）",
        "勢いで一気に片づける（burnout）",
        "他人の物が気になって進まない（scattered）"
    ]),
    ("捨てるときによくある気持ちは？", [
        "必要か判断できない（freeze）",
        "罪悪感がある（emotion）",
        "とにかく全部捨ててしまう（burnout）",
        "他人のモノは勝手に捨てられない（scattered）"
    ]),
    ("理想の片付け状態は？", [
        "必要な物の場所がすぐ分かる（freeze）",
        "思い出は残しながらスッキリ（emotion）",
        "無理せずきれいを維持できる（burnout）",
        "みんなが使いやすい（scattered）"
    ]),
    ("部屋でよく気になることは？", [
        "モノの配置がごちゃごちゃ（freeze）",
        "使ってないけど捨てられない物が多い（emotion）",
        "一時的に片付いてもすぐ散らかる（burnout）",
        "自分以外の物が多すぎる（scattered）"
    ]),
    ("片付けにかける時間は？", [
        "始めるまでに時間がかかる（freeze）",
        "迷って時間ばかり過ぎる（emotion）",
        "短時間で一気に済ませたい（burnout）",
        "時間がとれても他人の物で進まない（scattered）"
    ]),
    ("片付けでストレスになることは？", [
        "正解が分からないこと（freeze）",
        "思い出と向き合うこと（emotion）",
        "片付けてもまた散らかること（burnout）",
        "家族が協力してくれないこと（scattered）"
    ]),
    ("物を捨てる基準は？", [
        "使ってるか分からないと迷う（freeze）",
        "思い入れが強い（emotion）",
        "勢いで決める（burnout）",
        "他人の物だと手が出せない（scattered）"
    ]),
    ("あなたにとって片付けとは？", [
        "整理の方法を学ぶもの（freeze）",
        "心と向き合う時間（emotion）",
        "一気に片付けたいこと（burnout）",
        "自分以外の要因も大きいこと（scattered）"
    ])
]

# ページ設定
st.set_page_config(page_title="おかたづけタイプ診断")
st.title("🧹 おかたづけタイプ診断")
st.write("10問の質問で、あなたの片付け傾向が分かります。")

# タイプごとスコア初期化
scores = {key: 0 for key in TYPE_LABELS.keys()}

with st.form("diagnosis_form"):
    for idx, (q, options) in enumerate(questions):
        choice = st.radio(q, options, key=f"q{idx}")
        for key in scores:
            if f"（{key}）" in choice:
                scores[key] += 1
                break
    submitted = st.form_submit_button("[translate:診断する]")

if submitted:
    max_type = max(scores, key=scores.get)
    st.subheader("[translate:診断結果]")
    st.markdown(f"{RESULT_MESSAGES[max_type]}")
    st.markdown("[translate:▼あなたにぴったりのアドバイスはこちらから受け取れます👇]")
    st.markdown(f"[📩 [translate:おかたづけアドバイスを受けとる] ]({ADVICE_LINK})")
