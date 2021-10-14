# from kontrolaPrzeplywu.project1.isExist import *
from isExist import is_exist, write_in_file, check_dict
from fileRename import Renamefile
from findAWords import findfn
import os

print("""\n \t\t\t Script is made by Damian - ACROOXY \n
\t Welcome to Dictionary""")
decision = None
while decision != "exit":  
    decision = input("""1 Add an word ito file\n2 Find a word\n3 Dictionary check\n\n9 File Rename\n\nTo exit type \"exit\"\n""")  
    if decision == '1':
        write_in_file()
    elif decision == '2':
        findfn()
    elif decision == '3':
        check_dict()
    elif decision == '9':
        Renamefile()

        

    else:
        print("You have choosen a wrong option.")
        