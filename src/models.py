from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    question = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.Text, nullable=False)

    choices = db.relationship('Choice', backref='question', lazy=True)

    def __repr__(self):
        return f"<Question {self.question_id}: {self.question[:30]}...>"
    

class Choice(db.Model):
    __tablename__ = 'choices'
    
    choice_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'), nullable=False)
    choice = db.Column(db.Text, nullable=False)
    choice_score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Choice {self.choice_id}: {self.choice[:30]}...>"
    

def load_quiz_questions_optimized():
    """
    從資料庫讀取測驗題目和選項（優化版本）
    """
    try:
        # 使用 joinedload 一次性載入問題和選項
        questions = Question.query.options(
            db.joinedload(Question.choices)
        ).order_by(Question.question_id).all()
        
        quiz_list = []
        
        for question in questions:
            # 對選項按照 choice_id 排序
            sorted_choices = sorted(question.choices, key=lambda x: x.choice_id)
            
            # 構建選項列表
            options = [
                {
                    "text": choice.choice,
                    "value": choice.choice_score
                }
                for choice in sorted_choices
            ]
            
            # 構建問題字典
            question_dict = {
                "question_id": question.question_id,
                "question": question.question,
                "question_type": question.question_type,
                "options": options
            }
            
            quiz_list.append(question_dict)
        
        return quiz_list
        
    except Exception as e:
        print(f"讀取測驗題目時發生錯誤: {e}")
        return []
