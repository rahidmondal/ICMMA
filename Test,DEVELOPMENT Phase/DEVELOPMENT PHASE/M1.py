"""
Program Status : WORKING (ETC - 10-01-2022)
Program Name : M1.py - Module 1 File  .
Description : This File Will Contain Feautures which will help in Contact Management .
Part Of : Contant Managemnt and Bulk Messege Sending Application 
Author : 
        1.RAHID MONDAL
        2.PUSHPAM JHA 

"""
import time
import mysql.connector
import app


def DBC(X):

        try: 
                time.sleep(10)
                print("Connecting Database....")
                mydb = mysql.connector.connect(
                host="localhost",
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



def Teacher():
        print("...........................Teacher-Contacts....................")
        print("""
        1.ADD
        2.EDIT
        3.DELETE
        4.VIEW
        5.Go Back 
        """)
        tch = int(input("Please Enter your Chocie  : "))
        if tch == 1:
                print(".........Teacher-Add-Form.................")
                ID = input("Enter ID :  ")
                F_NAME = input("Full Name : ")
                C_Teacher = input("ClassTeacher Of : ")
                PHONE_NO = input("Phone Number : ")
                Subject_Teaching = input("Intials of Subject Teaching : ")
                Email = input("Email : ")
                stm = "insert into teacher values('{}','{}','{}','{}','{}','{}' )".format(ID,F_NAME,C_Teacher,PHONE_NO,Subject_Teaching,Email)
                DBC(stm)


        elif tch == 2 :
                print(".........Teacher-Edit-Form................")
        elif tch == 3 :
                print(".........Teacher-Delete-Form..............")
        elif tch == 4 :
                print(".........Teacher-view-Form.................")
        elif tch == 5 :
                CM()

        
def student(): #STUDNET ADD BUGGY 
        print("...........................Student-Contacts....................")
        print("""
        1.ADD
        2.EDIT
        3.DELETE
        4.VIEW
        5.Go Back 
        """)
        tch = int(input("Please Enter your Chocie  : "))
        if tch == 1:
              print("...............Student-Add-Form...................")
              ID = input("ID : ")
              F_NAME = input("Full Name : ")
              Class = input("Class : ")
              PHONE_NO = input("Phone Number : ")
              Parents_Number = input("Parents Number : ")
              email = input("Email : ")
              En = "insert into teacher values('{}','{}','{}','{}','{}','{}' )".format(ID,F_NAME,Class,PHONE_NO,Parents_Number,email)
              DBC(En)

        elif tch == 2 :
                print(".............Student-Edit-Form..................")
        elif tch == 3 :
                print(".............Student-Delete-Form................")
        elif tch == 4 :
                print(".............Student-View-Form...................")
        elif tch == 5 :
               CM()

def CM():
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
        student()





