from src.db.connect import get_connection


def execute_query(query, params=None, fetch=False, commit=False):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params or {})

    result = None
    if fetch:
        result = cursor.fetchall()

    if commit:
        conn.commit()

    cursor.close()
    conn.close()
    return result


