#write a program to input any number and check whether it is prime or not.

num = int(input("enter any number:"))
lim = int(num/2)+1

for i in (range(2,lim)):
    if num%i == 0:

        print(num, "is not prime")
        break
    else:
        print(num, "is prime")