spam = ["apples", "bananas", "tofu", "cats"]
bacon = ["cat", "bat", "rat", "elephant"]

def comma_and(array):

    for x in range(len(array) - 1):
        print(array[x] + ", ", end = "")
        x += 1

        if x == len(array) - 1:
            print("and " + array[-1])

comma_and(spam)
comma_and(bacon)
