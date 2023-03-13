import os
import time
from fun.mainfunction import *
import requests
from fun.logo import *

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

os.system("clear")
print(logo)
print(f"{green}[-]Checking Internet Connection...")

try:
    if __name__=="__main__":
        response = requests.get("https://www.google.com")
        if response.status_code == 200:
            os.system("clear")
            print(logo)
            print(f"{green}[-]Connected... ")
            time.sleep(1)    
            os.system("clear")
            print(logo)
            print(mainmenu)
            mainoption()

except Exception:
    os.system("clear")
    print(logo)
    print(f"""{red}[-]Check Your Internet Connection..and Try Again""")




