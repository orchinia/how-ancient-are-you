from flask import Flask, render_template, request, jsonify


from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@mysql/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DEV = True

db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

def load_quiz_questions():

    quiz_list = [
        {
            "question_id": 1,
            "question": "你最理想的日常生活是？",
            "question_type": "single_choice",
            "options": [
                {"text": "鑽研技藝、建立根基", "value": 10},
                {"text": "在樹林間冥想與藝術創作", "value": 7},
                {"text": "種田吃點心喝下午茶", "value": 3},
                {"text": "四處旅行冒險找機會", "value": 5}
            ]
        },
        {
            "question_id": 2,
            "question": "面對突如其來的挑戰，你會？",
            "question_type": "single_choice",
            "options": [
                {"text": "靜觀其變，等待最佳時機", "value": 7},
                {"text": "衝上去再說！", "value": 4},
                {"text": "找個安全角落喝茶", "value": 2},
                {"text": "確保自己準備好所有工具", "value": 10}
            ]
        },
        {
            "question_id": 3,
            "question": "與人意見不同時你會？",
            "question_type": "single_choice",
            "options": [
                {"text": "理性討論，尋求共識", "value": 7},
                {"text": "擺出證據和邏輯擊敗對方", "value": 10},
                {"text": "覺得無所謂，隨他吧", "value": 3},
                {"text": "擺臭臉但其實沒生氣", "value": 5}
            ]
        },
        {
            "question_id": 4,
            "question": "你的社交傾向？",
            "question_type": "single_choice",
            "options": [
                {"text": "大量社交我會疲憊", "value": 7},
                {"text": "很會交朋友、講幹話很快樂", "value": 3},
                {"text": "有時有點怕生但會主動", "value": 5},
                {"text": "比起說話我更喜歡做事", "value": 10}
            ]
        },
        {
            "question_id": 5,
            "question": "有人偷吃你最愛的點心，你會？",
            "question_type": "single_choice",
            "options": [
                {"text": "默默補一份，當作沒事", "value": 7},
                {"text": "把點心藏起來", "value": 10},
                {"text": "生氣 30 秒後算了", "value": 5},
                {"text": "哭給大家看", "value": 3}
            ]
        },
        {
            "question_id": 6,
            "question": "你對未來的想像是？",
            "question_type": "single_choice",
            "options": [
                {"text": "與大自然共存，悠然生活", "value": 7},
                {"text": "建立自己的王國！", "value": 5},
                {"text": "吃得飽、睡得好最重要", "value": 3},
                {"text": "留名青史，傳承給子孫", "value": 10}
            ]
        },
        {
            "question_id": 7,
            "question": "你理想中的家？",
            "question_type": "single_choice",
            "options": [
                {"text": "地底溫暖的石室", "value": 10},
                {"text": "被樹包圍的透明高塔", "value": 7},
                {"text": "舒適小屋與花園", "value": 3},
                {"text": "各地為家，無拘無束", "value": 5}
            ]
        }
    ]

    return quiz_list

@app.route("/quiz")
def quiz():
    quiz_questions = load_quiz_questions()
    return render_template("quiz.html", quiz_questions=quiz_questions)

def calculate_result(data):
    """
        data = dict of {'question_id(str)': 'option_value(str)'}

        result values = sum of option_values(int)

    """
    scores = [int(v) for v in data.values()]
    score = sum(scores)
    if score <= 25:
        res = {'race': '哈比人 🍞', 'age': 22, 'description': '天真樂觀、享受生活、沒有煩惱'}
    elif score <= 30:
        res = {'race': '哈比人 🍞', 'age': 28, 'description': '自在與人共處，有點世故但仍愛和平'}
    elif score <= 35:
        res = {'race': '人類 ⚔️', 'age': 32, 'description': '熱血冒險、充滿幹勁'}
    elif score <= 40:
        res = {'race': '人類 ⚔️', 'age': 38, 'description': '歷經挑戰，開始重視責任與平衡'}
    elif score <= 47:
        res = {'race': '精靈 🌿', 'age': 120, 'description': '優雅理性，重視自然與深層思考'}
    elif score <= 55:
        res = {'race': '精靈 🌿', 'age': 180, 'description': '深不可測，歷練豐富，靜如止水'}
    elif score <= 65:
        res = {'race': '矮人 🪓', 'age': 200, 'description': '固執可靠、做事有原則'}
    else: # score >= 66:
        res = {'race': '矮人 🪓', 'age': 300, 'description': '長者級智慧、以沉默與行動說話'}
    return res


@app.route("/submit", methods=["POST"])
def submit():
    # data = dict of {'question_id': 'option_value'}
    data = request.form.to_dict()
    res = calculate_result(data)
    return render_template("result.html", result=res)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8888, debug=DEV)
