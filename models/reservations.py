import time
from models.crud import CRUDModel

class ReservationsModel(CRUDModel):
    def __init__(self):
        super().__init__()
        self.table_name = 'reservations'
        self.create_table()
        
    
    def create_table(self):
        self.db.connect()        
        self.db.SQL(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                seats INTEGER NOT NULL,
                price REAL NOT NULL,
                user_id INTEGER NOT NULL,
                show_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL,
                FOREIGN KEY (show_id) REFERENCES shows(show_id) ON DELETE SET NULL
            )
        ''')
        self.db.close()


    def create_ticket_details(self):        
        self.db.SQL("DROP VIEW IF EXISTS ticket_details")
        self.db.SQL(f'''
            CREATE VIEW ticket_details AS
            SELECT
                reservations.reservation_id,
                users.name AS user_name,   
                reservations.seats,
                reservations.price,
                shows.name AS show_name,   
                shows.artist,
                shows.description,
                shows.date,
                locations.name AS location,
                locations.address
            FROM reservations
            JOIN users ON reservations.user_id = users.user_id
            JOIN shows ON reservations.show_id = shows.show_id
            JOIN locations ON shows.location_id = locations.location_id;
        ''')
        
    def get_ticket_details(self, id):
        self.db.connect()
        self.create_ticket_details()
        time.sleep(0.5)
        result = self.db.SQL(f"SELECT * FROM ticket_details WHERE reservation_id = {id}")
        self.db.SQL("DROP VIEW IF EXISTS ticket_details")
        self.db.close()
        return result
    
    def create_reservation(self, data):
        self.post(data)
        result = self.get_all()
        id = result[-1]['reservation_id']
        return self.get_ticket_details(id)
