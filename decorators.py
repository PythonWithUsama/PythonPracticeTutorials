# def func1():
#     print("I love programming...")
# myfunc = func1
# del func1
# myfunc()

# def funcretuner(num):
#     if num ==0:
#         return print
#     if num == 1:
#         return sum
# print(funcretuner(1))

# def executer(func1):
#     func1(2)
# executer(print)
# def make_pretty(function_name):
#     def inner():
#         print(f"({function_name.__name__}) this is decorated")
#         function_name()
#     return inner
# def ordinary():
#     print("This ordinary...")
#
# # ordinary()
# pretty = make_pretty(ordinary)
# pretty()
# def make_pretty(function_name):
#     def inner():
#         print(f"({function_name.__name__}) this is decorated")
#         function_name()
#     return inner
# @make_pretty
# def ordinary():
#     print("This ordinary...")
#
# ordinary()
def printDivision(funcation_name):
    def inner(num1,num2):
        print(f"({funcation_name.__name__}) is ({num1},{num2}) = {funcation_name(num1,num2)}")
    return inner
@printDivision
def divide(a,b):
    return a/b
@printDivision
def addition(a,b):
    return a+b
@printDivision
def subtraction(a,b):
    return a-b
divide(10,5)
addition(10,10)
subtraction(10,15)