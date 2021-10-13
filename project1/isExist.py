import os

path = '/home/acrooxy/Desktop/dictProject/project1/dict.txt'
def is_exist():
    is_file_exist = os.path.exists(path)

    if os.path.exists(path) == True: # to get True result remember to give chmod 777 permissions to the file
        return True
    elif is_file_exist == False:
        f = open("project1/dict.txt", "w")
        print("File is created now and it's ready to use!")

def check_dict():
    f = open(path, 'r')
    a = input("Do you want to see dict file?  y/n : ")
    if a == "y":
        print(f.read())
    
def write_in_file():


    if is_exist() == True:
        with open(path, 'r') as f:
            lines = len(open(path, 'r'). readlines ())
            if lines == 0:
                f = open(path, 'w')
                f.write("Welcome to dictionary ! \n")
                print("Welcome to dictionary, file is setted up and ready to use now !")
                exit()
            print(lines)
            while input("Do you want to add new word to dictionary? \n Type \"yes\" or \"no\"? : ") == "yes":
                lines = len(open(path, 'r'). readlines ())
                key = str(input("Type english word: "))
                f = open(path, 'r')
                for line in f:
                    wordlist = [line.split(' ', 2)[1] for line in f]
                    if key in wordlist:
                        print(wordlist)
                        print("This word already exist in dictionary")
                    elif lines > 0:
        
                        value = str(input("Type polish translation: "))          
                        print("Dictatory contains %s keys" % lines)
                        f = open(path, 'a')
                        f.write(str(lines) + ' ' + str(key) + " - " + str(value) + '\n')
                        # f = open(path, "r")
                        # dict = str(f.read())
                        # print(dict, "Dictionary printed")
                        # print(f.read())
                        f.close()
                        break
        check_dict()
    
                # wordsList.append(line.split(None, 1)[1]) # add only first word
                
#>>> f = open(filepath, "r")
# write_in_file()