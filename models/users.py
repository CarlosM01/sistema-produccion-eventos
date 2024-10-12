from db import DataBase

class User:
    def __init__(self):
        self.db = DataBase()
        self.create_table()

    def create_table(self):
        self.db.connect()        
        self.db.SQL('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone INTEGER NOT NULL,
                password TEXT NOT NULL    
            )
        ''')
        self.db.close()

    def get(self):
        self.db.connect()
        result = self.db.SQL('SELECT * FROM users')
        self.db.close()
        return result

    def get_by_id(self, user_id):
        self.db.connect()
        result = self.db.SQL('SELECT * FROM users WHERE user_id = ?', (user_id,))
        self.db.close()
        return result
    
    def get_by_email(self, email):
        self.db.connect()
        result = self.db.SQL('SELECT * FROM users WHERE email = ?', (email,))
        self.db.close()
        if result:
            return result[0]

    def post(self, data: dict) -> dict:
        self.db.connect()
        result = self.db.SQL('SELECT * FROM users WHERE email = ?', (data['email'],))
        if (result):
            return {'message': 'Este email ya ha sido registrado previamente'}
        self.db.SQL('''
            INSERT INTO users (name, email, phone, password)
            VALUES (?, ?, ?, ?)
        ''', (data['name'], data['email'], data['phone'], data['password']))
        self.db.close()
        return {'message': 'Usuario registrado exitosamente'}

    def patch(self, user_id, name=None, email=None, phone=None, password=None):
        self.db.connect()

        # create sql dynamically
        fields = []
        values = []
        if name:
            fields.append("name = ?")
            values.append(name)
        if email:
            fields.append("email = ?")
            values.append(email)
        if phone:
            fields.append("phone = ?")
            values.append(phone)
        if password:
            fields.append("password = ?")
            values.append(password)

        if fields:
            sql_query = f"UPDATE users SET {', '.join(fields)} WHERE user_id = ?"
            values.append(user_id)
            self.db.SQL(sql_query, tuple(values))

        self.db.close()

    def delete(self, user_id):
        self.db.connect()
        self.db.SQL('DELETE FROM users WHERE user_id = ?', (user_id,))
        self.db.close()
        