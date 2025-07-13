#!/usr/bin/env python3

import os

# Change the directory
os.chdir("/home/akharat")

# To ge the current working directory
print(f"Current working directory: {os.getcwd()}")

# To create the new directory

os.mkdir("/home/akharat/ark23")

# To remove the directory

os.rmdir("/home/akharat/ark23")

# To remove a file

os.remove("/home/akharat/test.txt")

# To join the path

FIRST_PATH="/var/log/"
SECOND_PATH="messages"

print(f"Joining two paths: {os.path.join(FIRST_PATH, SECOND_PATH)}")

# To split the directory and the filename from the given file to the path

FILE_PATH="/var/log/message"
FILE_AND_PATH = os.path.split(FILE_PATH)

print(f"Given path: {FILE_PATH}")
print(f"FILE_PATH: {FILE_AND_PATH[0]}")
print(f"FILE_NAME: {FILE_AND_PATH[1]}")

# To check if the file exist

FILE="/var/log/messages"

FILE_EXIST=os.path.exists(FILE)

print(f"Value that file exist variable holds: {FILE_EXIST}")

if FILE_EXIST == True:
    print(f"File {FILE} exist on the system.")
else:
    print("File does not exist")



######## This is an end to the script ################################# Thank you !!! #####################################






