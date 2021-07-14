print("Welcome to GarbageOS!")
from getpass import getpass
import os
f = open("./sys/startAsSetup").read()
if f == "1" :
    os.system('python setup/setup.py')
print("Please login.")
user = input("Type username: ")
passw = getpass("Type password: ")
f_user = open("./sys/user").read()
f_passw = open("./sys/pass").read()
if user == f_user :
    if passw == f_passw :
        print("Welcome,", user,"!")
    else:
        print("Username or password incorrect.")
        os.system("python garbageOS.py")
else:
    print("Username or password incorrect.")
    os.system("python garbageOS.py")
while True:
    cmd = input("Type help for a list of commands. > ")
    if cmd == "help" :
        print("""Commands:
about - Lists info about the system.
help - Displays a list of commands.
clear - Clears console.
launch - Launchs the program in the /sdk/ folder. (/sdk/app.py).
""")
    elif cmd == "about" :
        print("GarbageOS Beta.")
        print("Made by Damien S.")
    elif cmd == "clear" :
        os.system('cls' if os.name=='nt' else 'clear')
    elif cmd == "launch" :
        os.system('python sdk/launch.py')
    else:
        print("Command not found.")