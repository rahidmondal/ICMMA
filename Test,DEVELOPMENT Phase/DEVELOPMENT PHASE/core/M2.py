from pywhatkit import whats as n 
import time

time = (time.ctime())
n.sendwhatmsg_to_group_instantly("T1",f"Test Mesege 1 sent at '{time}' ",20,True,20)

