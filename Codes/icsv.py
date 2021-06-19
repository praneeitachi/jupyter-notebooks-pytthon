import csv
input="C:\\Users\\prane\\Desktop\\Python\\Codes\\emp.csv"
file=open(input,"r")
content=csv.reader(file)
for x in content:
    print(x)
file.close()
print(type(content))