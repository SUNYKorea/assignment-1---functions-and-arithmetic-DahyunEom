# Name:Dahyun Eom
# SBUID:115943034

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit):
    return 5/9*(fahrenheit-32)
fahrenheit = int(input("Type the temperature in fahrenheit:"))
print (fahrenheit2celsius(fahrenheit))

def what_to_wear(celsius):
    if (celsius < -10):
        print("wear puffy jacket")
        
    elif(-10 <= celsius < 0):
        print("wear scarf")
    
    elif (0 <= celsius < 10):
        print("wear sweater")
        
    elif (10 <= celsius < 20):
        print("wear light jacket")
        
    elif (20 <= celsius ):
        print("wear t-shrit")

celsius = int(input("type celsius:"))
what_to_wear(celsius)


# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    return (( x1*y2 + x2*y3 + x3*y1 ) - (x1*y3 + x2*y1 +x3*y2)) / 2

x1, x2, x3, y1, y2, y3 = int(input("type:"))      #절댓값, 왜 int/str안 될까


def euclidean_distance(x1, y1, x2, y2):
    return 

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    ...


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    ...

def apothem(number_sides, length_side):
   ...

def polygon_area(number_sides, length_side):
   ...


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
# 주어진 값을 사용하는건지, 사용자에게서 값을 받는 것인지 확실하지 않아서 두번쨰 케이스는 주석으로 달아둡니다. 
#
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

