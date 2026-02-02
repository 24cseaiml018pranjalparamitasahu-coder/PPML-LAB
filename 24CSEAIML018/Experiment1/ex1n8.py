a=int(input("Enter length of side 1:"))
b=int(input("Enter length of side 2:"))
c=int(input("Enter length of side 3:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.53
perimeter=a+b+c
print ("area is",area)
print("perimeter is",perimeter)
print("semiperimeter is",s)