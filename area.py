ch='y'
import math 
while(ch!='n'):
    n=int(input("1. for triangle\n 2. for rectangle\n 3. for square\n 4. for circle "))
    if(n==1):
        a=int(input("enter the first side "))
        b=int(input("enter the second side "))
        c=int(input("enter the third side "))
        p=(a+b+c)/2
        r=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("area of triangle is ",r)
    if(n==2):
        a=int(input("enter the width "))
        b=int(input("enter the height "))
        r=a*b
        print("area of rectangle is ", r)
    if(n==3):
        a=int(input("enter the side "))
        r=a**2
        print("area of square is ", r)
    if(n==4):
        a=int(input("enter the radious of circle "))
        r=math.pi*a**2
        print("area of circle is ", r)
    ch=input("Enter your choice 'y' or 'n' ")
