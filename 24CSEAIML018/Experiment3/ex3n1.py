String=input("Enter a string")
reversed_string=String[::-1]
if(String==reversed_string):
    print("The", String," is a palindrome")
else:
    print("Not Palindrome")