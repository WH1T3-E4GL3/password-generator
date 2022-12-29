import random
import os

os.system("figlet password generator")

print("\033[32m================================================================\033[0m")
print("\033[32mTool Author    : white-eagle\033[0m")
print("\033[33mGithub 	      : https://github.com/WH1T3-E4GL3/\033[0m")
print("\033[33mTelegram       : https://t.me/Ka_KsHi_HaTaKe\033[0m")
print("\033[32m================================================================\033[0m")

length=int(input("Enter The Length Of The Password  : "))

print (" ")

print ("=====================================================")

print ("Here is the password for you ")

print (" ")

char="abcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"

password= (" ")

for i in range(length):


     password+=random.choice(char)
     

print(password)

print (" ")

print ("=====================================================")

print ("                 Belive me it is strong              ")

print (" ")
