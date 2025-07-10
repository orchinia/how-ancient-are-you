from flask import Flask, render_template

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@mysql/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DEV = True

db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8888, debug=DEV)
