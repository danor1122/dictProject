import os

def is_exist():
    path = '/home/acrooxy/Desktop/dictProject/project1/dict.txt'
    is_file_exist = os.path.exists(path)
    # print(is_file_exist)

    if os.path.exists(path) == True: # to get True result remember to give chmod 777 permissions to the file
        return True
        
    elif is_file_exist == False:
        f = open("project1/dict.txt", "w")
        print("File is created now and it's ready to use!")

is_exist()
dict = {}
def write_in_file():


    if is_exist() == True:
        path = '/home/acrooxy/Desktop/dictProject/project1/dict.txt'
        with open(path, 'r') as f:
            lines = len(open(path, 'r'). readlines ()) + 1
            key = str(input("Type english word: "))
            value = str(input("Type polish translation: "))
                          
            print("Dictatory contains %s keys" % lines)

            f = open(path, 'a')
            f.write(str(lines))
            f.write(" " + str(key) + " - "+ str(value) + '\n')
            # f.write("/n")
            # # changing file from append a mode to r read
            f = open(path, "r")
            dict = str(f.read())
            print(dict, "słownik")
            # print(f.read())
            f.close()

#>>> f = open(filepath, "r")
write_in_file()
