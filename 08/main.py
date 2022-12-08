with open("input.txt") as f:
    data = f.read().split("\n")

trees = []

width: int
height: int

for line in data:
    inted = [int(x) for x in line]
    print(inted)
    trees.append(inted)

width = len(trees[0])
height = len(trees)

print("Height: ", height)
print("Width: ", width)

def is_visible(x, y, trees):
    if x == 0 or y == 0 or x == width - 1 or y == height - 1:
        return True

    myHeight = trees[y][x]
    #print("My height at ", x, y, " is ", myHeight)

    vLeft = True
    vRight = True
    vUp = True
    vDown = True

    for dy in range(y+1, height):
        #print("Checking (down) ", x, dy, trees[dy][x], " for ", x, y)
        if trees[dy][x] >= myHeight:
            vDown = False

    for dy in reversed(range(0, y)):
        #print("Checking (left) ", x, dy, trees[dy][x], " for ", x, y)
        if trees[dy][x] >= myHeight:
            vUp = False

    for dx in range(x+1, width):
        #print("Checking (right)", dx, y, trees[y][dx], " for ", x, y)
        if trees[y][dx] >= myHeight:
            vRight = False

    for dx in reversed(range(0, x)):
        #print("Checking (left) ", dx, y, trees[y][dx], " for ", x, y)
        if trees[y][dx] >= myHeight:
            vLeft = False

    return vLeft or vRight or vUp or vDown

    return True

visibleCount = 0
for y in range(0, height):
    for x in range(0, width):
        if is_visible(x, y, trees):
            print("X", end="")
            visibleCount += 1
        else:
            print(" ", end="")
print("")
print(visibleCount)