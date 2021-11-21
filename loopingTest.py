import random as rd
import math
passwordList = ["arslan", "zeeshan","siyapa","mudasar","kevin","faryal","ayaan","harika",
                "inoccent","faraz","kamran","sumaira","fariya","crisha","angela",
                "noor","!","@","#","$","%","&","*","1112","5411","7688","3216","1233","7890","0456"]
for i in range(1,50):
    random_pass_list = ""
    for counter in range(2):
        index = math.floor(rd.random() * 30)
        random_pass_list = random_pass_list + str(passwordList[index])
    print(random_pass_list)