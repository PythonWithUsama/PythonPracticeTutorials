'''
 object  -          define functions in object
iterable -           __iter__() or __getitem__()
iterator -           __next__()
iteration - 
'''
# print on the fly values using this method 
# for i in range(10):
#     print(i)

def gen(n):
    for i in range(n):
        yield i
numbers  = gen(10)
# print(numbers.__next__())
# print(numbers.__next__())
# print(numbers.__next__())
# for num in numbers:
#     print(num)

name = "usama"
iterr = iter(name)
print(iterr.__next__())
print(iterr.__next__())
print(iterr.__next__())
