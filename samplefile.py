import csv 

row_count=0
column_count=0

with open("sample.csv","r") as file:
    reader=csv.reader(file)

    for row in reader:
        print(row)
        row_count +=1
print("total number of rows:, row_count")

with open("sample.csv", "r")as file:
    reader=csv.reader(file)

    for col in reader:
        print(col)
        column_count +=1
print("total number of column:", column_count)

#APPEND NEW ROW
with open("sample.csv", "a", newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["PQR", "26", "MUMBAI"])

row_count=0
#READING AGAIN TO CHECK
with open("sample.csv","r")as file:
    reader_new = csv.reader(file)
    for row in reader_new:
       print(row)
       row_count +=1
print("total nnumber of rows after append:", row_count)
