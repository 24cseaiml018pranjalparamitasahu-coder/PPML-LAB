n=int(input("Enter a number:-"))
original=n
reverse=0
while (n>0):
    digit=n%10
    reverse=reverse*10+digit
    n//10
if original==reverse:
    print(f"{n} is a palindrome" )
else:
    print("Not palindrome")