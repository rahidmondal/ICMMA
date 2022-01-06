#Program Initial HAS BEEN COMPLETED ON 05-01-2022

import M1,M2,time
print("Application Starting.......")
time.sleep(2)


def app():
    print("----------------------------\ICMS/------------------------- ")
    print("Welcome User !! ")
    print("Login Time : ",time.ctime())
    print("1.Contact Management  ")
    print("2.Messege System      ")
    print("3.LICENCE & CREDITS")
    print("4.ABOUT THE APPLICATION+MANUEL")
    print("5.Logout")
    Ch = input("Please Enter Your Choice : ")
    if Ch == '1':
        pass
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
        app()
    








def init():
    print("------------------------------Welcome User !!!-----------------------------------")
    Z = input("Please Enter USER_NAME :  ")

    try :

        if Z == 'PUSHPAM' :
            X = input("Please Enter Password : ")
            if X == 'RAHID' :
                print("Login In.......")
                time.sleep(2)
                app()
            else :
                print("INCORRECT PASSWORD ")
                init()

        else:
            print("Incorrect Username !!!")
            init()

            
    except:
        print("Something Went Wrong")
        init()






#Test Area Below !!!!!

init()
