import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from models import Base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        # Drop existing tables
        print("🗑️  Dropping existing tables...")
        connection.execute(text("DROP TABLE IF EXISTS tasks CASCADE"))
        connection.execute(text("DROP TABLE IF EXISTS users CASCADE"))
        connection.commit()
        print("✅ Tables dropped successfully!")
        
    # Create new tables with correct structure
    print("🔨 Creating new tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ New tables created successfully!")
    
    # Verify tables
    with engine.connect() as connection:
        result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name IN ('users', 'tasks')"))
        tables = [row[0] for row in result]
        print(f"📋 Created tables: {tables}")
        
        # Check users table structure
        result = connection.execute(text("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users' ORDER BY ordinal_position"))
        columns = [(row[0], row[1]) for row in result]
        print(f"👤 Users table columns: {columns}")
        
except Exception as e:
    print(f"❌ Error: {e}")