def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            print("fermat was  wrong")
        else:
            print("doesn't work")

def input_fermat():
    a = int(input("enter var a: "))
    b = int(input("enter var b: "))
    c = int(input("enter var c: "))
    n = int(input("enter var n: "))
    check_fermat(a, b, c, n)

input_fermat()
