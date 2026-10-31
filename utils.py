import psycopg2

def get_db_connection():
    # Apne database ke credentials yahan daalein
    conn = psycopg2.connect(
        host="localhost",
        database="fraud_db",
        user="postgres",
        password="your_password"
    )
    return conn

def save_prediction(transaction_data, is_fraud):
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        INSERT INTO predictions (amount, time, v1, v2, is_fraud)
        VALUES (%s, %s, %s, %s, %s)
    """
    cur.execute(query, (*transaction_data, is_fraud))
    conn.commit()
    cur.close()
    conn.close()