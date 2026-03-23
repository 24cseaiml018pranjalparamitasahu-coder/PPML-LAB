#find minimum element in a list
def rec_min(L):
    if len(L)==1:
        return L[0]
    else:
        m=rec_min(L[1:])
        return L[0]