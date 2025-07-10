import csv

from app import app
from models import db, Question


def import_csv(file_path):
    with app.app_context():
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                question = Question(
                    question_id=int(row['question_id']),
                    question_content=row['question_content']
                )
                db.session.add(question)
            db.session.commit()
        print("✅ Questions imported successfully!")

if __name__ == "__main__":
    import_csv("data/question_data.csv")
