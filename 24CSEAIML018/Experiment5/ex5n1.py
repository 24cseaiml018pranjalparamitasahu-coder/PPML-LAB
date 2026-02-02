a=0
b=1
sum_even=0

for i in range(1000):
    if a>1000:
        break
    print(a,end="")
    if a%2==0:
        sum_even += a
    c=a+b
    a=b
    b=c
    print("\nSum of even terms",sum_even)


