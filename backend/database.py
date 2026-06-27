import sqlite3
import json
from contextlib import contextmanager

DB_PATH = "sbi_coach.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        
        # User Memory (balances, goals, preferences)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_memory (
                id INTEGER PRIMARY KEY,
                balance REAL,
                monthly_income REAL,
                avg_monthly_expense REAL,
                goals TEXT, 
                upcoming_bills TEXT
            )
        ''')
        
        # Audit Log
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                event_type TEXT,
                details TEXT,
                status TEXT
            )
        ''')
        
        # Ensure a default user exists
        cursor.execute("SELECT id FROM user_memory WHERE id = 1")
        if not cursor.fetchone():
            default_goals = json.dumps([
                {"name": "Emergency Fund", "target": 100000, "current": 25000},
                {"name": "Laptop", "target": 60000, "current": 10000}
            ])
            default_bills = json.dumps([
                {"name": "Electricity Bill", "amount": 2500, "due_in_days": 2},
                {"name": "Credit Card", "amount": 12000, "due_in_days": 8}
            ])
            cursor.execute('''
                INSERT INTO user_memory (id, balance, monthly_income, avg_monthly_expense, goals, upcoming_bills)
                VALUES (1, 15000, 62000, 38000, ?, ?)
            ''', (default_goals, default_bills))
        
        conn.commit()

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def log_event(event_type: str, details: str, status: str = "COMPLETED"):
    with get_db() as conn:
        conn.execute(
            "INSERT INTO audit_log (event_type, details, status) VALUES (?, ?, ?)",
            (event_type, details, status)
        )
        conn.commit()

def get_user_memory():
    with get_db() as conn:
        cursor = conn.execute("SELECT * FROM user_memory WHERE id = 1")
        row = cursor.fetchone()
        return dict(row) if row else None
