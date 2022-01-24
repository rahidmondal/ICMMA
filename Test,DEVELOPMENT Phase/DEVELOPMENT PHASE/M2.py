
#Program Status : WORKING ETC - 17/01/2022
#Program Name : M2.py - Module 2 FETCH AND DISTRUBUTE MESSEGE MODULE   .
#Description : This module will contain files which will hgelp in fecthing and grouping messeges .




try :
    import time ,app,M3
    import mysql.connector as mc

except :
    print("Module import Failed - Contact Developer")

def sm(Num= int, Messege = str , H = int , M = int  ):
    import pywhatkit as p  
    p.sendwhatmsg(Num,Messege,H,M,15,True,5)

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

    for item in Number:
        for i in item :
            M3.send_meessege(i,Message)


    time.sleep(1)
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
    for item in Number:
        for i in item :
            M3.send_meessege(i,Message)


    time.sleep(1)
    menue()

def f():
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
            pass


        except :
            print("Error Fecthing")
    except :
        print("Conenction Error ")

    finally :
        md.close()

    for item in Number:
        for i in item :
            M3.send_meessege(i)
    return Number

    

def MsgCtm():
    print("---------------------------------------------------------------------------------")
    print("                        CUSTOM MESSEGING DASHBOARD                              ")
    print("---------------------------------------------------------------------------------")
    print("""
    1.SELECT CLASS STUDENT
    2.SELECT SUBJECT STUDENT
    3.SELECT SUBJECT TEACHER 
    4.ID FROM RANGE.
    5.Send Messege To Group 
    6.Go Back 
    """)
    Ch = int(input("Enter Your Choice : "))
    if Ch == 1 :
        X = input("SELECT THE CLASS WHERE YOU WANT TO FIND THE STUDNET OF : ")
        Message = input("Enter Messege You want To Send : \n ")
        print(f"THE Following Messege will be Send to {X} ; \n {Message}")

    elif Ch == 2 :
        X = input("INPUT THE SUBJECT INITIALS/CODE : ")
        Message = input("Enter Messege You want To Send : \n ")
        print(f"THE Following Messege will be Send to Students Having  {X}  ; \n {Message}")
        Pass = input("To Continue Execution Enter Passcode : ")
 
        
    elif Ch == 3 :
        X = input("INPUT THE SUBJECT(Teachers) INITIALS/CODE : ")
        Message = input("Enter Messege You want To Send : \n ")
        print(f"THE Following Messege will be Send to Teachers Having  {X}  ; \n {Message}")

        
        
    elif Ch == 4 :
        X = input("Input Lower ID LIMIT : ")
        Y = input("Input Upper ID LIMIT : ")
        Message = input("Enter Messege You want To Send : \n ")

    elif Ch == 5 :
        X = input("Enter Group Name ")
        Message = input("Enter Messege You want To Send : \n ")
        M3.send_messege_group(X,Message)
        

    elif Ch == 6 :
        time.sleep(2)
        menue()

def menue(): 
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
    #menue()
    #MsgAll()
    N = input("Enter Number : ")
    Ms = input("Enter Messege : ")
    H = int(input("Sending Hour : "))
    M = int(input("Sending Min : "))
    sm(N,Ms,16,52)








