import json , random
from time import sleep
from colorama import Style , Fore
import json
import random
import functions
import webbrowser
from os import system

from colorama import Style, Fore

data = json.load(open("data.json"))


all_col = [
Style.BRIGHT+Fore.RED,
Style.BRIGHT+Fore.CYAN,
Style.BRIGHT+Fore.LIGHTCYAN_EX, 
Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,
Style.BRIGHT+Fore.LIGHTMAGENTA_EX,
Style.BRIGHT+Fore.LIGHTYELLOW_EX
]

ran = random.choice(all_col)

functions.banner()

no = ["no" , "n"]
cont = " "

while cont not in no:
    
    print(ran + "\n\t[1] Encrypt Text\n\t[2] Decrypt Text\n\t[3] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    
    if choice == "1":
        functions.encrypt(ran, data)
        
    elif choice == "2":
        functions.decrypt(ran, data)
        	
    elif choice == "3":
        print("\nCriador: BLACKOUT-777\nRefatorado: def-richardy")
        sleep(1)
        webbrowser.open("https://github.com/BLACKOUT-777")
        exit()
        
    else:
        print(ran + "\nInvalid option")
        exit()
    cont = input(ran + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        system("clear" or "cls")
        functions.banner()
        
    else:
        pass