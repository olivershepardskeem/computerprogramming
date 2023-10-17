how_deep = int(input("how deep into the fibonacci would you like to go? "))

x = 0
y = 1
z = y
count = 1

while count <= how_deep:
    print(f"{z} ")
    count += 1
x, y = y, z
z = x + y