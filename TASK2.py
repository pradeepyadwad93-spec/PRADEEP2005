
file1 = open("output.txt","w")
text = str(input("enter the text into write in the file: "))

file_contents = file1.write(text)
print("data is succefully written in output.txt")
file1.close()


file1 = open("output.txt","a")
text2 = str(input("enter the additional inpromation into thj7gt6gye file: "))

file_contents = file1.write(text2)
print("data is succefully appended")
file1.close()

file1 = open("output.txt","r")
filepradeep = file1.read()
print("final contents of the output.txt")
print(filepradeep)
file1.close()