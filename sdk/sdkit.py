
import os


class sdk:
    def exit(): # Exits back to the OS.
        os.system('cd ..')
        os.system('python garbageOS.py')
    def refresh(): # Restarts the program.
        os.system('python sdk/launch.py')