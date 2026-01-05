from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from database import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def list_all_data():
    db = SessionLocal()
    try:
        users = db.query(models.User).all()
        print(f"Found {len(users)} users.")
        for user in users:
            print(f"User: {user.username} (ID: {user.id}, Email: {user.email})")
            tasks = db.query(models.Task).filter(models.Task.user_id == user.id).all()
            if tasks:
                for task in tasks:
                    print(f"  - Task: {task.title} (ID: {task.id}, Completed: {task.completed})")
            else:
                print("  - No tasks")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    list_all_data()
