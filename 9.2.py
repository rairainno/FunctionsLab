def rectangle(b,h):
    for i in range(b):
        for b in range(h):
            print("*", end = "")
        print()

base = int(input("Enter the base length:"))
height = int(input("Enter the height length:"))

rectangle(base, height)

