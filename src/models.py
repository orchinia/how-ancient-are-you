from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    question = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.Text, nullable=False)

    choices = db.relationship('Choice', backref='question', lazy=True)
    

class Choice(db.Model):
    __tablename__ = 'choices'
    
    choice_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'), nullable=False)
    choice = db.Column(db.Text, nullable=False)
    choice_score = db.Column(db.Integer, nullable=False)


class ResultMapping(db.Model):
    __tablename__ = 'result_mappings'

    result_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    min_score = db.Column(db.Integer, nullable=False)
    max_score = db.Column(db.Integer, nullable=False)
    race = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<ResultMapping {self.race} ({self.min_score}-{self.max_score})>"
    

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
    

def calculate_result(data: dict) -> dict:
    """
    Args:
        data: dict of {'question_id(str)': 'option_value(str)'}
    
    Returns:
        dict with keys: race, age, description (from result_mappings)
    """
    scores = [int(v) for v in data.values()]
    total_score = sum(scores)

    # 查詢符合區間的 result mapping
    result = ResultMapping.query.filter(
        and_(
            ResultMapping.min_score <= total_score,
            ResultMapping.max_score >= total_score
        )
    ).first()

    if not result:
        raise ValueError(f"No result mapping found for score: {total_score}")

    return {
        "race": result.race,
        "age": result.age,
        "description": result.description,
    }
