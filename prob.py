def divisible5(n):
    if(n%5==0):
        return True
    return False
a = [1,2,3,3,333,5,66,77,99,100]
f = list(filter(divisible5,a))
print(f)