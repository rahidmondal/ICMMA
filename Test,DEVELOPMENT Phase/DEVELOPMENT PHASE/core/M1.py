#Program Status : COMPLETED ON 12-01-2022
#Program Name : M1.py - Module 1 File  .
#Description : This File Will Contain Feautures which will help in Contact Management .

import time
import mysql.connector
import app


      
def DBC(X): #COMPLETED 

        try: 
                time.sleep(10)
                print("Connecting Database....")
                mydb = mysql.connector.connect(host="localhost",
                user="root",
                password="1234",
                database = 'SCD'
                )

                print("Database Connected ..")
                try :
                        myc = mydb.cursor()
                        myc.execute(X)
                        mydb.commit()
                        print("Record Added Succesfully !!")
                        
                except :
                        mydb.rollback()
                        print("Unssuccessfull Transaction .. ")

                finally :
                        mydb.close() 
                
        except:
                print("Error Connecting To Database ")

                
def Teacher(): #completed 
        print("...........................Teacher-Contacts....................")
        print("""
        1.ADD
        2.EDIT
        3.DELETE
        4.VIEW
        5.Go Back 
        """)
        tch = int(input("Please Enter your Chocie  : "))
        if tch == 1: #Completed
                x = "Y"
                if x=="Y":
                        print(".........Teacher-Add-Form.................")
                        ID = input("Enter ID :  ")
                        F_NAME = input("Full Name : ")
                        C_Teacher = input("ClassTeacher Of : ")
                        PHONE_NO = input("Phone Number : ")
                        Subject_Teaching = input("Intials of Subject Teaching : ")
                        Email = input("Email : ")
                        stm = "insert into teacher values('{}','{}','{}','{}','{}','{}')".format(ID,F_NAME,C_Teacher,PHONE_NO,Subject_Teaching,Email)
                        DBC(stm)
                        X = input("Do You Want To add more Data ?(Y/N) :  ")
                time.sleep(5)
                Teacher()

        elif tch == 2 : #Completed
                print(".........Teacher-Edit-Form................")
                print("""
                Chose From The following :
                1.ID
                2.F_NAME
                3.CLASS_TEACHER
                4.PHONE_NO
                5.Subject_Teaching
                6.Email.
                """)

                while True:
                        Id = input("ID : ")
                        table_name = "Teacher"
                        colum = input("ENTER THE COLUM NAME : ")
                        value = input("Value : ")
                        mydb = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="1234",
                                        database = 'SCD')

                        myc = mydb.cursor()
                        myc.execute(f"Update {table_name} set {colum} = '{value}' where ID = {Id}")
                        mydb.commit()
                        print("Record Added Succsfully ")
                        time.sleep(2)
                        mydb.close()
                        C = input("Do you wish to Edit more ?(Y/N) : ")
                        if C == 'N':
                                break
                        else :
                                continue

                Teacher()

        elif tch == 3 : #Completed
                print(".........Teacher-Delete-Form..............")
                ID = input("Please Enter the ID : ")
                try : 
                        mydb = mysql.connector.connect(host="localhost",
                        user="root",
                        password="1234",
                        database = 'SCD')
                        print("Connected To Database ...")
                        try :
                                myc = mydb.cursor()
                                myc.execute("Select * From Teacher where ID = '{}'".format(ID))
                                G = myc.fetchall()
                                print(G)
                                x = input("Do You Want To Continue deleting (Y/N): ")
                                if x == 'Y':
                                        try : 
                                                        
                                                myc.execute("Delete from teacher where ID = '{}'".format(ID))
                                                mydb.commit()
                                                print("Records Deleted Succesfully !! ")
                                        except:
                                                mydb.rollback()
                                                print("Transaction Unsuccesfull !!")
                                        
                                        finally:
                                                mydb.close()     
                        except:
                                print("Error Fetching Data ...")
                except : 
                        print("Error Connecting To Database !!! ")
                finally:
                        Teacher()

        elif tch == 4 :  #Completed.
                print(".........Teacher-view-Form.................")
                print("1.VIEW ALL TEACHER ")
                print("2.View Individual ")
                x = input("Enter Choice : ")
                try :
                                mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database = 'SCD'
                                )
                                print("Database Connected Succesfully ")
                except :
                                print("Erro Connecting Database...")

                if x == "1":                               
                                try :
                                        myc = mydb.cursor()
                                        myc.execute(f"SELECT * FROM TEACHER ")
                                        C = myc.fetchall()
                                        print(C)
                                except:
                                        print("Error Fetching Data or Data Doesnt Exixts.")
                                finally:
                                        mydb.close()
                                        Teacher()
                
                elif x == '2':
                        ID = input("Enter The Id : ")
                        try :
                                myc = mydb.cursor()
                                myc.execute(f"SELECT * FROM TEACHER where ID = {ID}")
                                C = myc.fetchall()
                                print(C)
                        except:
                                print("Error Fetching Data or Data Doesnt Exixts.")
                        finally:
                                mydb.close()
                                Teacher()
                
                else:
                        print("Invalid Choice ")
                        Teacher()
                           
        elif tch == 5 : #COMPLTED
                CM()
      
