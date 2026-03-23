x=input("Enter a word:")
for y in x:
    if y in "aeiouAEIOU":
        print(f"{y} is vowel")
    else:
        print(f"{y} is consonant")