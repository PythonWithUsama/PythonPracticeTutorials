#!/usr/bin/python3
import os
import time as T
import math as M
import random as Rd
import requests as R
import colorama as color

# All networks codes
jazzCodes = [300, 301, 302,303,304,305,306,307, 308, 309]
waridCodes = [320, 321, 322, 323, 324, 325]
ufoneCodes = [331, 332, 333, 334, 335, 336, 337]
zongCodes = [311, 312, 313, 314, 315]
telenorCodes = [340, 341, 342, 343, 344, 345, 346, 347]
code = 0
digits = [n for n in range(0, 10)]
# clear screen function
def clearTerminal():
    cmd = 'clear'
    if os.name in ('nt', 'dos'):
        cmd = 'clear'
    os.system(cmd)

# network code select function
def codeSelection(networkCodes):
    code = Rd.choice(networkCodes)
    return code

# get phone nubmers functions
def getNumbers():
    random_str = ""
    for i in range(7):
        index = M.floor(Rd.random()*10)
        random_str += str(digits[index])
    return random_str
clearTerminal()
print(color.Fore.GREEN + "=============Get Pakitan Phone Numbers=============\n")
try:
    print(color.Fore.CYAN + "\t\tSelect Network type\n\n"
          "Jazz\t JazzWarid\t Zong\t Telenor\t Ufone\n")
    selectNetwork = input(color.Fore.LIGHTGREEN_EX + "Type Network here in lowercase...e.g(jazz):")
    inputTotalNumberLen = int(input("How many get numbers?e.g(5):"))
    T.sleep(2)
    print(color.Fore.CYAN + f"{selectNetwork.capitalize()} sim code is {code}")
    T.sleep(1)
    print(color.Fore.CYAN + "please wait...")
    T.sleep(3)
    print(color.Fore.CYAN + "Numbers loading...")
    T.sleep(4)
    for printNum in range(inputTotalNumberLen):
        cdoe = codeSelection(selectNetwork)
        phoneNumbers = getNumbers()
        T.sleep(2)
        print(color.Fore.BLUE + f"+92{code}{phoneNumbers}")
except Exception as error:
    print(error)
