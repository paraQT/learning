# this isn't working

def pos_neg(a, b, negative):
    if negative == True:
            if a < 0 and b < 0:
                return True
            else:
                return False
    else:
        if a >= 0 or b >= 0:
            return False
        elif a < 0 or b < 0:
            return False
        elif (a < 0 and b > 0) or (a > 0 and b < 0):
            return True
        else:
            return True

print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
