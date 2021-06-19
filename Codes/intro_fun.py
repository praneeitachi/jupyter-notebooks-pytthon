import os
import time
import platform
def my_code(x,y,z):
    print("please wait, we are clearing the screen")
    time.sleep(x)
    os.system(y)
    print("please wait, we are fetching the directories")
    time.sleep(x)
    os.system(z)
if platform.system()=="Windows":
    my_code(2,'cls','dir')
else:
    my_code(3,'clear','ls-lrt')