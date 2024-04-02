#Password Generator

import string
import random
import time

def simple_passwd_gen(num_of_ch, w_list):
    password = ''
    for i in range(num_of_ch):
        password += random.choice(w_list)
    return password

def multiple_passwd_gen(num_of_ch, passwd_num, w_list):
    list_of_passwds = []
    for i in range(passwd_num):
        password = ''
        for j in range(num_of_ch):
            password += random.choice(w_list)
        list_of_passwds.append(password)
    return(list_of_passwds)

time_string = time.strftime("%Y%m%d-%H%M%S")
f = open(f"Password-File-{time_string}", "at")

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
whole_list = letters + digits + special_chars


while True:
    num_of_chars = input("Enter password length: ")
    if num_of_chars.isdigit():
        num_of_pass_chars = int(num_of_chars)
        break


while True:
    password_number = input("Enter number of requested passwords: ")
    if password_number.isdigit():
        password_count = int(password_number)
        break

if int(password_count) > 0:
    passwd = multiple_passwd_gen(num_of_pass_chars, password_count, whole_list)
    print("Your password is:")
    for i in passwd:
        f.write(i + "\n")
        print(i)
else:
    passwd = simple_passwd_gen(num_of_pass_chars, whole_list)
    f.write(passwd)
    print(f"Your password: {passwd}")



