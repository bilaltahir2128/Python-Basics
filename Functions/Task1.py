height=int(input("Enter the heigt of triangle: "))
base=int(input("Enter the base of triangle: "))
def Area(height,base):
    Area_of_triangle=1/2*base*height
    return print(f"The Area of triangle is : {Area_of_triangle}")
Area(height,base)