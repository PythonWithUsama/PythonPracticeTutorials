def factorial(facNum):
    ans = 1
    for counter in range(1, facNum+1):
        ans = ans*counter
    # print(facNum, "!"," = ", ans)
    print("Factorial of ", facNum, " is ", ans)
inutNumber = int(input("Enter number to find factorial: "))
factorial(inutNumber)