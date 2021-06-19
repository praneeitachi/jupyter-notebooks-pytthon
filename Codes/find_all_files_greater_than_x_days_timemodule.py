'''
Requirement:
1. find files which are older than say 70 days
2. it means some files are created before 70 days in a list and some are not
   a) we have to know when files are created - os.path.getctime("path")
   b)current time ( both are in same format)
   c) difference between them ) === 70 days
   
3. we are providing a path 
   a} check if its valid or not
   b) check it must be a file or not if necessary

'''
import os
import string
import datetime
path=input("enter a valid path: \n")
list=os.listdir(path)

if os.path.exists(path):
   print("its a valid path")
if os.path.isdir(path):
   print(" its a directory")
   for x in list:
     x=path+"\\"+x
     #print(x)
     created_time=datetime.datetime.fromtimestamp(os.path.getctime(x))
     current_time=datetime.datetime.now()
     time_diff=current_time - created_time
     #print(dir(time_diff))
     #print(help(time_diff))
     print(time_diff.days)
