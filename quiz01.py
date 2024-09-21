#write a program to input three numbers and calculate sum. if the numbers are  diffrent, then add them. 
#  if any of two given input numbers are same, then print the third number.

a = int(input("enter the first number:"))
b = int(input("enter the second numbern:"))
c = int(input("enter the third nunber:"))

sum = a+b+c

if(a==b):
    print("sum=", c)
elif(b==c):
    print("sum=", a)
elif(a==c):
    print("sum=", b)
else:
    print("sum=",(a+b+c))


