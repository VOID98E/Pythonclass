num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
num3=float(input("Enter the third number: "))
           
while True:
    if num1 >= num2 and num1 >= num3:
        print(f"The largest number is: {num1}")
        break
    elif num2 >= num1 and num2 >= num3:
        print(f"The largest number is: {num2}")
        break
    else:
        print(f"The largest number is: {num3}")
        break