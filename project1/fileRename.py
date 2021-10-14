import os

path = '/home/acrooxy/Desktop/dictProject/project1/dict.txt'

def Renamefile():
    
    file_to_change = 'project1/' + str(input("Which file you want to change in project1/ destination:  "))
    # path_new = str(file_to_change)
    # if open(path_new, 'r') == True:
    new_name = str(input("Type new name for this file: "))
    path_new = 'project1/' + new_name
    print("Renamed Completed!")

    os.rename(file_to_change, path_new)
# Renamefile()