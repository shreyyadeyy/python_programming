#Program to perform operations on dictionary 
#Creating a dictionary 
my_dict= {
    "Name": "ABC",
    "Age":   25,
    "City": "Pune"
}
print("Original Dictionary:", my_dict)

#1. Accessing elements 
print("Name:", my_dict["Name"])

#2. Adding new key-value pair 
my_dict["Country"]="India"
print("After adding country:", my_dict)

#3. Updating value
my_dict["Age"]=26
print("After updating age:", my_dict)


