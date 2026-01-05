from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, DATABASE_URL
import models

# Setup DB connection
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def list_tasks():
    db = SessionLocal()
    try:
        tasks = db.query(models.Task).all()
        if not tasks:
            print("No tasks found in the database.")
        else:
            print("Existing Tasks:")
            for task in tasks:
                print(f"ID: {task.id}, Title: {task.title}")
    finally:
        db.close()

if __name__ == "__main__":
    list_tasks()
