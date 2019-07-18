num1 = float(input("Enter in your first number: "))
op = input("Enter your operator: ")
num2 = float(input("Enter in your second number: "))


result = None
if op == "+":
    result = (num1+num2)
    print(result)
elif op == "-":
    result = (num1 - num2)
    print(result)
elif op == "*":
    result =(num1 * num2)
    print(result)
elif op == "/":
    result = (num1 / num2)
    print(result)
else:
    print("Error")

if result != None:
    print('{}{}{} ={}' .format(num1, op, num2, result))
    # print("User input error. Please double check to makes sure that your operator is correct")
