import time
import string
from random import *
while True:
    tool = input("1. generate, 2. exit: ")

    if tool == "1":
        print("generating password")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(choice(characters) for x in range(randint(8, 16)))
        print(password)
    
    if tool == "2":
        print("goodbye")
        time.sleep(3)
        quit()