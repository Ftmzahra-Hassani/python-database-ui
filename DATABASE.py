import sqlite3
class Database:
    def init(self , db):
        self.con = sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Contacts (id INTEGER PRIMARY KEY, name TEXT , lname TEXT , address TEXT , phone TEXT)
        """)
        self.con.commit()

    def delete_user(self , id):
        self.cur.execute("DELETE FROM contacts WHERE id =?" , (id,))
        self.con.commit()

    def serch_user(self , text):
        self.cur.execute("""
        SELECT * FROM contacts WHERE name LIKE ?
        """ , ('%' + text + '%',))
        return self.cur.fetchall()

    def show_users(self):
        self.cur.execute("SELECT * FROM contacts")
        return self.cur.fetchall()


    def add_user(self,name , lname , address , phone):
        self.cur.execute("""
        INSERT INTO contacts (name , lname , address , phone)
        VALUES (? ,? ,? ,?)
        """ , (name , lname , address , phone))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM contacts")
        rows = self.cur.fetchall()
        return rows

    def insert(self , name , lname , address , phone):
        self.cur.execute("""
        INSERT INTO Contacts VALUES (NULL , ? , ? , ? , ?)
        """ , (name , lname , address , phone))
        self.con.commit()

    def remove(self , id):
        sql_delete="DELETE FROM Contacts WHERE id = ?"
        self.cur.execute(sql_delete , (id,))
        self.con.commit()

    def update(self , id , name , lname , address , phone):
        self.cur.execute("""
        UPDATE contacts SET name = ? , lname = ? , phone = ? , address = ? WHERE id = ?
        """ , (name , lname , address , phone , id))
        self.con.commit()