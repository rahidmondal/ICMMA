#This File Will Contain All The Things which needs to be runn before the actual program 
#This File Will Run only for the first time ..

from logging import error
import mysql.connector,time

try : 
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
        )
    print("Connection Succesfull With Host at",time.ctime())
    try:
        
        mycursor = mydb.cursor()
        '''
        mycursor.execute("CREATE DATABASE SCD")
        print("Database SCD created")
        '''
        try :
            time.sleep(10)
            mycursor.execute("USE SCD")
            print("Creating Tables!")
            mycursor.execute("CREATE TABLE (ID varchar(10) ,TEACHER (NAME VARCHAR(50),ClassTeaching varchar(50),Phone varchar(15),SubjectTeaching varchar(100),Email varchar(50),PRIMARY KEY(ID) );")

            
        except:
            print(error)
        
    except:
        print("Error Creating Database M1-DB-A2")
    
    finally:
        pass






except:
    print("Error Connection Code M1-DB-A1-CONNECTION ERROR TO THE DATABASE")

finally:
    pass

