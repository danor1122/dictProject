# from kontrolaPrzeplywu.project1.isExist import *
from isExist import is_exist

print(is_exist())
if is_exist() == True:
    print("We did it ! import {}".format("completed!"))
elif is_exist() == False:
    print("Unforcunatelly we couldn't import the file")

