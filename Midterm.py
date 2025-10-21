import math

# Q1: Calculate the area of a circle
def area_of_circle(radius) :
    area = (math.pi) * (radius ** 2)

    return round(area, 2)


# Q2: Hollow Right Triangle
def hollow_right_triangle(n) :
    result = ""
    if n < 4 :
        result = "The triangle height should be at least 4."
    else:
        for i in range(n) :
            if i == 0 :
                result += "*" + "\n"
            elif i == n - 1 :
                result += "*" * n
            else :
                result += "*" + " " * (i - 1) + "*" + "\n"

    return result


# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""
    if n < 3 :
        return "The pyramid height should be at least 3."
    else:
        for i in range(n) :
            for k in range(i):
                result += " "
            for j in range( 2 * n - 1 - 2 * i) :
                result += "*"
            result += "\n"

        return result.rstrip()
    


    





# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(2))
print()

print(inverted_pyramid(5))
print()