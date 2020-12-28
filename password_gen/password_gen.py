
import random
import os

def random_string(string):
    tmpList = list(string)
    random.shuffle(tmpList)
    return ''.join(tmpList)
while(True):
    print("1.Generate password\n")
    print("2.Exit program\n")
    option = int(input("Your option: "))
    if(option == None):
        print("Please enter option")
    if(option == 1):
        pass_length = int(input("Enter password length: "))
        password: str = ''
        for i in range(pass_length):
            a = str(random.choice("!#$%&*+-.0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_abcdefghijklmnopqrstuvwxyz"))
            password += a
        password = random_string(password)
        print("your password: ", password)
        continue
    if(option == 2):
           break
    else:
        print("Wrong option\n")
    os.system('cls')
    