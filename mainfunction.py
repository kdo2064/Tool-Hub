from fun.logo import *
import os
import time
from fun.tools import *

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

def mainoption():
    ask=input(f"{yellow}Choose an Option:{green}")
    if ask == "1":
        os.system("clear")
        print(logo)
        menu()
    elif ask == "4":
        about()
        aboutexit()

def aboutexit():
    ask=input(f"{yellow}Do You want to exit[y/n]:{bgreen}")
    if ask=="y" or ask == "Y":
        os.system("python3 main.py")
    if ask=="n" or ask =="N":
        about()
        aboutexit()

def toolsinstall():
    ask=input(f"{yellow}Choose an Option:{bgreen}")
    if ask =="1":
        print("1")
    elif ask == "2":
        print("2")
    elif ask == "3":
        print("2")
    elif ask == "4":
        print("2")
    elif ask == "5":
        print("2")
    elif ask == "6":
        print("2")
    elif ask == "7":
        print("2")
    elif ask == "8":
        print("2")
    elif ask == "9":
        print("2")
    elif ask == "10":
        print("2")
    elif ask == "11":
        print("2")
    elif ask == "12":
        print("2")
    elif ask == "13":
        print("2")
    elif ask == "":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
    elif ask == "2":
        print("2")
