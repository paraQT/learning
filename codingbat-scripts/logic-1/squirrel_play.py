def squirrel_play(temp, is_summer):
    if temp >= 60 and temp <= 90:
        return True
    elif temp >= 60 and temp <= 100 and is_summer == True:
        return True
    else:
        return False
