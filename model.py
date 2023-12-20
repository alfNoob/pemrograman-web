from flask_mysqldb import MySQL

class MahasiswaModel:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM mahasiswa")
        data = cur.fetchall()
        cur.close()
        return data

    def create(self, nama, hobi):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO mahasiswa (nama, hobi) VALUES (%s, %s)", (nama, hobi))
        self.mysql.connection.commit()
        cur.close()

    def get_by_id(self, id):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM mahasiswa WHERE id=%s", (id,))
        data = cur.fetchone()
        cur.close()
        return data

    def update(self, id, nama, hobi):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE mahasiswa SET nama=%s, hobi=%s WHERE id=%s", (nama, hobi, id))
        self.mysql.connection.commit()
        cur.close()

    def delete(self, id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM mahasiswa WHERE id=%s", (id,))
        self.mysql.connection.commit()
        cur.close()
