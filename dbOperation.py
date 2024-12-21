import sqlite3

class DatabaseOperations:
    def __init__(self):
        self.db_name = "teachers.db"  # Updated database name for teacher data

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                qualification TEXT,
                subjects TEXT,
                location TEXT,
                profile_url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def insert_teacher(self, teacher):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO teachers (name, qualification, subjects, location, profile_url)
                VALUES (?, ?, ?, ?, ?)
            ''', (teacher['name'], teacher['qualification'], teacher['subjects'], teacher['location'], teacher['profile_url']))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Teacher already exists: {teacher['name']}")
            return False
        finally:
            conn.close()
