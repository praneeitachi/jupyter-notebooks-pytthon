import os
os=os.get_terminal_size()
size=os.columns
str=input("enter the string below: ")
str=input("enter the string below: ")
print(str.center(size))
print(str.ljust(size))
print(str.rjust(size))
