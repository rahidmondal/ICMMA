#Program Initial HAS BEEN COMPLETED ON 05-01-2022
import time,M1,M2
print("Application Starting.......")
time.sleep(2)

def MM():
    print("----------------------------\ICMS/------------------------- ")
    print("Welcome User !! ")
    print("1.Contact Management  ")
    print("2.Messege System      ")
    print("3.LICENCE & CREDITS")
    print("4.ABOUT THE APPLICATION+MANUEL")
    print("5.Logout")
    Ch = input("Please Enter Your Choice : ")
    if Ch == '1':
        time.sleep(5)
        M1.CM()
    elif Ch == '2':
        pass
    elif Ch == '3':
        print()
    elif Ch == '4' :
        print()
    
    elif Ch == '5':
        print("Logging Out...............")
        time.sleep(3)
        print("Logout Succesfull At : ",time.ctime())
        print("**************************************************************************")
        time.sleep(3)
 
    else : 
        print("Invalid Selection !!! ")
        MM()


def init():    
    print("------------------------------Welcome User !!!-----------------------------------")   
    A = input("Please Enter USER_NAME :  ")
    if A == 'PUSHPAM' : 
        B = input("Please Enter Password : ")
        if B == 'RAHID' :
                print("Login In.......")
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
    


