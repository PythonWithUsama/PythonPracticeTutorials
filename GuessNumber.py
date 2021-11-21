n = 11
count = 5
while(True):
    print("Your chances left ===> ", count)
    guessN = int(input("Enter Number to guess number: "))
    if guessN > n:
        print("Entered number is greater than guess number..try again")
    elif guessN <n:
        print("Entered number is less than guess number...try again")
    elif guessN == n:
        print("congratulations!...\nEntered number perfect match guess number")
        break
    if count <=1:
        break
    count = count - 1
