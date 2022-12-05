with open("input.txt") as f:
    data = f.read().split("\n")


def parse_blocks(lines):
    bottomIndex = [i for i, x in enumerate(lines) if x == ""][0]

    crates = lines[:bottomIndex]

    columnIndexes = {}

    for index, char in enumerate(crates[-1]):
        if char == " ":
            continue

        try:
            columnIndexes[index] = int(char)
        except:
            continue

    towers = {}
    for index, line in enumerate(crates[:-1]):
        for i, value in columnIndexes.items():
            if len(line) <= i or line[i] == " ":
                continue

            if value not in towers:
                towers[value] = [line[i]]
            else:
                towers[value].append(line[i])

    return towers, bottomIndex


crates, bottomIndex = parse_blocks(data)

for line in data[bottomIndex:]:
    if line == "":
        continue

    move, amount, _from, fromTower, to, toTower = line.split(" ")
    amount, fromTower, toTower = int(amount), int(fromTower), int(toTower)

    crates[toTower] = crates[fromTower][:amount] + crates[toTower]
    crates[fromTower] = crates[fromTower][amount:]

print("".join([crates[i][0] for i in sorted(crates.keys())]))
