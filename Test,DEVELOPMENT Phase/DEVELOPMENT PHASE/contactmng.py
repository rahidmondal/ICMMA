import mysql.connector
import time 

#Fianl Presenatation Time 
"""

print("Welcome To Contact Manangement Page ")
time.sleep(5)
for i in range(10):
    print(".",flush=True)
    time.sleep(2)

"""
try : 
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
    )

    print(mydb)
    print("Connection succesfully Establised")
    

except :
    print("Connection Error ")

finally : 
    print("Program Executed Succesfully")

