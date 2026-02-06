import sqlite3
from datetime import datetime
import os


class DatabaseManager:
    def __init__(self, db_path='chatbot.db'):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """Create a database connection."""
        return sqlite3.connect(self.db_path)
    
    def init_database(self):
        """Initialize the database with required tables."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Create conversations table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create messages table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id INTEGER NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (conversation_id) REFERENCES conversations(id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_conversation(self):
        """Create a new conversation and return its ID."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO conversations DEFAULT VALUES')
        conversation_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return conversation_id
    
    def save_message(self, conversation_id, role, content):
        """Save a message to the database."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO messages (conversation_id, role, content) VALUES (?, ?, ?)',
            (conversation_id, role, content)
        )
        conn.commit()
        conn.close()
    
    def get_conversation_messages(self, conversation_id):
        """Get all messages for a specific conversation."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT role, content, timestamp FROM messages WHERE conversation_id = ? ORDER BY timestamp',
            (conversation_id,)
        )
        messages = cursor.fetchall()
        conn.close()
        return messages
    
    def get_all_conversations(self):
        """Get all conversations with their message counts."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT c.id, c.created_at, COUNT(m.id) as message_count
            FROM conversations c
            LEFT JOIN messages m ON c.id = m.conversation_id
            GROUP BY c.id
            ORDER BY c.created_at DESC
        ''')
        conversations = cursor.fetchall()
        conn.close()
        return conversations
