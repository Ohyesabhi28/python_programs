import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

try:
    # Get table names
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    print("📋 Tables in database:")
    for table in tables:
        print(f"  - {table}")
    
    print("\n🔍 Table structures:")
    
    # Check each table structure
    for table in tables:
        print(f"\n📊 {table.upper()} table:")
        columns = inspector.get_columns(table)
        for column in columns:
            print(f"  - {column['name']}: {column['type']} {'(PK)' if column.get('primary_key') else ''}")
    
    # Check data count
    print("\n📈 Data counts:")
    with engine.connect() as connection:
        for table in tables:
            try:
                result = connection.execute(text(f"SELECT COUNT(*) FROM {table}"))
                count = result.fetchone()[0]
                print(f"  - {table}: {count} records")
            except Exception as e:
                print(f"  - {table}: Error counting - {e}")
                
except Exception as e:
    print(f"❌ Error: {e}")