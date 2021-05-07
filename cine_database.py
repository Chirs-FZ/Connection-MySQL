import mysql.connector

class MyDatabase:
    def open_connection(self):
        connection = msql.connector.connect
        (host="localhost"
        user="root"
        passw=""
        database="db_red_social")
        return connection
    
    def insert_db(self, email, pwd, age):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_CINE_DISEÑO(BOLETOS, PRECIO, BUTAKAS, SALA) VALUES (%s,%s,%s)"
        data = (email ,pwd, age)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()
