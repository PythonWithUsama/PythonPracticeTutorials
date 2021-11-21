def raisedToThePower(num1,num2):
    calculatePower = 1
    for coutner in range(1,num2+1):
        calculatePower = calculatePower * num1
    print(num1, " raise to the power ", num2, " is ", calculatePower)
inputNumber1 = int(input("Enter 1st number: "))
inputNumber2 = int(input("Enter 2st number: "))
raisedToThePower(inputNumber1,inputNumber2)
