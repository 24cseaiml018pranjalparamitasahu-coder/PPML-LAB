#WAP to remove all duplicates fromn a given string
x=input("Enter a string:")
result=""
for char in x:
    if char not in result:
        result=result+char
print(result)