def maxNumber(num1,num2):
    """
this function is about to print the maximum number
    """
    if num1 > num2:
        print(num1, "is maximum...")
    else:
        print(num2, "is maximum...")

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2st number: "))
maxNumber(n1,n2)
