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
#if we want to check if something even exists . so we do os.path.exists(name) it checks in the cwd.
print("Now we check if a file exists")
print(os.path.exists("anant.py"))
print(os.path.exists("LEARNOS.py"))

#TO CHECK THE CURRENT DIRECTORY we can use "."
print(os.getcwd())
print(os.path.exists(".."))
print(os.path.isdir(".."))
print(os.path.isfile(".."))
#TO CHECK ABSOLUTE PATHS
# path = "C:\\Users\\anant\\PycharmProjects\\python-automation"
# path = r"C:\Users\anant\PycharmProjects\python-automation"
# WE CAN PROVIDE OUR OWN PATHS AND CHECK AS WELL
print("PROVIDING OWN PATHS AND WORKING")
path = r"C:\Users\anant\Desktop\edits"
print(os.path.exists(path))
print(os.path.exists("Anant.png"))
print(os.listdir(path))
print(os.path.exists("../.venv"))
# print(os.path.exists("Arise.png"))
# THE ABOVE DOESNT WORK BECAUSE WE HAVENT GIVEN OS THE DIRECTORY OF IT THATS WHY FOR ANANT.PNG ALSO IT SHOWS FALSE
# ITS CURRENTLY AT THE PYTHON-AUTOMATION FOLDER, so for .venv it gves TRUE
# WE CAN CHECK USING GIVING THE FULL FILE PATH.
print(os.path.exists(r"C:\Users\anant\Desktop\edits\Arise.png"))

#LETS MAKE IT EASIER USING JOIN
# os.path.join()
# Its job is simple:
# Combine pieces of a path into one proper path.
print("USING JOIN")
folder = r"C:\Users\anant\Desktop\edits"
file = "Arise.png"
joining = os.path.join(folder,file)
print(os.path.exists(joining))
# even we can check if that path is a file or folder


# TIME TO CHANGE DIRECTORIES
