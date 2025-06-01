mark1 = int(input("Enter marks 1: "))
mark2 = int(input("Enter marks 2: "))
mark3 = int(input("Enter marks 3: "))
total_percentage = ((mark1+mark2+mark3)*100)/300
print(total_percentage)
if(total_percentage>=40):
    print("passed")
else:
    print("failed")