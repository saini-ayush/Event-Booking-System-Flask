import os
from migration_manager import MigrationManager

def run_migrations():
    migration_manager = MigrationManager()
    migrations_dir = "app/db/migrations/versions"
    
    # Get all migration files
    migration_files = sorted([f for f in os.listdir(migrations_dir) if f.endswith('.sql')])
    
    # Apply each migration
    for migration_file in migration_files:
        with open(os.path.join(migrations_dir, migration_file), 'r') as f:
            sql_content = f.read()
            migration_manager.apply_migration(migration_file, sql_content)

if __name__ == "__main__":
    run_migrations()