from src.db.connect import get_connection

def init_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Drop table if it exists (safe)
    drop_table_sql = """
    BEGIN
       EXECUTE IMMEDIATE 'DROP TABLE todo_items PURGE';
    EXCEPTION
       WHEN OTHERS THEN
          IF SQLCODE != -942 THEN
             RAISE;
          END IF;
    END;
    """
    
    # Create table
    create_table_sql = """
    CREATE TABLE todo_items (
        id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        title VARCHAR2(100) NOT NULL,
        description VARCHAR2(400),
        status VARCHAR2(20) DEFAULT 'Pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        due_date TIMESTAMP
    )
    """
    
    # Execute statements
    cursor.execute(drop_table_sql)
    cursor.execute(create_table_sql)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_database()
