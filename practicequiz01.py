#WAP to check if a number entered by the user is even or odd.

num = int(input("enter number"))

rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")

#WAP to find the gretest of three numbers entered by the user.

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a >= b and a >=c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third is largest")

    
#WAP to check if a number is a multiple of 7 or not.

num = int(input("enter number"))

if(num%7 == 0):
    print("multiple of 7")
else:
    print("is not a multiple of 7")
