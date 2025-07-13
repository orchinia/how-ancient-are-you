from flask import Flask, render_template, request

from models import db, load_quiz_questions_optimized

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@mysql/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DEV = True

db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    quiz_questions = load_quiz_questions_optimized()
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
