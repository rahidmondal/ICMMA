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


def DBC():

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
                pass
        elif tch == 2 :
                pass
        elif tch == 3 :
                pass
        elif tch == 4 :
                pass
        elif tch == 5 :
                pass

def student():
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
                pass
        elif tch == 2 :
                pass
        elif tch == 3 :
                pass
        elif tch == 4 :
                pass
        elif tch == 5 :
                pass

        
      

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
        CM()




