# def outerfun(msg):
#     def innerfun():
#         print(msg)
#     return innerfun()
# outerfun("hello")
#
# def outer1(msg1):
#     def inner1():
#         print(msg1)
#     inner1()
# outer1("Hi")
# def multiplier_of(n):
#     def multiplier(x):
#         return n*x
#     return multiplier
# res = multiplier_of(3)
# print(res(9))
# print(res.__closure__[0].cell_contents)

def increment(increment_num):
    return increment_num + 1
def decrement(decrement_num):
    return decrement_num - 1
def process(funcation_name,number): #higher order function
    """
    this function is called a higher order function
    """
    result = funcation_name(number)
    return result
ans = process(increment, 5)
ans1 = process(decrement, 5)
print(f"The increment of 5 is {ans}\nThe decrement of 5 is {ans1}")