import sqlite3

DATABASE = 'users.db'

def add_sample_users():
    """Add sample users to the database"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Sample users
    sample_users = [
        ('admin', 'admin123'),
        ('user1', 'password1'),
        ('testuser', 'test123'),
    ]
    
    for username, password in sample_users:
        try:
            cursor.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)',
                (username, password)
            )
            print(f"Added user: {username}")
        except sqlite3.IntegrityError:
            print(f"User {username} already exists")
    
    conn.commit()
    conn.close()
    print("\nSample users added successfully!")
    print("You can login with:")
    print("  - Username: admin, Password: admin123")
    print("  - Username: user1, Password: password1")
    print("  - Username: testuser, Password: test123")

if __name__ == '__main__':
    add_sample_users()
