import os
import time
import sys
import os.path

print("==============================================================================")
time.sleep(0.4)
print("this script was made to check if the download was done or not you need to \n Specify file name that you want to download !! ")
time.sleep(0.4)
print("==============================================================================")
time.sleep(0.4)
my_input = input("Enter the file name that you want to check if the file in exists: ")
print("every 5 minutes the script will check if the download is done or not !! ")

def shutdown():
    print("just wait !! ")
    time.sleep(300)
    file = os.path.isfile(my_input)
    if file:
        os.system("shutdown /s /t 1")
    else:
        print("the file not in the location !!")
        shutdown()

shutdown()

