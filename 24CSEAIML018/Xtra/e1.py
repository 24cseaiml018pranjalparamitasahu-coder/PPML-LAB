num=int(input("Enter a 5 digit number:-"))
count=0
while(x!=0):
    if count%2!=0:
        print(x%10)
    x//=10
    count+=1