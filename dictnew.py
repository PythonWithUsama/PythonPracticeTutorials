# squares = {}
# for numbers in range(0,10):
#     squares[numbers] = numbers*numbers
# print(squares)
names = {}
index = 0
while(True):
    userName = input("Enter name: ")
    names[index] = userName
    index +=1
    print("\n")
    exitp = input("Y/N ")
    if exitp == 'Y' or exitp == 'y':
        break
print(names)
print(names.keys())
print(names.values())
print(names.items())