# Miguel Lucas & Eduardo Rocha
# Final Project CS1

import turtle
import math
from math import pi, sqrt
from turtle import *

# Program asking the user for data of a shape ( circle, triangle, square, or rectangle) and finding calculations
# for it depending on the data given. The Shape Calculator will then draw the shape using turtle graphics.



# WELCOME TO THE SHAPE CALCULATOR INTRO
# function receives an input and validates it
# @param none the function serves to validate
# @return validation for input or exits program
#

def get_input_number():
    print("Welcome to the Shape Drawing Calculator! ")
    print("Available shapes to calculate: 1)Circle 2)Triangle 3)Square 4)Rectangle! ")
    print("Which would you like to calculate and draw today? 1 , 2, 3 or 4? Enter 0 to quit.")
    global num
    num = int(input(" "))
    if num == 0:
        print("Thank you for using the Shape Calculator! Have a great day!")
        return exit()
    elif num < 0 or num > 4:
        print("Invalid input.  Try again ")
        return get_input_number() # Returns beginning statement if not 1,2,3 or 4

    else:
        return num #returns valid number within range

## Main function is where we implement our other functions and get calculations
# @param none
# @return the shapes calculations and drawings
#

def main():


    x = get_input_number()
    userChoice = num
    if userChoice == 1:
        userChoice = "circle"
        print("What would you like to calculate about the circle?")
        print("1)radius 2)circumference 3)diameter 4)area")
        userData = int(input(" "))

        if userData == 1: userData = "radius"
        elif userData == 2: userData = "circumference"
        elif userData == 3: userData = "diameter"
        elif userData == 4: userData = "area"

        a = calculations(userData) # Calculates Circle


    elif userChoice == 2:
        userChoice = "triangle"
        print("Which type of triangle would you like to find?")
        print("1)Equilateral 2)Right 3)Isosceles")
        userTriangle = int(input(" "))

        b = calculations2(userTriangle) # Calculates Triangle

    elif userChoice == 3:
        userChoice = "square"
        print("What would you like to calculate about the Square?")
        print("1)Perimeter 2)Area")
        userData3 = int(input(" "))
        if userData3 == 1: userData3 = "perimeter"
        elif userData3 == 2: userData3 = "area"


        c = calculations3(userData3) # Calculates Square

    elif userChoice == 4:
        userChoice = "rectangle"
        print("What would you like to calculate about the Rectangle")
        print("1)Perimeter 2)Area")
        userData4 = int(input(" "))
        if userData4 == 1: userData4 ="perimeter"
        elif userData4 == 2: userData4 = "area"

        d = calculations4(userData4) # Calculates rectangle





## Function calculates a circle's circumference,area, diameter, radius
# @param circle input from main()
# @return the calculation and respective drawing
#

def calculations(circle):


    list = ["circumference","area","diameter","radius"] # Error message if input not valid using list
    if circle not in list:
        print("Invalid input! Please try again!")
        return main() # returns back to the beginning

# -- Circumference = 2 * pi * r
    if circle == "circumference":
        r = float(input("Please enter the radius of the circle: "))
        diameter = (2 * r)
        circum = round(pi * diameter, 2)
        print("The circumference of your circle is",circum)

# -- Area = pi * r**2
    elif circle == "area":
        r = float(input("Please enter the radius of the circle: "))
        s = r**2
        area = round(pi * s, 2)
        print("The area of your circle is",area)

# -- Diameter = r * 2
    elif circle == "diameter":
        r = float(input("Please enter the radius of the circle: "))
        diameter = round( r * 2, 2)
        print("The diameter of your circle is",diameter)

# -- Radius = r
    elif circle == "radius":
        r = float(input("Please enter the radius of your circle: "))
        radius = round(r,2)
        print("The radius of your circle is",radius)



# brings in the canvas
    window = turtle.Screen()

# assigns color to circle
    turtle.color("black", "red")
# draws the circle
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


# labels the circumference
    if circle == "circumference":
        turtle.write( "Circumference is %d " %  circum , font=("Arial", 16, "normal") )
    elif circle == "radius":
        # labels the radius
        turtle.write( "Radius is %d " % r , font=("Arial", 16, "normal") )
    elif circle == "area":
        # labels the area
        turtle.write( "Area is %d " % area , font=("Arial", 16, "normal") )
        # labels the diameter
    elif circle == "diameter":
        turtle.write( "Diameter is %d " % diameter , font=("Arial", 16, "normal"))

# assigns color to background
    window.bgcolor("green")

    turtle.getscreen()._root.mainloop()



## Function asks for right, equlateral or iscosceles and calculates a triangle's area or perimeter
# @param triangle from main()
# @return the required calculation and respective turtle drawing
#

def calculations2(triangle):

    list = [1,2,3] # Error message if input not valid using list
    if triangle not in list:
        print("Invalid input! Please try again!")
        return main() # returns back to the beginning


    if triangle == 1: #Option one is equilateral triangle
        triangle = "equilateral"
        print("What would you like to find? 1) Area or 2) Perimeter")
        areaOrPerim = int(input(" "))
        if areaOrPerim == 1:
            side = float(input("Please enter a height of your triangle: "))
            area = round((sqrt(3) / 4) * (side**2),2)
            print("The Area of your triangle is",area)
        elif areaOrPerim == 2:
            side = float(input("Please enter a side of your triangle: "))
            perimeter = round(side * 3,2)
            print("The Perimeter of your triangle is",perimeter)


