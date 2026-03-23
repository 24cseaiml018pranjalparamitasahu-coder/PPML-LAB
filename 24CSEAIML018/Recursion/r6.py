#power of a number using recursion
def pow(x,y):
    if y==1:
        return x
    return x*pow(x,y-1)
print(pow(2,3))
