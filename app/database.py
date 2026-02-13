import os
from typing import Optional

class Database:
    """Database connection handler"""
    
    def __init__(self):
        self.host = os.getenv('DB_HOST', 'localhost')
        self.port = os.getenv('DB_PORT', '5432')
        self.database = os.getenv('DB_NAME', 'flask_app')
        self.user = os.getenv('DB_USER', 'postgres')
        self.password = os.getenv('DB_PASSWORD', '')
        self.connection = None
    
    def connect(self):
        """Establish database connection"""
        print(f"Connecting to database: {self.database} at {self.host}:{self.port}")
        # Actual connection logic would go here
        self.connection = f"Connected to {self.database}"
        return self.connection
    
    def disconnect(self):
        """Close database connection"""
        if self.connection:
            print("Disconnecting from database")
            self.connection = None
    
    def get_connection_info(self) -> dict:
        """Return connection information"""
        return {
            'host': self.host,
            'port': self.port,
            'database': self.database,
            'user': self.user,
            'connected': self.connection is not None
        }

# Singleton instance
db = Database()