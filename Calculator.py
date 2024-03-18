#Getting numbers to be operated on
num1 = float(input("Write the first number: "))
num2 = float(input("Write the second number: "))
#Determining the operation
oprtr = input("To add the numbers press '+'\nTo subtract the numbers press '-'\nTo multiply the numbers press 'x'")
#committing the operation according to user's input
if oprtr == "+" :
    print("The sum of ",num1,"and",num2,"is",num1 + num2)

if oprtr == "-" :
    print("The difference of ",num1,"and",num2,"is",num1 - num2)

if oprtr == "x" :
    print("The product of ",num1,"and",num2,"is",num1 * num2)
