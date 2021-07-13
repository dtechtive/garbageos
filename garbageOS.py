print("Welcome to GarbageOS!")

import os

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