num=int(input("Enter a number"))
sum=0
while(num>0):
    r=num%10
    sum+=r
    num //=10

print("Sum of digits=",sum)