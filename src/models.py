from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    question_content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Question {self.question_id}: {self.question_content[:30]}...>"
