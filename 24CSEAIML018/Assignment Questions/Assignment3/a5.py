#WAP to print even length words in a string
x=input("Enter a string:")
y=""
for c in x:
    if c!="":
        y=y+c
    else:
        if len(y)%2==0:
            print(y)
        y=""
    if len(y)%2==0:
        print(y)