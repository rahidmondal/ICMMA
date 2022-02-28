#Warning : Possibility of Erasing all available Data ....(Please Use ONLY IN FIRST TIME OR SYSYTEM CLEANUP !!)
#Program Status : Completed (06-01-2022).
#Program Name : IR.py - Intial Setup File .
#Description : This File Helps Us Setup the Initial Database and Required Tables For Program.
#Part Of : Contant Managemnt and Bulk Messege Sending Application 


import mysql.connector,time
def DBMS():       
    try : 
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
            )
        print("Connection Succesful With Host at",time.ctime())
        try:
            
            mycursor = mydb.cursor()
            mycursor.execute("DROP DATABASE SCD")

            mycursor.execute("CREATE DATABASE SCD")
            print("Database SCD created")

            try :
                time.sleep(10)
                mycursor.execute("USE SCD")

                print("Creating Tables!")
                mycursor.execute("""
                CREATE TABLE teacher 
                (ID varchar(10) Not Null ,
                F_NAME  varchar(50),
                Class_Teacher  varchar(50),
                PHONE_NO varchar(15),
                Subject_Teaching varchar(50),
                email varchar(50) ,
                primary key(ID)
                )
                """
                )
                print("Teachers Table Created ")

                try:
                    print("Creating Table student")
                    time.sleep(5)
                    mycursor.execute("""CREATE TABLE student
                                        (ID varchar(10) Not Null ,
                                        F_NAME  varchar(50),
                                        Class  varchar(50),
                                        PHONE_NO varchar(15),
                                        Parents_Phone varchar(50),
                                        email varchar(50) ,
                                        primary key(ID))
                                        """)
                    print("Student Table Created !! ")

                except:
                    print("Error !!")
    
            except:
                print("Error !!")
            
        except:
            print("Error Creating Database M1-DB-A2")
        
        finally:
            print(":)")






    except:
        print("Error Connection Code M1-DB-A1-CONNECTION ERROR TO THE DATABASE")

    finally:
        pass
  
print("----------------------------------------------------")
print("INITIAL SETUP BEGINS !!")
print("Warning : Please Don't Run This It will Delete ALL PREVIOUS DATA !! ")
ch = input("Do you wish To Continue(Y/N) : ")
if ch == 'Y' :
    time.sleep(5)
    DBMS()
    print("Setup Completed !! ")
else :
    print("Thanks For using Setup !! ")
    


