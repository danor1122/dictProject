# from kontrolaPrzeplywu.project1.isExist import *
from isExist import is_exist

print(is_exist()[1])
if is_exist()[1] == True:
    print("We did it ! import {}".format("completed!"))
elif is_exist()[1] == False:
    print("Unforcunatelly we couldn't import the file")

