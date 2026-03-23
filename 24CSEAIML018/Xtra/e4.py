st=input("Enter a string:-")
rev=''.join(reversed(st))
print(rev)
count=0
for i in str:
    if i in ['a','e','i','o','u','A','B','C','D','E','O','U']:
        count+=1
print("Number of vowels:",count)
print("Number of consonants",len(str)-count)