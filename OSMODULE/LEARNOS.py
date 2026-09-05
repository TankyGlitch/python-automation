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
# chdir means change directory.
# It changes Python's current working directory (CWD).

print(os.getcwd())
os.chdir(r"C:\Users\anant\Desktop\edits")
print(os.getcwd())
print(os.listdir())
print(os.path.exists("Arise.png"))
# now it works because our path is assigned to new directory


# CREATING NEW FOLDER
# we use mkdir
"""x = input("Enter folder name")
while(os.path.exists(x)):
    print("Folder already exists")
    x = input("Enter folder name again")
else:
    os.mkdir(x)
print(os.getcwd())
print(os.path.isdir(x))
print(os.path.exists(x))"""

# WE CAN CREATE NESTED DIRECTORIES AS WELL. WE CAN USE MAKEDIRS("")
# os.makedirs("cars/BMW/photos")
# "Create this structure if necessary. If it already exists, that's fine. exist_ok = True
print("WE CHECK")
os.makedirs("cars/BMW/photos", exist_ok = True)
# os.rename() works for both files and directories.
# os.rename("old.txt", "new.txt")
# os.rename("old_folder", "new_folder")

os.remove() is for files, not folders.
# Python will give you an error because the file isn't there.
# So you can combine it with what you already know:
import os
file = input("Enter file name to delete: ")
if os.path.isfile(file):
    os.remove(file)
    print("File deleted")
else:
    print("File doesn't exist")

# DELETING FOLDERS
os.rmdir()→ deletes a directory.
os.rmdir() can only remove an empty directory.
if it contains files first they need to be deleted.
import os
folder = input("Enter folder name to delete: ")
if os.path.isdir(folder):
    os.rmdir(folder)
    print("Folder deleted")
else:
    print("Folder doesn't exist")


# SEPARATE what the file is called from what type it is.
SUPPOSE:
file = "Arise.png"
name, extension = os.path.splitext(file)
print(name)
print(extension)
O/P:
Arise
.png

# os.path.getsize()
# This tells you the size of a file in bytes.
import os
size = os.path.getsize("Arise.png")
print(size)


# Python can tell you when a file was last modified.
import os
time = os.path.getmtime("Arise.png")
print(time)


# os.environ — Access environment variables stored by the operating system.
import os
print(os.environ.get("USERNAME"))
USED IN API-KEYS.

# os.system() — Execute a command through the operating system.
import os
os.system("dir")  # Windows: lists files/folders