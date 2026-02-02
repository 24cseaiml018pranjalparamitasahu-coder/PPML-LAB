"""x=int(input("Enter a number between 0 to 6 "))
if(x==0):
    print("Sunday")
elif(x==1):
    print("Monday")
elif(x==2):
    print("Tuesday")
elif(x==3):
    print("Wednesday")
elif(x==4):
    print("Thursday")
elif(x==5):
    print("Friday")
elif(x==6):
    print("Saturday")
else:
    print("Wrong input!!")"""
n=int(input("Enter a day number from 0 to 6:-"))
l=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print("It is",l[n])