
#Program Status : WORKING ETC - 17/01/2022
#Program Name : M2.py - Module 2 FETCH AND DISTRUBUTE MESSEGE MODULE   .
#Description : This module will contain files which will hgelp in fecthing and grouping messeges .

from email.message import Message


try :
    import time ,app
    import mysql.connector as mc

except :
    print("Module import Failed - Contact Developer")


def Dc():
    try : 
        print("Connecting to Datbase !!!")
            
        md = mc.connect(
            host="localhost",
            user="root",
            password="1234",
            database = 'SCD'
        )

        print("Conenction Succesfull")
    except :
        print("Conenction Error ")

    finally :
        pass



def MsgAll(M):
    print("Development Underway")
    menue()

def MsgTch(M):
    print("Development Underway")
    menue()

def MsgCtm(M):
    print("Development Underway")
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
    Message = input("Enter The Messege You Want To Send : \n ")
    if ch == 1 :
        MsgAll(Message)
    elif ch == 2 :
        MsgTch(Message)
    elif ch == 3 :
        MsgCtm(Message)
    elif ch == 4 :
        app.MM()
    else :
        print("Invalid Choice !!!")
        input("Press Any key to Continue!!")
        menue()

if __name__ == '__main__':
    menue()








