num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))


if (num1 > num2):
    if(num1 > num3):
        print("num1 is greatest")
    else:
        print("num3 is greatest")

elif (num2 > num3):
    print("num2 is greatest")

else:
    print("num3 is greatest")

    
