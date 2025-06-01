a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
c = int(input("enter 3rd number:")) 
d = int(input("enter 4th number:"))

if(a>b and a>c and a>d):
    print("The greatest number is: ", a)

if(b>a and b>c and b>d):
     print("The greatest number is: ", b)
elif(c>a and c>b and c>d):
    print("The greatest number is: ", c)
else:
     print("The greatest number is: ", d)
