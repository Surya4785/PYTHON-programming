#logical operators 

#not operator
print(not False)
print(not True)

a=50
b=30
print(not(a>b))
print(not(a<b))

#and operator
val1=True
val2=False
print("and operator:",val1 and val2)

a=10
b=20
print("and operator:",(a<b) and (a==b))

val1=True
val2=True
print("and operator:",val1 and val2)

a=10
b=20
print("and operator:",(a<b) and (a<=b))

#or operator
val1=True
val2=False
print("or operator:",val1 or val2) 

a=100
b=200
print("or operator:",(a<b) or (a>b))

val1=False
val2=False
print("or operator:",val1 or val2)

a=100
b=200
print("or operator:",(a==b) or (a>b))



