num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operation(+, -, *, /): ")

if operator == "+" :
    print("Answer =", num1 + num2)

elif operator == "-" :
    print("Answer =", num1 - num2)

elif operator == "*" :
    print("Answer =", num1 * num2)

elif operator == "/" :
    if b == 0:
        print("Divisible by zero is not possible")
    else:
        print("Answer =", num1 / num2)
else:
    print("Wrong operation entered")