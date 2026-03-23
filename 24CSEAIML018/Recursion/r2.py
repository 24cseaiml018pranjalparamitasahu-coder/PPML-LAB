#fibonacci using recursion

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(6):
    print(fibonacci(i))


"""def print_fibo(n,a=0,b=1):
    if n==0:
        return
    print(a,end=" ")
    print_fibo(n-1,b,a+b)
print_fibo(6)"""