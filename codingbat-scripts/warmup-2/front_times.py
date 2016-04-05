def front_times(str, n):
    front = str[0:3]
    result = ''
    for i in range(n):
        result = result + front
    return result
