#Neccessary Modules Below 

try :
    import time
    import M1
    import M2

except :
    print("Module Import Failed Please Contact The Developer !!!")

time.sleep(1)
def MM():
    print("------------------------------Welcome User !!!---------------------------------")
    print("1.Contact Management  ")
    print("2.Message System      ")
    print("3.ABOUT THE APPLICATION+MANUAL")
    print("4.Logout")
    Ch = input("Please Enter Your Choice : ")
    if Ch == '1':
        time.sleep(1)
        M1.CM()

    elif Ch == '2':
        time.sleep(1)
        M2.menue()

    elif Ch == '3' :
        with open("Manual.txt")as f:
            d = f.read()
            print(d)
            time.sleep(10)
            MM()
       
    elif Ch == '4':
        print("Logging Out...............")
        time.sleep(2)
        print("Logout Successful At : ",time.ctime())
        print("**************************************************************************")
        input("                       Input Any Key  to exit                             ")

    else : 
        print("Invalid Selection !!! ")
        MM()

def init(): 
    print("----------------------------------------------------------------------------")
    print("        ICMMA-INTEGRATED CONTACT MANAGEMENT & MESSAGING APLLICATION         ")
    print("----------------------------------------------------------------------------")
    print("Application Starting.......")
    time.sleep(2)      
    A = input("Please Enter USER_NAME :  ")
    if A == 'PUSHPAM' : 
        B = input("Please Enter Password : ")
        if B == 'RAHID' :
                print("Logging In.......")
                time.sleep(2)
                print("Login Time : ",time.ctime())
                MM()
        else :
                print("INCORRECT PASSWORD ")
                init()

    else:
            print("Incorrect Username !!!")
            init()


if  __name__ == "__main__": 
    init()



    


