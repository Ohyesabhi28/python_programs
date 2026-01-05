from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from database import DATABASE_URL, Base

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def create_sample_data():
    db = SessionLocal()
    try:
        # Define sample data
        sample_users = [
            {"username": "admin", "email": "admin@example.com", "is_admin": True},
            {"username": "alice", "email": "alice@example.com", "is_admin": False},
            {"username": "bob", "email": "bob@example.com", "is_admin": False},
            {"username": "charlie", "email": "charlie@example.com", "is_admin": False},
        ]

        created_users = {}

        for user_data in sample_users:
            user = db.query(models.User).filter(models.User.email == user_data["email"]).first()
            if not user:
                print(f"Creating user {user_data['username']}...")
                user = models.User(**user_data)
                db.add(user)
                db.commit()
                db.refresh(user)
                print(f"User {user.username} created with ID: {user.id}")
            else:
                print(f"User {user.username} already exists with ID: {user.id}")
            created_users[user.username] = user

        # Define sample tasks mapping to usernames
        sample_tasks = [
            {"title": "Sample Task for Admin", "description": "This task is for testing the admin fetch endpoint.", "completed": False, "username": "admin"},
            {"title": "Buy groceries", "description": "Milk, Bread, Eggs", "completed": False, "username": "alice"},
            {"title": "Walk the dog", "description": "Take user to the park", "completed": True, "username": "alice"},
            {"title": "Finish report", "description": "Q4 financial report", "completed": False, "username": "bob"},
            {"title": "Plan vacation", "description": "Look for hotels in Tokyo", "completed": False, "username": "charlie"},
            {"title": "Book flights", "description": "Flight to Tokyo", "completed": True, "username": "charlie"},
        ]

        for task_data in sample_tasks:
            username = task_data.pop("username")
            user = created_users.get(username)
            if user:
                task = db.query(models.Task).filter(models.Task.title == task_data["title"], models.Task.user_id == user.id).first()
                if not task:
                    print(f"Creating task '{task_data['title']}' for {username}...")
                    task = models.Task(**task_data, user_id=user.id)
                    db.add(task)
                    db.commit()
                    db.refresh(task)
                    print(f"Task '{task.title}' created with ID: {task.id}")
                else:
                    print(f"Task '{task.title}' already exists for {username}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_sample_data()
