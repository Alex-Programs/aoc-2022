with open("input.txt") as f:
    data = f.read().split("\n")


count = 0
count2 = 0
for pair in data:
    first, second = pair.split(",")
    a = set(range(int(first.split("-")[0]), int(first.split("-")[1]) + 1))
    b = set(range(int(second.split("-")[0]), int(second.split("-")[1]) + 1))

    if a.issubset(b) or b.issubset(a):
        count += 1

    if len(a.intersection(b)) > 0:
        count2 += 1

print(str(count))
print(str(count2))