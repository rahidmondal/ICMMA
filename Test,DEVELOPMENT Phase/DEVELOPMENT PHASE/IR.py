#This File Will Contain All The Things which needs to be runn before the actual program 
#This File Will Run only for the first time ..

import mysql.connector,time

try : 
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
        )
    print("Connection Succesfull With Host at",time.ctime())
    try:
        '''
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE SCD")
        print("Database SCD created")
        '''
        
    except:
        print("Error Creating Database M1-DB-A2")
    
    finally:
        pass






except:
    print("Error Connection Code M1-DB-A1-CONNECTION ERROR TO THE DATABASE")

finally:
    pass

