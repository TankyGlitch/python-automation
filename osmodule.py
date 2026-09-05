import os
#for getting the current working directory.
print(os.getcwd())
#for listing the files present in the current directory
print(os.listdir())
x = os.listdir()
#return type of listdir is list.
print(type(x))
#os.listdir() shows both files AND directories (folders).
for files in os.listdir():

    print("The names are", files)
#isfile() - to check if the given is a file or not
#isdir()  - to check if the given is a directory or not.
#using isdir, isfil returns true or false values. if we want to use in for loop we need to give path and check.
for x in os.listdir():
    if os.path.isfile(x):
        #os.path.isfile(filename)
        print("The file name is: ", x)
    elif os.path.isdir(x):
        #os.path.isdir(dirname)
        print("The dir name is: ", x)
#if we want to check if something even exists as a whole

