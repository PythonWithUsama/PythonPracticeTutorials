# numberlist = [1,2,3,4,5]
# numbers = list(map(lambda a:a*a, numberlist))
# print(numbers)
# numbers = str(list(map(lambda a:a*a, numberlist)))
# print(list(map(lambda a:a*a, numberlist)))
# for value in numbers:
#     print(value)
# for key, numbers in range(len(numberlist)):
#     print(key, numbers)
# n_list = [1,2,3,4,5,6,8,30,99,90,15,33,93]
# for i in range(len(n_list)):
#     if n_list[i]%5==0:
#         print(n_list[i])
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# funcs = [square, cube]
# for i in range(5):
#     value = tuple(map(lambda takeFuncName: takeFuncName(i),funcs))
#     print(value)
# =================================================
# filter
# n_list = [45,21,4,8,7,9,36,4,5,1,212]
# def is_greater(num):
#     return num>10
# # print(list(filter(is_greater,n_list)))
# print(set(filter(is_greater,n_list)))
from functools import reduce
num_list = [i for i in range(1,5)]
# num_list = [1,2,3,4]
print(reduce(lambda x,y:x*y, num_list))