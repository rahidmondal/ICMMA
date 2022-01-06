"""
Program Status : WORKING (ETC - 10-01-2022)
Program Name : M1.py - Module 1 File  .
Description : This File Will Contain Feautures which will help in Contact Management .
Part Of : Contant Managemnt and Bulk Messege Sending Application 
Author : 
        1.RAHID MONDAL
        2.PUSHPAM JHA 

"""

import mysql.connector,time
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database = 'SCD'
    )


