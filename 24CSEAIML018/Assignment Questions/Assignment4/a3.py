#wap to create an integer list of 20 elements increase the odd valued elements by 5
s=[]
x=int(input("Enter the no of elements:"))
for i in range(x):
    n=int(input("Enter the element: "))
    s.append(n)
for i in range(x):
    if s[i]%2!=0:
        s[i]=s[i]+5
print(s)