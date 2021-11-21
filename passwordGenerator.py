import random as rd
import math
passwordList = ["arslan", "zeeshan","siyapa","mudasar","kevin","faryal","ayaan","harika",
                "inoccent","faraz","kamran","sumaira","fariya","crisha","angela",
                "noor","!","@us1","#m","12$","%78o","Agf&","D12l*","1112","5411","7688","3216","1233","7890","0456"]
number_of_password = int(input("Enter number that you want to print password: "))
for i in range(number_of_password):
    random_pass_list = ""
    for counter in range(2):
        index = math.floor(rd.random() * 30)
        random_pass_list = random_pass_list + str(passwordList[index])
    print(f"{random_pass_list}")