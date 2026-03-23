#WAP TO CREATE A FUNCTION THAT TAKES LIST AS ARGUMENT AND RETURNS THE EVEN VALUES OF THE LIST.PRINT THE NEW LIST WITH EVEN VALUES
def even_len(n):
    s=[]
    for int(i) in n:
        if i%2==0:
            s.append(i)
    return s
x=input("Enter the list of elements:")
n=(i for i in x.split(","))
s=even_len(n)
print(s)
    