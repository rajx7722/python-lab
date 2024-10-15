import shapes

print("choose the shape whose area has to be calculated:")

choice = int(input("1 for circle, 2 for square , 3 for rectangle"))

if choice==1:
    radius=float(input("enter the radius"))
    area=shapes.area_circle(radius)
    print(f"area of circle = {area} ")

elif choice ==2:
    side=float(input("enter the length of the side of the square:"))
    area= shapes.area_square(side)
    print(f"area of square = {area} ")

elif choice==3:
    length= float(input("enter the lenght of the rectangle"))
    breadth=float(input("enter the breadth of the rectangle"))
    area = shapes.area_rectangle(length,breadth)
    print(f"area of rectangle ={area}")