# brings in the canvas, color,and draws triangle
        window = turtle.Screen()
        turtle.color("black","yellow")
        turtle.begin_fill()

        for i in [0,1,2]:

            turtle.forward(side)
            turtle.left(120)
        window.bgcolor("green")
        if areaOrPerim == 1:
            turtle.write( "Area is %d " %  area, font=("Arial", 16, "normal") )
        elif areaOrPerim ==2:
            turtle.write( "Perimeter is %d " %  perimeter , font=("Arial", 16, "normal") )
        turtle.end_fill()
        window.exitonclick()



    elif triangle == 2: #Option two is the right triangle
        triangle = "right"
        print("What would you like to find? 1) Area or 2) Perimeter")
        areaOrPerim = int(input(" "))
        if areaOrPerim == 1:
            side = float(input("Please enter the height of your triangle: "))
            hypotenuse = (sqrt(side**2 + side**2))
            area = float((side * side) // 2)
            print("The Area of your triangle is",area)
        elif areaOrPerim == 2:
            side = float(input("Please enter a side of your triangle: "))
            hypotenuse = float((sqrt(side**2 + side**2)))
            perimeter = (side + side)+(sqrt(side**2 + side**2))
            print("The Perimeter of your triangle is",perimeter)
# brings in the canvas, color,and draws triangle
        window = turtle.Screen()
        turtle.color("black","yellow")
        turtle.begin_fill()
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(135)
        turtle.forward(hypotenuse)
        turtle.left(45)

        window.bgcolor("green")

        if areaOrPerim == 1:
            turtle.write( "Area is %d " %  area, font=("Arial", 16, "normal") )
        elif areaOrPerim ==2:
            turtle.write( "Perimeter is %d " %  perimeter , font=("Arial", 16, "normal") )
        turtle.end_fill()

        window.exitonclick()



    elif triangle == 3: #Option three is the isosceles triangle
        triangle = "isosceles"
        print("What would you like to find? 1) Area or 2) Perimeter")
        areaOrPerim = int(input(" "))
        if areaOrPerim == 1:
            side = float(input("Please enter a side length of your triangle: "))
            base = float(input("Please enter the base of your triangle: "))
            area = (side * base) // 2
            print("The Area of your triangle is",area)

        elif areaOrPerim == 2:
            side = float(input("Please enter a side of your triangle: "))
            base = float(input("Please enter the base of your triangle: "))
            perimeter = (2*side) + base
            print("The Perimeter of your triangle is",perimeter)

# brings in the canvas, color,and draws triangle
        window = turtle.Screen()
        turtle.color("black","yellow")
        turtle.begin_fill()
        for i in [0,1,2]:

            turtle.forward(side)
            turtle.left(120)

        if areaOrPerim == 1:
            turtle.write( "Area is %d " %  area, font=("Arial", 16, "normal") )
        elif areaOrPerim ==2:
            turtle.write( "Perimeter is %d " %  perimeter , font=("Arial", 16, "normal") )
        turtle.end_fill()
        window.bgcolor("green")
        window.exitonclick()





## Function calculates a square's area or perimeter
# @param square input from main()
# @return the desired calculation
#

def calculations3(square):

    list = ["perimeter","area"] # Error message if input not valid using list
    if square not in list:
        print("Invalid input! Please try again!")
        return main() # returns back to the beginning

# -- Perimeter = 4 times side
    if square == "perimeter":
        side = float(input("Please enter the side length of your square:"))
        perimeter = round(4*side,2)
        print("The perimeter of your square is",perimeter)

# -- Area = side squared
    elif square == "area":
        side = float(input("Please enter the side length of your square:"))
        area = round(side**2,2)
        print("The area of your square is",area)

# brings in the canvas, color,and draws triangle
    window = turtle.Screen()
    turtle.color("black", "red")
    turtle.begin_fill()
    window.bgcolor("yellow")

    turtle.forward(side)

    for i in [0,1,2,3]:
        turtle.left(90)
        turtle.forward(side)
    if square == "perimeter":
        turtle.write( "Perimeter is %d " %  perimeter , font=("Arial", 16, "normal") )
    elif square == "area":
# labels the radius
        turtle.write( "Area is %d " % area , font=("Arial", 16, "normal") )
    turtle.end_fill()
    turtle.exitonclick()

## Function calculates and draws the rectangle
# @param rectangle choice from main function
# @return the required calculation and respective turtle graphics drawing
#

def calculations4(rectangle):

    list = ["perimeter","area"] # Error message if input not valid using list
    if rectangle not in list:
        print("Invalid input! Please try again!")
        return main() # returns back to the beginning


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

# brings in the canvas, color,and draws triangle

    window = turtle.Screen()
    turtle.color("black", "red")
    turtle.begin_fill()
    window.bgcolor("yellow")

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    if rectangle == "perimeter":
        turtle.write("Perimeter is %d " %  perimeter , font=("Arial", 16, "normal"))
    elif rectangle == "area":
        turtle.write("Area is %d " % area , font=("Arial", 16, "normal"))

    turtle.end_fill()
    turtle.exitonclick()



main() #Calling back to the main function
