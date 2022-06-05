#Calculator using python simple code
num1 = float(input("Enter 1st number: "))
add = input(str("+, -, *, /, squre='^', for reminder='//' :"))
num2 = float(input("Enter 2nd number: "))
if add == "+":
    print(float(num1+num2))
elif add == "-":
    print(float(num1-num2))
elif add == "*":
    print(float(num1*num2))
elif add == "/":
    print(float(num1/num2))
elif add == "^":
    print(float(num1**num2))
elif add == "//":
    print(float(num1//num2))
else:
    print("Wrong input")
