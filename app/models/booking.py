from app.db.config import get_db_connection  
class Booking:     
    def init(self, id, event_id, bookie_id):         
        self.id = id         
        self.event_id = event_id         
        self.bookie_id = bookie_id      
    @staticmethod     
    def create_booking(event_id, bookie_id):         
        conn = get_db_connection()         
        cur = conn.cursor()         
        cur.execute(""" INSERT INTO booking (show_booked, booked_by)VALUES (%s, %s) RETURNING id""", (event_id, bookie_id))         
        results = cur.fetchone()[0]         
        conn.commit()         
        cur.close()         
        conn.close()         
        return results 