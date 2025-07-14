import csv

from app import app
from models import db, Question, Choice, ResultMapping


def import_question_csv(file_path):
    with app.app_context():
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                question = Question(
                    question_id=int(row['question_id']),
                    question=row['question_content'],
                    question_type='single_choice'
                )
                db.session.add(question)
            db.session.commit()
        print("✅ Questions imported successfully!")


def import_choice_csv(file_path):
    with app.app_context():
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                choice = Choice(
                    choice_id=int(row['choice_id']),
                    question_id=row['question_id'],
                    choice=row['choice'],
                    choice_score=row['choice_score']
                )
                db.session.add(choice)
            db.session.commit()
        print("✅ Choices imported successfully!")


def import_result_csv(file_path):
    with app.app_context():
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                result = ResultMapping(
                    result_id=int(row['result_id']),
                    min_score=int(row['min_score']),
                    max_score=int(row['max_score']),
                    race=row['race'],
                    age=int(row['age']),
                    description=row['description'],
                )
                db.session.add(result)
            db.session.commit()
        print("✅ Results imported successfully!")


def test_load_questions():
    from app import app
    from models import load_quiz_questions_optimized

    with app.app_context():
        print(
            load_quiz_questions_optimized()
        )


def test_calculate_result():
    from app import app
    from models import calculate_result

    with app.app_context():
        print(
            calculate_result(
                {
                    'question_id': 0,
                    'question_value': 50
                }
            )
        )


if __name__ == "__main__":
    import_question_csv("data/question.csv")
    # import_choice_csv("data/choice.csv")
    # import_result_csv("data/result.csv")
    # test_load_questions()
    # test_calculate_result()
