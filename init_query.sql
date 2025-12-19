-- Drop table if exists (use try/catch block style in Oracle)
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE todo_items PURGE';
EXCEPTION
   WHEN OTHERS THEN
      IF SQLCODE != -942 THEN
         RAISE;
      END IF;
END;


-- Create the table
CREATE TABLE todo_items (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR2(100) NOT NULL,
    description VARCHAR2(400),
    status VARCHAR2(20) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    due_date TIMESTAMP
);
