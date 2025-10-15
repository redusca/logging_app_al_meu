from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with users table"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password required'}), 400
    
    conn = get_db_connection()
    results = conn.execute(
        'SELECT * FROM users',
    ).fetchall()

    print(f"All users in database: {results}")

    print(f"Attempting login for user: {username}")
    print(f"Password provided: {password}")

    user = conn.execute(
        'SELECT * FROM users WHERE username = ? AND password = ?',
        (username, password)
    ).fetchone()
    conn.close()
    
    if user:
        return jsonify({'success': True, 'message': 'Yes OK'}), 200
    else:
        return jsonify({'success': False, 'message': 'No, not an account'}), 200

if __name__ == '__main__':
    init_db()
    print("Database initialized!")
    app.run(debug=True, port=5000)
