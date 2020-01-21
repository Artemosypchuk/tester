from calc import *


first_numb = int(input("Enter first numb: "))  # FIRST argument in calc
seccond_numb = int(input("Enter seccond numb: "))  # SECOND argument in calc
operation = input("Enter operator + , - , * , / . :")  # OPERATOR BY USER INPUT

if operation == '+':
    result = (plus(first_numb, seccond_numb))
    print("Your result: ", first_numb, operation, seccond_numb, "=", result)
elif operation == '-':
    result = (minus(first_numb, seccond_numb))
    print("Your result: ", first_numb, operation, seccond_numb, "=", result)
elif operation == '*':
    result = (multiply(first_numb, seccond_numb))
    print("Your result: ", first_numb, operation, seccond_numb, "=", result)
elif operation == '/':
    result = (slicer(first_numb, seccond_numb))
    print("Your result: ", first_numb, operation, seccond_numb, "=", result)
