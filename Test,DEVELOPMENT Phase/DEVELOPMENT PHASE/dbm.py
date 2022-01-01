import mysql.connector,time

#This File will run for once when program runs for first time .

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
    )

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Contacts")
mycursor.execute("USE Contacts")
mycursor.execute("Create Table admin(name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
print("Program Executed Succesfully")


