def check(a):
    return "Even" if a%2==0 else "odd"
n=int(input("Enter a number"))
print(n,"is",check(n))