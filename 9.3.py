def find(my_list, key):
    position = 0
    for i in my_list:
        if i == key:
            print("found", i, "position", position)
        position = position + 1

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)