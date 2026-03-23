def count_digit(n):
    if n==0:
        return 0
    else:
        return 1+count_digit(n//10)
num=int(input("Enter a number"))
print(count_digit(num))