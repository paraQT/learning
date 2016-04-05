def is_triangle(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        print("no")
    else:
        print("yes")

def triangle_input():
    a = int(input("enter var a: "))
    b = int(input("enter var b: "))
    c = int(input("enter var c: "))
    is_triangle(a, b, c)

triangle_input()
