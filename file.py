#program to read and display file contents 

#specify the file name
filename = "example.txt"

try: 
    #open the file in read mode
    with open(filename,"r") as file:
        contents = file.read()

    #print the contents
    print("Contents of the file:")
    print(contents)

except FileNotFoundError:
    print(f"error: the file '{filename}' does not exist.")
    