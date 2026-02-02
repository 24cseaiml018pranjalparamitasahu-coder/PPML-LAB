a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter third number"))
while(b!=0):
    temp=a
    a=b
    b=temp%b
while(c!=0):
    temp=a
    a=c
    c=temp%c
    print("GCD is",a)
