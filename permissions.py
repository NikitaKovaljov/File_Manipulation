import os 
from notifypy import Notify
import time

while True:
    for file in os.listdir("/Users/nikitakovaljov/Desktop/Permissions/"):
        perms = os.access(file, os.R_OK | os.W_OK | os.X_OK)
        print("Name of the file: ",file,"\tHis permission is:",perms)

        if perms == True:
            print("This files will be deleted automatically: ",file,"\n")
            os.remove(file)
            notification = Notify()
            notification.title = "Someone is trying to create a file with sudo permissions"
            notification.message = "Dont be afraid, your python script already carrying situation."
            notification.send()

        else: 
            print("Nothing to delete\n")
    time.sleep(.10)
