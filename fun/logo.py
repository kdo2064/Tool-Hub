import os

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



logo=f"""
{bgreen}╭━━━━╮╱╱╱╱╭╮╱╱{byellow}╭╮╱╭╮╱╱╭╮{bgreen}
┃╭╮╭╮┃╱╱╱╱┃┃╱╱{byellow}┃┃╱┃┃╱╱┃┃{bgreen}
╰╯┃┃┣┻━┳━━┫┃╱╱{byellow}┃╰━╯┣╮╭┫╰━╮{bgreen}
╱╱┃┃┃╭╮┃╭╮┃┣━━{byellow}┫╭━╮┃┃┃┃╭╮┃{bgreen}
╱╱┃┃┃╰╯┃╰╯┃╰┳━{byellow}┫┃╱┃┃╰╯┃╰╯┃{bgreen}
╱╱╰╯╰━━┻━━┻━╯{byellow}╱╰╯╱{byellow}╰┻━━┻━━╯{bgreen}
    {bcyan}Tool by Cyber-D{red}[{purple}v{green}1.0{red}]
"""

secondlogo=f"""
{bgreen}╭━━━━╮╱╱╱╱╭╮╱╱{byellow}╭╮╱╭╮╱╱╭╮{bgreen}
┃╭╮╭╮┃╱╱╱╱┃┃╱╱{byellow}┃┃╱┃┃╱╱┃┃{bgreen}
╰╯┃┃┣┻━┳━━┫┃╱╱{byellow}┃╰━╯┣╮╭┫╰━╮{bgreen}
╱╱┃┃┃╭╮┃╭╮┃┣━━{byellow}┫╭━╮┃┃┃┃╭╮┃{bgreen}
╱╱┃┃┃╰╯┃╰╯┃╰┳━{byellow}┫┃╱┃┃╰╯┃╰╯┃{bgreen}
╱╱╰╯╰━━┻━━┻━╯╱╰╯╱{byellow}╰┻━━┻━━╯{bgreen}
"""


mainmenu=f"""
_____________________
|{white}----{bcyan}Cyber-D Army{white}----{red}|
|                    {red}|
|{white}-{red}x{white}-{red}[{green}1{red}]{white}-{yellow}>{green}Tools{red}       |
|{white}-{red}x{white}-{red}[{green}2{red}]{white}-{yellow}>{green}Unintall{red}    |
|{white}-{red}x{white}-{red}[{green}3{red}]{white}-{yellow}>{green}Update{red}      |
|{white}-{red}x{white}-{red}[{green}4{red}]{white}-{yellow}>{green}About {red}      |
|{white}-{red}x{white}-{red}[{green}5{red}]{white}-{yellow}>{green}Exit {red}       |
|____________________|

"""

def about():
    os.system("clear")
    print(secondlogo)
    print(f"""
{bcyan}[-]This tool is Created By Cyber-D Army

{yellow}Author    :  K.D.O x Hawk x Krishna
Github    :  https://github.com/kdo2064
Telegram  :  https://t.me/cyberdoffficial
Discord   :  https://discord.gg/v8FVzsuH
Version   :  1.0

{red}[-]Warning:

{blue}This Tool is made for educational purpose
only ! Author will not be responsible for
any misuse of this toolkit !

{bpurple}[-]About Update:
{bred}some Bug fixed..! and added audio

{bgreen}[-]Dev SocialMedia
{red}[{byellow}1{red}]{white}-{red}>{bcyan}K.D.O   : Instagram
{red}[{byellow}2{red}]{white}-{red}>{bcyan}Hawk    : Instgram
{red}[{byellow}3{red}]{white}-{red}>{bcyan}krishna : Instagram
{red}[{byellow}0{red}]{white}-{red}>{bcyan}Exit
""")


def menu():
    print(f"""
{red}[{green}1{red}]{white}-{red}>{bcyan}Cyber-D Virus          {red}[{green}16{red}]{white}-{red}>{bcyan}spymer
{red}[{green}2{red}]{white}-{red}>{bcyan}CamPhish               {red}[{green}17{red}]{white}-{red}>{bcyan}darkdump
{red}[{green}3{red}]{white}-{red}>{bcyan}TigerVirus             {red}[{green}18{red}]{white}-{red}>{bcyan}routersploit
{red}[{green}4{red}]{white}-{red}>{bcyan}T-HYDRA                {red}[{green}19{red}]{white}-{red}>{bcyan}Email-Spammer
{red}[{green}5{red}]{white}-{red}>{bcyan}BruteX                 {red}[{green}20{red}]{white}-{red}>{bcyan}emailspam
{red}[{green}6{red}]{white}-{red}>{bcyan}ighack                 {red}[{green}21{red}]{white}-{red}>{bcyan}AdminHack
{red}[{green}7{red}]{white}-{red}>{bcyan}SocialBox-Termux       {red}[{green}22{red}]{white}-{red}>{bcyan}sqlmap 
{red}[{green}8{red}]{white}-{red}>{bcyan}maskphish              {red}[{green}23{red}]{white}-{red}>{bcyan}AndroRAT
{red}[{green}9{red}]{white}-{red}>{bcyan}EasY_HaCk              {red}[{green}24{red}]{white}-{red}>{bcyan}TermuxCyberArmy
{red}[{green}10{red}]{white}-{red}>{bcyan}IP-Tracer             {red}[{green}25{red}]{white}-{red}>{bcyan}Ransomware 
{red}[{green}11{red}]{white}-{red}>{bcyan}mrphish               {red}[{green}26{red}]{white}-{red}>{bcyan}Brutegram
{red}[{green}12{red}]{white}-{red}>{bcyan}Pyshell               {red}[{green}27{red}]{white}-{red}>{bcyan}CCTV
{red}[{green}13{red}]{white}-{red}>{bcyan}Facebook-BruteForce   {red}[{green}28{red}]{white}-{red}>{bcyan}Fox-WebINFO
{red}[{green}14{red}]{white}-{red}>{bcyan}sherlock              {red}[{green}29{red}]{white}-{red}>{bcyan}fox_userfinder
{red}[{green}15{red}]{white}-{red}>{bcyan}SMS-Bomber-300-Free   {red}[{green}30{red}]{white}-{red}>{bcyan}Fox-DDOSER 

{red}[{green}0{red}]{white}-{red}>{bcyan}Exit 
    """)

def cyberdvi():
    os.system("clear")
    print(logo)
    print(f"""
{red}[-]Warning:

{blue}This Virus can be Danger, Don't use
this virus for fun!

{bgreen}[-]Cyber-D Virus
{red}[{byellow}1{red}]{white}-{red}>{bcyan}Love(apk)             : +18 Harmless
{red}[{byellow}2{red}]{white}-{red}>{bcyan}Love yek pal ka(apk)  : Harmful
{red}[{byellow}3{red}]{white}-{red}>{bcyan}King of King(website) : Instagram
{red}[{byellow}0{red}]{white}-{red}>{bcyan}Exit
""")
