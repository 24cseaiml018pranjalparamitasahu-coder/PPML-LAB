para=input("Enter a paragraph:-")
words=para.split()
print("Word count:",len(words))
pal_count=0
for w in words:
    if w==w[::-1]:
        pal_count+=1
print("Palindrome count:",pal_count)
for w in words:
    print(w[::-1])
