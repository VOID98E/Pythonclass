

print("______________Calculator________________")

print("welcoome to the calculator\n" 
"additon,\n" \
"subtraction,\n" \
"multiplication,\n" \
"division\n"
"reminder\n"
"odd or even number\n"
"power\n"
"square\n"
"square root\n"
)

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. reminder")
print("6. odd or even number")
print("7. power")
print("8. square ") 
print("9.square root")
print("10. exit")

print("Please choose an number from 1 to 10:")

while True:

 a=int(input("Enter number: "))

 if a<1 or a>10:
      print("Invalid choice,choose a number from 1 to 10.")
      continue
    
 if a==1:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    result=num1+num2
    print(f"The sum of {num1} and {num2} is: {result}")

 elif a==2:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    result=num1-num2
    print(f"The subtration of {num1} and {num2} is: {result}")

 elif a==3:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    result=num1*num2
    print(f"The product of {num1} and {num2} is: {result}")

 elif a==4:
    num1=float(input("Enter second number: "))
    num2=float(input("Enter second number: "))
    result=num1/num2
    print(f"The quotient of {num1} and {num2} is: {result}")
 elif a==5:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    result=num1/num2
    print(f"The quotient of {num1} and {num2} is: {result}")
 elif a==5:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    result=num1%num2
    print(f"The remainder of {num1} and {num2} is: {result}")

 elif a==6:
    num1=int(input("Enter a number: "))
    if num1%2==0:
        print(f"{num1} is an even number")
    else:
        print(f"{num1} is an odd number")
 elif a==7:
    num1=float(input("Enter a number: "))
    num2=float(input("Enter the power: "))
    result=num1**num2
    print(f"{num1} to the power of {num2} is: {result}")

 elif a==8:
      num1=float(input("Enter a number: "))
      result=num1**2
      print(f"The square of {num1} is: {result}")
 elif a==9:
    num1=float(input("Enter a number: "))
    result=num1**0.5
    print(f"The square root of {num1} is: {result}")
 elif a==10:
    print("Thank u for usin the calculator.")
    break