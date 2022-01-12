#Neccessary Modules Below 

import time,M1,M2
time.sleep(2)


def MM():
    print("----------------------------\ICMS/------------------------- ")
    print("Welcome User !! ")
    print("1.Contact Management  ")
    print("2.Messege System      ")
    print("3.ABOUT THE APPLICATION+MANUEL")
    print("4.Logout")
    Ch = input("Please Enter Your Choice : ")
    if Ch == '1':
        time.sleep(5)
        M1.CM()

    elif Ch == '2':
        print("Work In Progress ..")
        MM()

    elif Ch == '3' :
        with open("Manuel.txt")as f:
            d = f.read()
            print(d)
            time.sleep(10)
            MM()
       
    elif Ch == '4':
        print("Logging Out...............")
        time.sleep(3)
        print("Logout Succesfull At : ",time.ctime())
        print("**************************************************************************")
        time.sleep(100) #WILL AUTOMNATICALLY CLOSE IF NOT CLOSED WITHIN 100 SEC
 
    else : 
        print("Invalid Selection !!! ")
        MM()

def init(): #COMPLETED 
    print("Application Starting.......")   
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


if  __name__ == "__main__": #COMPLETED
    init()



    


