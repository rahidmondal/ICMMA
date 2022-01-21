
#Program Status : WORKING ETC - 17/01/2022
#Program Name : M2.py - Module 2 FETCH AND DISTRUBUTE MESSEGE MODULE   .
#Description : This module will contain files which will hgelp in fecthing and grouping messeges .


try :
    import time ,app
    import mysql.connector as mc

except :
    print("Module import Failed - Contact Developer")


def MsgAll():
    print("------------------------Messege-All-Number-------------------")
    Message = input("Enter The Messege You Want To Send : \n ")
    Number = []
    try : 
        print("Connecting to Datbase !!!")
            
        md = mc.connect(
            host="localhost",
            user="root",
            password="1234",
            database = 'SCD'
        )

        print("Conenction Succesfull")
        try :
            myc = md.cursor()
            myc.execute("Select Phone_NO FROM TEACHER")
            TN = myc.fetchall()
            Number.extend(TN)
            myc.execute("Select Phone_NO FROM Student")
            SP = myc.fetchall()
            Number.extend(SP)
            myc.execute("Select Parents_Phone FROM Student")
            PrN= myc.fetchall()
            Number.extend(PrN)

        except :
            print("Error Fecthing")
    except :
        print("Conenction Error ")

    finally :
        md.close()

    print(Number)
    input("Press Any Key To Go Back To Menue Development Still Underway !!")
    menue()

def MsgTch():
    print("---------------------------Messege-All-Teacher------------------")
    Message = input("Enter The Messege You Want To Send : \n ")
    Number = []
    try : 
        print("Connecting to Datbase !!!")
            
        md = mc.connect(
            host="localhost",
            user="root",
            password="1234",
            database = 'SCD'
        )

        print("Conenction Succesfull")
        try :
            myc = md.cursor()
            myc.execute("Select Phone_NO FROM TEACHER")
            TN = myc.fetchall()
            Number.extend(TN)


        except :
            print("Error Fecthing")
    except :
        print("Conenction Error ")

    finally :
        md.close()
    print(Number)
    input("Press Any Key To Go Back To Menue Development Still Underway !!")
    menue()



def MsgCtm():
    print("---------------------------------------------------------------------------------")
    print("                        CUSTOM MESSEGING DASHBOARD                              ")
    print("---------------------------------------------------------------------------------")
    print("""
    1.SELECT CLASS STUDENT
    2.SELECT SUBJECT STUDENT
    3.SELECT SUBJECT TEACHER 
    4.ID FROM RANGE .
    5.Go Back 
    """)
    Ch = int(input("Enter Your Choice : "))
    if Ch == 1 :
        pass
    elif Ch == 2 :
        pass
    elif Ch == 3 :
        pass
    elif Ch == 4 :
        pass
    elif Ch == 5 :
        time.sleep(2)
        menue()

def menue():
    PC = 'VBSS1234'
    print("----------------------------------Messege System-----------------------------------------")
    print("Warning : Caution Advised - Use Of this For Fake News Spreading is against Terms of Use ")
    print("-----------------------------------------------------------------------------------------")
    print(
    """
    1.Messege All Members of School (Teachers+Student) -> Notice/General Information.
    2.Send Messege To all Teacher -> Official Notice[Priveledged]/Others
    3.Custom Messege Send (Group/Individual Catogory)
    4.Go Back 

    """
    )
    ch = int(input("Enter Your Choice : "))
    if ch == 1 :
        MsgAll()
    elif ch == 2 :
        MsgTch()
    elif ch == 3 :
        MsgCtm()
    elif ch == 4 :
        app.MM()
    else :
        print("Invalid Choice !!!")
        input("Press Any key to Continue!!")
        menue()

if __name__ == '__main__':
    menue()









