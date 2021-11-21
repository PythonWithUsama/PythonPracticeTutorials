def table(number):
    for counter in range(1, 11):
        print(number, "x", counter, "=", number*counter)

tableNumber = int(input("Enter number that you want to print the table: "))
table(tableNumber)