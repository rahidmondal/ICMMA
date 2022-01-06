import mysql.connector,time 
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database = 'SCD'
        )
mycursor = mydb.cursor()
mycursor.execute("Drop Table teacher")