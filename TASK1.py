import os

file = str(input("enter the file name : "))

if os.path.exists(file):

    file1 = open(file,"r")
    file_contents = file1.read()
    print("reading file file contents")
    print(file_contents)
    file1.close()

else:
    print("error:the file", file,"doesnt exist")