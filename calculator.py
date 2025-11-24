num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator = input("Enter operator(+,-,*,/): ")
if operator == '+':
    result = num1+num2
    print("result:",result)
elif operator == '-':
    result = num1-num2
    print("result:", result)
elif operator == '*':
    result = num1*num2
    print("result: ", result)
elif operator == '/':
    if num2==0:
        print("error")
    else:    
        result = num1/num2
        print("result:", result)
else:
    print("Invalid operator")        
