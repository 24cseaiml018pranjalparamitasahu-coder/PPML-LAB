#WAP TO CALCULATE FACTORIAL OF A NUMBER USIONG RECURSION
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
n=int(input("Enter the number:"))
if (n<0):
    print("It is negative number")
else:
    print("Factorial of",n,"is:",factorial(n))