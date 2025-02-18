from app.db.config import get_db_connection

class Event:
    def __init__(self, id, name, description, date, location, created_by, seats):
        self.id = id
        self.name = name
        self.description = description
        self.date = date
        self.location = location
        self.created_by = created_by
        self.seats = seats

    @staticmethod
    def create_event(name, description, date, location, created_by, seats):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO events (name, description, date, location,seats, created_by)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
        """, (name, description, date, location, int(seats), created_by))
        event_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return event_id

    @staticmethod
    def get_event_by_id(event_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, description, date, location, seats, created_by FROM events WHERE id = %s", (event_id,))
        event_data = cur.fetchone()
        cur.close()
        conn.close()
        if event_data:
            return Event(*event_data)
        return None
    
    @staticmethod
    def get_all_event_by_user_id(user_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, description, date, location, created_by, seats FROM events WHERE created_by = %s", (user_id,))
        event_data = cur.fetchall()
        cur.close()
        conn.close()
        if event_data:
            print()
            return event_data
        return None
    
    @staticmethod
    def get_all_events():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, description, date, location, seats, created_by FROM events")
        event_data = cur.fetchall()
        cur.close()
        conn.close()
        if event_data:
            print()
            return event_data
        return None
    
    def update_seats_by_event_id(event_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE events SET seats = seats - 1 WHERE id = %s" ,(event_id, ))
        conn.commit()
        cur.close()
        conn.close()
        return "Updated Successfully"