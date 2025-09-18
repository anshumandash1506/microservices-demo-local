
from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER', 'testuser'),
        password=os.environ.get('DB_PASSWORD', 'testpass'),
        database=os.environ.get('DB_NAME', 'demo'),
        port=int(os.environ.get('DB_PORT', 3306))
    )

# Ensure users table exists on startup
def ensure_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT PRIMARY KEY,
            name VARCHAR(50)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/api/users')
def users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT id, name FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)


if __name__ == '__main__':
    ensure_users_table()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
