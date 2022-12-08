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


def scenic(x, y, trees):
    myHeight = trees[y][x]
    # print("My height at ", x, y, " is ", myHeight)

    vLeft = 0
    vRight = 0
    vUp = 0
    vDown = 0

    for dy in range(y+1, height):
        if trees[dy][x] >= myHeight:
            vDown += 1
            break
        else:
            vDown += 1

    for dy in reversed(range(0, y)):
        if trees[dy][x] >= myHeight:
            vUp += 1
            break
        else:
            vUp += 1

    for dx in range(x+1, width):
        if trees[y][dx] >= myHeight:
            vRight += 1
            break
        else:
            vRight += 1

    for dx in reversed(range(0, x)):
        if trees[y][dx] >= myHeight:
            vLeft += 1
            break
        else:
            vLeft += 1

    return vLeft * vRight * vUp * vDown


visibleCount = 0
highest = 0
for y in range(0, height):
    for x in range(0, width):
        score = scenic(x, y, trees)
        if score > highest:
            highest = score

        print(highest)
