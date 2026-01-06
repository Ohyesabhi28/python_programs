import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        # Drop all tables
        tables_to_drop = [
            "user_roles",
            "users", 
            "roles",
            "products",
            "profiles", 
            "authors",
            "author_bios",
            "alembic_version"
        ]
        
        for table in tables_to_drop:
            try:
                connection.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE"))
                print(f"✅ Dropped table: {table}")
            except Exception as e:
                print(f"⚠️  Could not drop {table}: {e}")
        
        connection.commit()
        print("🎉 All tables dropped successfully!")
        
except Exception as e:
    print(f"❌ Error: {e}")