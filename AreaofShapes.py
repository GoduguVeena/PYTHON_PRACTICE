def calculate_area(name): 
    name = name.lower()
    if name == "rectangle":
        l = int(input("Enter rectangle's length: "))
        b = int(input("Enter rectangle's breadth: ")) 
        # calculate area of rectangle
        rect_area = l * b
        print(f"The area of rectangle is {rect_area}.")
    elif name == "square":
        S = int(input("Enter square's side length: "))
        # calculate area of square
        sqt_area = S * S
        print(f"The area of square is {sqt_area}.") 
    elif name == "triangle":
        h = int(input("Enter triangle's height length: ")) 
        b = int(input("Enter triangle's base length: ")) 
        # calculate area of triangle
        tri_area = 0.5 * b * h
        print(f"The area of triangle is {tri_area}.")
    elif name == "circle":
        r = int(input("Enter circle's radius length: "))
        pi = 3.14
        # calculate area of circle
        circ_area = pi * r * r
        print(f"The area of circle is {circ_area}.")
    elif name == 'parallelogram':
        b = int(input("Enter parallelogram's base length: "))
        h = int(input("Enter parallelogram's height length: "))
        # calculate area of parallelogram
        para_area = b * h
        print(f"The area of parallelogram is {para_area}.")
    else:
        print("Sorry! This shape is not available.")

def main():
    print("Calculate Shape Area")
    shape_name = input("Enter the name of the shape whose area you want to find: ")
    calculate_area(shape_name)

if __name__ == "__main__":
    main()
