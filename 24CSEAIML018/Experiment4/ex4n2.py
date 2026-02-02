num=int(input("Enter a number"))
number=1
while(number<num):
    if(number%num==0):
        break
    number+=1
if(number==2):
    print("Prime")
else:
    print("Not Prime")