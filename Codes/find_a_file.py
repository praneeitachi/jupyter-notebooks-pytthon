import os
import string
allowed_paths=string.ascii_uppercase
enter=input("if its a directory 'dir' and file 'file' : \n")
read=input("enter a file name: \n")
existing_path=[]
for item in allowed_paths:
     if os.path.exists(item + ":\\"):
        existing_path.append(item + ":\\")
print(existing_path)
for each_drive in existing_path:
    walk=os.walk(each_drive)
    for r,d,f in walk:
        if enter=="dir":
             if len(d) != 0:
        #print(r)
        #print(f) 
                for each_file in d:
                   if each_file==read:
                      print(os.path.join(r,item))

        else:
             if len(f) != 0:
        #print(r)
        #print(f) 
                 for each_file in f:
                    if each_file==read:
                       print(os.path.join(r,item))
