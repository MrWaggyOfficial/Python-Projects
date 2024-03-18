num1 = float(input("Write the first number: "))
num2 = float(input("Write the second number: "))

oprtr = input("To add the numbers press '+'\nTo subtract the numbers press '-'\nTo multiply the numbers press 'x'")

if oprtr == "+" :
    print("The sum of ",num1,"and",num2,"is",num1 + num2)

if oprtr == "-" :
    print("The difference of ",num1,"and",num2,"is",num1 - num2)

if oprtr == "x" :
    print("The product of ",num1,"and",num2,"is",num1 * num2)
