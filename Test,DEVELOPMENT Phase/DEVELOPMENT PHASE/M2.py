
#Program Status : WORKING ETC - 17/01/2022
#Program Name : M2.py - Module 2 FETCH AND DISTRUBUTE MESSEGE MODULE   .
#Description : This module will contain files which will hgelp in fecthing and grouping messeges .

import time 
import mysql.connector as mc


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






