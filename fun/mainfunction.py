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


# first option

def mainoption():
    ask=input(f"{yellow}Choose an Option:{green}")
    if ask == "1":
        os.system("clear")
        print(logo)
        menu()
        toolsinstall()
    elif ask == "2":
        uninstall()
    elif ask == "3":
        updatetool()
    elif ask == "4":
        about()
        aboutexit()
    elif ask=="5":
        os.system("exit")
    else:
        print(f"{red}invalied option..! Try again")
        time.sleep(0.5)
        os.system("clear")
        print(logo)
        print(mainmenu)
        mainoption()

# about option 

def aboutexit():
    ask=input(f"{yellow}Choose Option:{bgreen}")
    if ask=="1":
        kdoinsta()
    elif ask == "2":
        hawkinsta()
    elif ask == "3":
        krishnainsta()
    elif ask=="0":
        os.system("clear")
        print(logo)
        print(mainmenu)
        mainoption()
    else:
        print(f"{red}invalied option..! Try again")
        time.sleep(0.5)
        about()
        aboutexit()

# tool option

def toolsinstall():
    ask=input(f"{yellow}Choose an Option:{bgreen}")
    if ask =="1":
        os.system("cd $HOME && mkdir Cyber-D-Virus")
        cyberdvi()
        cyberdvirus()
    elif ask == "2":
        camphish()
    elif ask == "3":
        tigervirus()
    elif ask == "4":
        THYDRA()
    elif ask == "5":
        BruteX()
    elif ask == "6":
        ighack()
    elif ask == "7":
        SocialBox()
    elif ask == "8":
        maskphish()
    elif ask == "9":
        easyhack()
    elif ask == "10":
        IPTracer()
    elif ask == "11":
        mrphish()
    elif ask == "12":
        Pyshell()
    elif ask == "13":
        FacebookBruteForce()
    elif ask == "14":
        sherlock()
    elif ask == "15":
        smsbomber300free()
    elif ask == "16":
        spymer()
    elif ask == "17":
        darkdump()
    elif ask == "18":
        routersploit()
    elif ask == "19":
        EmailSpammer()
    elif ask == "20":
        emailspam()
    elif ask == "21":
        AdminHack()
    elif ask == "22":
        sqlmap()
    elif ask == "23":
        AndroRAT()
    elif ask == "24":
        TermuxCyberArmy()
    elif ask == "25":
        Ransomware()
    elif ask == "26":
        Brutegram()
    elif ask == "27":
        cctv()
    elif ask == "28":
        FoxWebInfo()
    elif ask == "29":
        foxuserfinder()
    elif ask == "30":
        foxddoser()
    elif ask == "0":
        print(logo)
        print(mainmenu)
        mainoption()
    else:
        print(f"{red}invalied option..! Try again")
        time.sleep(0.5)
        os.system("clear")
        print(logo)
        menu()
        toolsinstall()

# cyber-d virus

def cyberdvirus():
    ask=input(f"{yellow}Choose Option:{bgreen}")
    if ask=="1":
        love()
        cyberdvi()
        cyberdvirus()
    elif ask == "2":
        loveyekpal()
        cyberdvi()
        cyberdvirus()
    elif ask == "3":
        kingofking()
    elif ask=="0":
        print(logo)
        print(mainmenu)
        mainoption()
    else:
        print(f"{red}invalied option..! Try again")
        time.sleep(0.5)
        about()
        aboutexit()