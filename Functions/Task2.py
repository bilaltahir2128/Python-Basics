shape=input("Enter the shape type triangle or rectangle :")
dimension1=int(input(f"Enter the first dimension of {shape}: "))
dimension2=int(input(f"Enter the second dimension of {shape} : "))

def Area(dimension1,dimension2,shape):
    if shape=="triangle":
        Area_of_shape=1/2*dimension1*dimension2
    elif shape=="rectangle":
        Area_of_shape=dimension1*dimension2
    else:
        Area_of_shape=1/2*dimension1*dimension2

    return print(f"The Area of shape is : {Area_of_shape}")
Area(dimension1,dimension2,shape)