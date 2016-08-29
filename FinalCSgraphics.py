
# Equilateral triangle

window = turtle.screen()
    for i in [0,1,2]:
        turtle.forward(side)
        turtle.left(30)
    window.exitonclick()

# right triangle


window = turtle.screen()
    for i in [0,1,2]:
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side2)
        turtle.left(45)
        turtle.forward(hypotenuse)
        turtle.left(45)
    window.exitonclick()

# iscosceles triangle
window = turtle.screen()
    for i in [0,1,2]: 
        turtle.forward(base)
        turtle.left(70)
        turtle.forward(hypotenuse)
        turtle.left(40)
        turtle.forward(side)
        turtle.left(70)
    window.exitonclick()
# scalene triangle

window = turtle.Screen()
    turtle.forward(base)

elif userChoice == 4:
    userChoice == "rectangle"
    
def calculations(rectangle)
    if rectangle == "perimeter" or square == "area":
        if rectangle == "perimeter":
            side = float(input("Please enter the side length of your rectangle:"))
            width = float(input("Please enter the width of your rectangle:"))
            perimeter = round(2*(side + width),2)
            print("The perimeter of your rectangle is",perimeter)


        elif rectangle == "area":
            side = float(input("Please enter the side length of your rectangle:"))
            width = float(input("Please enter the width of your rectangle:"))
            area = round(side * width,2)
            print("The area of your rectangle is",area)
