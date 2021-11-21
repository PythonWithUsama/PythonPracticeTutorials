# Global variable section
# number1 = 420
# def PrintNumber():
#     # number1 = 520
#     # global number1
#     # global number1
#     # number1 = number1 +30
#     print(number1)
# def printNUmber2():
#     print(number1)
# #
# # printNUmber2()
# # print(number1)
# number1 = number1 +10
# print(number1)
# PrintNumber()
def func1():
    x = 10
    def func2():
        global x
        x = 33
    print("Before calling function 2 ==> ", x)
    func2()
    print("after calling function 2 ===> ", x)
func1()
# print(x) reason because the global keyword make the global variable and store value