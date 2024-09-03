def calculator():
    print("calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    
    c=int(input("Enter your choice: "))
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    
    if c==1:
        print(num1,"+",num2,"=",num1+num2)
        
    elif c==2:
        print(num1,"-",num2,"=",num1-num2)
    elif c==3:
        print(num1,"*",num2,"=",num1*num2)
    elif c==4:
        print(num1,"/",num2,"=",num1/num2)
    else:
        print("Invalid choice")
        
calculator()
