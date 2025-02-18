from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.db.config import get_db_connection
from contextlib import contextmanager
from psycopg2 import Error as PostgresError

class User(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    @staticmethod
    @contextmanager
    def _get_db_cursor():
        """Context manager for database cursor"""
        conn = get_db_connection()
        try:
            cur = conn.cursor()
            yield cur
            conn.commit()
        except PostgresError as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def create_user(username, password):
        try:
            with User._get_db_cursor() as cur:
                password_hash = generate_password_hash(password)
                cur.execute(
                    "INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING id",
                    (username, password_hash)
                )
                user_id = cur.fetchone()[0]
                return User(user_id, username, password_hash)
        except PostgresError as e:
            raise Exception(f"Database error occurred: {str(e)}")

    @staticmethod
    def get_user_by_username(username):
        try:
            with User._get_db_cursor() as cur:
                cur.execute(
                    "SELECT id, username, password_hash FROM users WHERE username = %s",
                    (username,)
                )
                user_data = cur.fetchone()
                return User(*user_data) if user_data else None
        except PostgresError as e:
            raise Exception(f"Database error occurred: {str(e)}")

    @staticmethod
    def get_user_by_id(user_id):
        try:
            with User._get_db_cursor() as cur:
                cur.execute(
                    "SELECT id, username, password_hash FROM users WHERE id = %s",
                    (user_id,)
                )
                user_data = cur.fetchone()
                return User(*user_data) if user_data else None
        except PostgresError as e:
            raise Exception(f"Database error occurred: {str(e)}")

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
