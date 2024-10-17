from models.crud import CRUDModel

class LocationsModel(CRUDModel):
    def __init__(self):
        super().__init__()
        self.table_name = 'locations'
        self.create_table()

    def create_table(self):
        self.db.connect()        
        self.db.SQL(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                location_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                capacity INTEGER NOT NULL
            )
        ''')
        self.db.close()

    