import time
from models.crud import CRUDModel

class ShowsModel(CRUDModel):
    def __init__(self):
        super().__init__()
        self.table_name = 'shows'
        self.create_table()
        
    
    def create_table(self):
        self.db.connect()        
        self.db.SQL(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                show_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                artist TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL,
                price REAL NOT NULL,
                location_id INTEGER NOT NULL,
                FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE SET NULL  
            )
        ''')
        self.db.close()

    def create_recap_view(self):       
        self.db.SQL("DROP VIEW IF EXISTS shows_recap")
        self.db.SQL(f'''
            CREATE VIEW shows_recap AS
            SELECT 
                shows.show_id,
                shows.name,
                shows.artist,
                shows.date,
                locations.name AS location_name
            FROM shows
            JOIN locations ON shows.location_id = locations.location_id;
        ''')

    def create_detail_view(self):        
        self.db.SQL("DROP VIEW IF EXISTS shows_detail")
        self.db.SQL(f'''
            CREATE VIEW shows_detail AS
            SELECT 
                shows.show_id,
                shows.artist,
                shows.description,
                shows.date,
                shows.price,
                locations.name AS location_name,
                locations.address AS location_address
            FROM shows
            JOIN locations ON shows.location_id = locations.location_id;
        ''')


    def get_shows_recap(self):
        self.db.connect()
        self.create_recap_view()
        time.sleep(0.5)
        result = self.db.SQL("SELECT * FROM shows_recap;")
        self.db.SQL("DROP VIEW IF EXISTS shows_recap;")
        self.db.close()
        return result

    def get_shows_detail(self, id):
        self.db.connect()
        self.create_detail_view()
        time.sleep(0.5)
        result = self.db.SQL(f"SELECT * FROM shows_detail WHERE show_id = {id};")
        self.db.SQL("DROP VIEW IF EXISTS shows_detail;")
        self.db.close()
        return result


    def get_by_location(self, id:int):
        self.db.connect()
        result = self.db.SQL(f"SELECT * FROM {self.table_name} WHERE location_id = {id}")
        self.db.close()
        return result if result else None