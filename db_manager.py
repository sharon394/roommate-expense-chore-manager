import sqlite3

class DatabaseManager:
    def __init__(self, db_path="data/app_database.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        
        # Table 1: Users
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                points INTEGER DEFAULT 0
            )
        ''')

        # Table 2: Expenses
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                payer_id INTEGER,
                amount REAL NOT NULL,
                description TEXT NOT NULL,
                FOREIGN KEY(payer_id) REFERENCES users(id)
            )
        ''')

        # Table 3: Chores
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                assigned_to TEXT NOT NULL,
                weight INTEGER DEFAULT 1,
                completed INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_user(self, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (name, points) VALUES (?, 0)", (name,))
        self.conn.commit()
        return cursor.lastrowid

    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()

    def add_expense(self, payer_id, amount, description):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO expenses (payer_id, amount, description) VALUES (?, ?, ?)",
                       (payer_id, amount, description))
        self.conn.commit()

    def add_chore(self, title, assigned_to, weight):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO chores (title, assigned_to, weight, completed) VALUES (?, ?, ?, 0)",
                       (title, assigned_to, weight))
        self.conn.commit()

    def get_chores(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM chores")
        return cursor.fetchall()

    def mark_chore_done(self, chore_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE chores SET completed = 1 WHERE id = ?", (chore_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
