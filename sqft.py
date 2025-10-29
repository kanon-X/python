print("please enter the dimention of the sqft")
def calculate_area(w,h):
    area_sqft = w*h
    print(f"The total sqft is: {area_sqft}")
width = int(input("Enter the width of the room : "))
height = int(input("Enter the height of the room : "))
calculate_area(width,height)
