n=int(input("Enter a number"))
original=n
n//=10
while(n>0):
    digit=n%10
    reverse=reverse*10+digit
    n//=10
if(original==reverse):
    print("Palindrome")
else:
    print("NOt palindrome")