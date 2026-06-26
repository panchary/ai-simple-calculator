#simple calculator
x=int(input("Enter your 1st number:"))
y=int(input("Enter your 2st number:"))
user_enter=input("Enter operator (+,-,/,*,%,^,!):")
if user_enter=="+":
    sum=x+y
    print(sum)
elif user_enter=='*':
    multiply=x*y
    print(multiply)
elif user_enter=='-':
    if x>y:
        subtract=x-y
        print(subtract)
    else:
        subtract=y-x
        print(subtract)
elif user_enter=='/':
    if x>y:
        divide=x/y
        print(divide)
    else:
        divide=y/x
        print(divide)
elif user_enter=="%":
    if x>y:
        modulo=x%y
        print(modulo)
    else:
        modulo=y%x
        print(modulo)
elif user_enter == "^":
    if x > y:
        power = x ** y
        print(power)
    elif x < y:
        power = y ** x
        print(power)
    else:
        
        t = int(input("Enter subscript: ")) 
        power = x ** t
        print(power)
    
elif user_enter=="!":
    import math
    number = (x and y)
    
    if number >= 0:
        print(math.factorial(number))
    else:
        print("Factorial does not exist for negative numbers.")
else:
    print("write a valid opterator")