import random as rd
import math
import time as t
phoneCodeList = [303,304,305,306,307]
numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def codeSelection():
    code = rd.choice(phoneCodeList)
    return code
def phoneGenerator():
    random_str = ""
    for counter in range(7):
        index = math.floor(rd.random()*10)
        random_str += str(numberList[index])
    return random_str

phoneCode = codeSelection()
print("=============Get Pakitan Phone Numbers=============\n")
try:
    inputDigit = int(input("How many get numbers? put number(e.g:5):"))
    t.sleep(2)
    print("please wait...")
    t.sleep(3)
    print(f"Number code is {phoneCode}")
    t.sleep(3)
    print("Numbers loading....")
    t.sleep(4)
    for i in range(inputDigit):
        phoneNumber = phoneGenerator()
        t.sleep(1)
        print(f"+92{phoneCode}{phoneNumber}")
except Exception as error:
    print(error)