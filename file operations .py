#CREATE A FILE AND CLOSE IT
file=open("main.txt", "w")
file.write("hi! shreya dey this side \n")
file.write("she is very cute \n")
file.close 
print("the content was written successfully \n")

#READ THE FILE
file=open("main.txt", "r")
content=file.read()
print("content of the file:",content)
file.close

#APPEND THE FILE
file=open("main.txt", "a")
file.write("she the best \n")
print("data was appended succesfully \n")

#UPDATED FILE
file=open("main.txt","r")
content_updated=file.read()
print("updated file:", content_updated)
file.close()
