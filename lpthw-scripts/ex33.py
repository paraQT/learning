# i = 0
# numbers = []
#
# while i < 600000000:
#     print("At the top i is %d" % i)
#     numbers.append(i)
#
#     i += 1
#     print("Numbers now: ", numbers)
#     print("At the bottom i is %d" % i)
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)

def counter(start_at, stop_at, step):
    while start_at < stop_at:
        print(start_at)
        start_at = start_at + step

input_start = int(input("What number should I start from? "))
input_stop = int(input("What number should I count to? ")) + 1
input_step = int(input("How much should the counter increment each time? "))

counter(input_start, input_stop, input_step)
