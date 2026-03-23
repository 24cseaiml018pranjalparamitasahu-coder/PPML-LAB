#reverse a string using recursion
def rev_str(s):
    
    if len(s)==0:
        return s
    else:
        return rev_str(s[1:])+s[0]
        
print(rev_str("Pranjal"))