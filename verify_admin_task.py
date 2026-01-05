from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from main import admin_get_task
from models import User, Task
from fastapi import HTTPException
import sys

# Setup in-memory DB
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def test_admin_fetch_task():
    db = TestingSessionLocal()
    try:
        # Create user
        user = User(username="admin", email="admin@example.com", is_admin=True)
        db.add(user)
        db.commit()
        db.refresh(user)

        # Create task
        task = Task(title="Test Task", description="Content", user_id=user.id)
        db.add(task)
        db.commit()
        db.refresh(task)

        # Test fetch
        print(f"Fetching task with ID: {task.id}")
        fetched_task = admin_get_task(task.id, db)
        if fetched_task.title == "Test Task" and fetched_task.description == "Content":
            print("Success: Task fetched successfully")
        else:
            print("Failure: Task content mismatch")
            sys.exit(1)

        # Test 404
        try:
            admin_get_task(999, db)
            print("Failure: Should have raised 404")
            sys.exit(1)
        except HTTPException as e:
            if e.status_code == 404:
                print("Success: 404 raised for invalid ID")
            else:
                print(f"Failure: Unexpected status code {e.status_code}")
                sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        db.close()

if __name__ == "__main__":
    test_admin_fetch_task()
