p=float(input("Enter the principal amount"))
t=float(input("Enter the time period in years:"))
r=float(input("Enter the rate of interest"))
n=float(input("Enter the number of times interest is compounded per year:- "))
si=(p*t*r)/100
print("simple interest is",+si)
a=p*(1+(r/n))**(n*t)
ci=a-p
print("compound interest is",+ci)