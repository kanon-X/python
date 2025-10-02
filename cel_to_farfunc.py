def f_to_C(f):
    return 5*(f-32)/9

f=int(input("Enter temperature in fahrenheit: "))
C =f_to_C(f)
print(f"{round(C,2)}°C")