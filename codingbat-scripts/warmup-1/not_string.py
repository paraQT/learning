def not_string(str):
    if str[0:3] == 'not':
        return str
    elif str[0:3] != 'not':
        return 'not ' + str

print(not_string('not candy'))
print(not_string('x'))
print(not_string('not bad'))
