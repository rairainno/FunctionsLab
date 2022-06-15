x = input("First Value:")
y = input("Second Value:")
z = input("Third Value:")
def min3(x, y, z):
    if(x<=y) and (x<=z):
        least = x
    elif (y<=x) and (y<=z):
        small = y
    else:
        small = z
    return small

print(min(x, y, z))

