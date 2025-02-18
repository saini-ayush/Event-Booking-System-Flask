import os
from ..config import get_db_connection

class MigrationManager:
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()
        self._ensure_migrations_table()

    def _ensure_migrations_table(self):
        """Create migrations table if it doesn't exist"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                id SERIAL PRIMARY KEY,
                migration_name VARCHAR(255) UNIQUE NOT NULL,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        self.conn.commit()

    def apply_migration(self, migration_name, sql_content):
        """Apply a single migration"""
        try:
            # Check if migration was already applied
            self.cursor.execute("SELECT migration_name FROM migrations WHERE migration_name = %s", (migration_name,))
            if self.cursor.fetchone():
                print(f"Migration {migration_name} already applied")
                return False

            # Apply migration
            self.cursor.execute(sql_content)
            
            # Record migration
            self.cursor.execute(
                "INSERT INTO migrations (migration_name) VALUES (%s)",
                (migration_name,)
            )
            self.conn.commit()
            print(f"Successfully applied migration: {migration_name}")
            return True
            
        except Exception as e:
            self.conn.rollback()
            print(f"Error applying migration {migration_name}: {str(e)}")
            return False

    def get_applied_migrations(self):
        """Get list of applied migrations"""
        self.cursor.execute("SELECT migration_name FROM migrations ORDER BY applied_at")
        return [row[0] for row in self.cursor.fetchall()]

    def __del__(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()