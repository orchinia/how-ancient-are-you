from flask import Flask, render_template, request

from models import calculate_result, db, load_quiz_questions_optimized

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
