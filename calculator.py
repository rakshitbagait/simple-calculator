#_simple calculator
import math
print("--CALCULATOR--")
 
def sum(a,b):
    a +=b
    return a
def sub(a,b):
    if a>b:
        a-=b
        return a
    else:
        b-=a
        return b
def mul(a,b):
    a *=b
    return a
def div (a,b):
    q= a/b
    r =a%b
    print("the quotient is",q)
    print("the remainder is:",r)

def sqr(a):
    x = math.sqrt(a)
    return x
while(True):
    print("Choose the opreation you want to perform ")
    print("1 FOR ADDITION")
    print("2 FOR SUBTRACTION")
    print("3 FOR MULTIPLICATION")
    print("4 FOR DIVISION")
    print("5 FOR SQUARE ROOT")
    print("6 FOR EXIT")
    
    choice = int(input("enter you choice"))
    
    if choice== 1:
        num1 = int(input("enter the number 1"))
        num2 = int(input("enter the number 2"))
        s = sum(num1,num2)
        print("the sum is ",s)
    
    elif choice==2 :
        num1 = int(input("enter the number 1"))
        num2 = int(input("enter the number 2"))
        m = sub(num1,num2)
        print("the answer is ", m)
    
    elif choice ==3:
        num1 = int(input("enter the number 1"))
        num2 = int(input("enter the number 2"))
        p = mul(num1,num2)
        print("the answer is ",p)
    elif choice==4:
        num1 = int(input("enter the number 1"))
        num2 = int(input("enter the number 2"))
        div(num1,num2)

    elif choice == 5:
        num =int(input("enter the number"))
        r = sqr(num)
        print(r)

    else:
        print("you chose to exit")
        break
