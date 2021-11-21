# import random
# import math
# # d = [1,2,3,4,5]
# # for di in d:
# #     print(int(di))
# digits = [d for d in range(0, 10)]
# print(digits)
#
# anyN = 3
# ans = math.floor(anyN/10)
# print(ans)

# ========================================================================

## importing modules
import random
import math
digits = [i for i in range(0, 10)]
random_str = ""
for n in range(6):
    index = math.floor(random.random() * 10)
    # random_str += str(digits[index])
    random_str = random_str + str(digits[index])
print(random_str)

# generating a random index
## if we multiply with 10 it will generate a number between 0 and 10 not including 10
## multiply the random.random() with length of your base list or str
## displaying the random string
## we can generate any lenght of string we want

## initializing a string

## storing strings in a list