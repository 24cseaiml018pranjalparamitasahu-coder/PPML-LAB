#palindrome of string
def palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return palindrome(s[1:-1])
word=input("Enter word:")
if palindrome(word):
    print("Palindrome")
else:
    print("NOt palindrome")