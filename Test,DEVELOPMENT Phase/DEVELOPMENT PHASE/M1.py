#Program Status : COMPLETED ON 12-01-2022
#Program Name : M1.py - Module 1 File  .
#Description : This File Will Contain Feautures which will help in Contact Management .



try : 
        import time
        import mysql.connector
        import app 
except :
        print("Module Import Error Please Contact The Developer ")




      
def DBC(X): 

        try: 
                time.sleep(2)
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
                stm = "insert into teacher values('{}','{}','{}','{}','{}','{}')".format(ID,F_NAME,C_Teacher,PHONE_NO,Subject_Teaching,Email)
                DBC(stm)
                print(f"Records with Id Number {ID} succesfully added !!")
                input("Press Any key to Continue.")
                Teacher()
                

                
                

        elif tch == 2 :
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

                while True :
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
                        if C == 'Y':
                                continue
                        else :
                               break
                                
                                

                

        elif tch == 3 : 
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

        elif tch == 4 :  
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
                                        print("ID \t Name \t Class_Teacher \t Phone \t S-Teaching \t Email")
                                        print(C)
                                        #Need To Fixed For imporved User Experience 
                                        for i in C :
                                                pass
                                                #print(i)
                                                #print(i[0],i[1],i[2],i[3],i[4],i[5],i[6] ,sep='\t')
                                        
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
                                Data = myc.fetchall()[0]
                                a = ["ID","F_NAME","CLASS_TEACHER","PHONE_NO","SUBJECT_TEACHING","EMAIL"]
                                print("-----------------------------Individual_Details-------------------")
                                print(a[0],':',Data[0])
                                print(a[1],':',Data[1])
                                print(a[2],':',Data[2])
                                print(a[3],':',Data[3])
                                print(a[4],':',Data[4])
                                print(a[5],':',Data[5])
                                print("-------------------------------------------------------------------")


                        except:
                                print("Error Fetching Data or Data Doesnt Exixts.")
                        finally:
                                mydb.close()
                                time.sleep(2)
                                Teacher()
                
                else:
                        print("Invalid Choice ")
                        Teacher()
                           
        elif tch == 5 :
                CM()

        else :
                Teacher()

      
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

                print("...............Student-Add-Form...................")
                ID = input("ID : ")
                F_NAME = input("Full Name : ")
                Class = input("Class : ")
                PHONE_NO = input("Phone Number : ")
                Parents_Number = input("Parents Number : ")
                email = input("Email : ")
                En = "insert into STUDENT values('{}','{}','{}','{}','{}','{}')".format(ID,F_NAME,Class,PHONE_NO,Parents_Number,email)
                DBC(En)
                print(f"Records with Id Number {ID} succesfully added !!")
                input("Press Any key to Continue..........")
                student()

        elif tch == 2 : 
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

                
        elif tch == 4 :
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
        Teacher()
        





