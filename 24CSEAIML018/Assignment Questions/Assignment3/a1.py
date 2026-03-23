#WAP to print twin prime numbers between 1 to N
N=int(input("Enter a number"))
for i in range(2,N):
    d=0
    for j in range(1,i+1):
        if i%j==0:
            d=d+1
    if d==2:
        d=0
        N=i+2
        for j in range(1,N+1):
            if N%j==0:
                d=d+1
        if d==2:
            print("(%d,%d)"%(i,N))