n=int(input("Enter a num:"))
x=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
print("Perfect number")if n==sum else print("NOt perfect")