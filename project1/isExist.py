import os

def is_exist():
    is_file_exist = os.path.exists("/home/acrooxy/Desktop/code/project1/dict.txt")
    # print(os.path.exists("/home/acrooxy/Desktop/code/project1/dict.txt"))

    if is_file_exist == True:
        print("File dict.txt {}.".format("exist"))
    elif is_file_exist == False:
        print("File dict.txt {}.".format("doesn't exist"))

    file = is_file_exist

    is_file_exist_test = os.path.exists("/home/acrooxy/Desktop/code/project1/test.txt")
    # print(os.path.exists("/home/acrooxy/Desktop/code/project1/test.txt"))

    if is_file_exist_test == True:
        print("File test.txt {}.".format("exist"))
    elif is_file_exist_test == False:
        print("File test.txt {}.".format("doesn't exist"))
    print(is_file_exist_test)

    test = is_file_exist_test


    return is_file_exist, is_file_exist_test

# os.path.exists(".server.conf"):
a = is_exist()
print("Def File = %s " % (a[0]))
print("Def Test = %s " % (a[1]))