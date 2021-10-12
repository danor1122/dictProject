import os

def is_exist():
    path = '/home/acrooxy/Desktop/dictProject/project1/dict.txt'
    is_file_exist = os.path.exists(path)
    print(is_file_exist)

    if os.path.exists(path) == True: # to get True result remember to give chmod 777 permissions to the file
        return True
        
    elif is_file_exist == False:
        f = open("project1/dict.txt", "w")
        print("File is created now and it's ready to use!")

is_exist()

def write_in_file():
    if is_exist() == True:
        path = '/home/acrooxy/Desktop/dictProject/project1/dict.txt'
        count = 1
        with open(path, 'r') as f:
            lines = len(open(path, 'r'). readlines ()) + 1
            print("Dictatory contains %s lines" % lines)
            f = open(path, 'a')
            f.write(str(lines))
            f.write(" Przykladowy tekst do dodania\n")
            # changing file from append a mode to r read
            f = open(path, "r")
            print(f.read())
            f.close()

#>>> f = open(filepath, "r")
write_in_file()