def student(): #COMPLETED
        print("...........................Student-Contacts....................")
        print("""
        1.ADD
        2.EDIT
        3.DELETE
        4.VIEW
        5.Go Back 
        """)
        tch = int(input("Please Enter your Chocie  : "))
        if tch == 1: #Completed. - SOLVE THE LOOP ISSUE HERE 
                x = "Y"
                if x=="Y":
                        print("...............Student-Add-Form...................")
                        ID = input("ID : ")
                        F_NAME = input("Full Name : ")
                        Class = input("Class : ")
                        PHONE_NO = input("Phone Number : ")
                        Parents_Number = input("Parents Number : ")
                        email = input("Email : ")
                        En = "insert into STUDENT values('{}','{}','{}','{}','{}','{}')".format(ID,F_NAME,Class,PHONE_NO,Parents_Number,email)
                        DBC(En)
                        X = input("Do You Want To add more Data ?(Y/N) :  ")
                time.sleep(5)
                student()

        elif tch == 2 : #COMPLETED 
                print(".............Student-Edit-Form..................")
                print("""
                Chose From The following :
                1.ID
                2.F_NAME
                3.CLASS
                4.PHONE_NO
                5.Parents_Phone
                6.email
                """)

                while True:
                        Id = input("ID : ")
                        table_name = "student"
                        colum = input("ENTER THE COLUM NAME : ")
                        value = input("Value : ")
                        mydb = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="1234",
                                        database = 'SCD')

                        myc = mydb.cursor()
                        myc.execute(f"Update {table_name} set {colum} = '{value}' where ID = {Id}")
                        mydb.commit()
                        print("Record Added Succsfully ")
                        time.sleep(2)
                        mydb.close()
                        C = input("Do you wish to Edit more ?(Y/N) : ")
                        if C == 'N':
                                break
                        else :
                                continue

                student()
                
        elif tch == 3 : #Completed
                print(".............Student-Delete-Form................")
                ID = input("Please Enter the ID : ")
                try : 
                        mydb = mysql.connector.connect(host="localhost",
                        user="root",
                        password="1234",
                        database = 'SCD')
                        print("Connected To Database ...")
                        try :
                                myc = mydb.cursor()
                                myc.execute("Select * From student where ID = '{}'".format(ID))
                                G = myc.fetchall()
                                print(G)
                                x = input("Do You Want To Continue deleting (Y/N): ")
                                if x == 'Y':
                                        try : 
                                                        
                                                myc.execute("Delete from student where ID = '{}'".format(ID))
                                                mydb.commit()
                                                print("Records Deleted Succesfully !! ")
                                        except:
                                                mydb.rollback()
                                                print("Transaction Unsuccesfull !!")
                                        
                                        finally:
                                                mydb.close()     
                        except:
                                print("Error Fetching Data ...")
                except : 
                        print("Error Connecting To Database !!! ")
                finally:
                        student()

                
        elif tch == 4 : #Completed
                print(".............Student-View-Form...................")
                print("1.VIEW ALL TEACHER ")
                print("2.View Individual ")
                x = input("Enter Choice : ")
                try :
                                mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="1234",
                                database = 'SCD'
                                )
                                print("Database Connected Succesfully ")
                except :
                                print("Erro Connecting Database...")

                if x == "1":                               
                                try :
                                        myc = mydb.cursor()
                                        myc.execute("SELECT * FROM student")
                                        C = myc.fetchall()
                                        print(C)
                                except:
                                        print("Error Fetching Data or Data Doesnt Exixts.")
                                finally:
                                        mydb.close()
                                        student()
                
                elif x == '2':
                        ID = input("Enter The Id : ")
                        try :
                                myc = mydb.cursor()
                                myc.execute(f"SELECT * FROM student where ID = {ID}")
                                C = myc.fetchall()
                                print(C)
                        except:
                                print("Error Fetching Data or Data Doesnt Exixts.")
                        finally:
                                mydb.close()
                                student()
                
                else:
                        print("Invalid Choice ")
                        Teacher()

        elif tch == 5 :
               CM()




def CM(): #COMPLETED
        print("--------------------------Contact Management-----------------------")
        print("""
        1.TEACHER
        2.STUDENT
        3.Go Back
        """)
        CH = int(input("Enter Your Choice : "))
        if CH == 1:
                time.sleep(2)
                Teacher()
        
        elif CH == 2 :
                time.sleep(2)
                student()
        
        elif CH== 3 :
                time.sleep(2)
                app.MM()

                

        else :
                print("INVALID CHOICE PLEASE TRY AGAIN....")
                CM()

if __name__ == '__main__':
        CM()
        





