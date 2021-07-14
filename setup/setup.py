import os
from getpass import getpass
print("GarbageOS - SETUP")
name = input("Type username: ")
passw = getpass("Type password: ")
print("Finishing up...")
open("./sys/startAsSetup",'w',encoding = 'utf-8').write("0")
open("./sys/user",'w',encoding = 'utf-8').write(name)
open("./sys/pass",'w',encoding = 'utf-8').write(passw)
print("Finished. Restarting....")
os.system('python garbageOS.py')