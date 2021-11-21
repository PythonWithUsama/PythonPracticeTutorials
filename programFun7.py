def maximumNumber(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2st number: "))
max = maximumNumber(number1, number2)
print("Maximum Number is ===> ", max)