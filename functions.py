from colorama import Style , Fore
import random
import json , random

def encrypt(ran, data):
    text = input(ran + "\nEnter text to encrypt: " + Style.BRIGHT+Fore.LIGHTGREEN_EX)
    enc = ""
    for i in text:
        for j in data.keys():
            if i == j:
                enc = enc + data.get(i)
        if i not in data.keys():
            enc = enc +i
    print(Style.BRIGHT+Fore.LIGHTGREEN_EX + "\n\t\tCopy and send the text: \n\n" + enc)


def decrypt(ran, data):
    text = input(ran + "\nEnter text to decrypt: " + Style.BRIGHT + Fore.LIGHTGREEN_EX)
    dec = ""
    for i in text:
        for key , value in data.items():
            if i == value:
                dec = dec + key

        if i not in data.values():
            dec = dec +i
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "\n\t\tCopy and send the text: \n\n" + dec)


def banner():
    print("""
__  __                    ____                  _   
|  \/  | ___   ___  _ __  / ___|_ __ _   _ _ __ | |_ 
| |\/| |/ _ \ / _ \| '_ \| |   | '__| | | | '_ \| __|
| |  | | (_) | (_) | | | | |___| |  | |_| | |_) | |_ 
|_|  |_|\___/ \___/|_| |_|\____|_|   \__, | .__/ \__|
                                     |___/|_|
""")