with open("input.txt") as f:
    data = f.read().split("\n")

from dataclasses import dataclass


@dataclass
class Tower():
    index: int
    items: list


def parse_blocks(lines):
    bottomIndex = 0
    for line in lines:
        if line == "":
            bottomIndex = lines.index(line)

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
    for index, line in enumerate(crates):
        if index == len(crates) - 1:
            break

        for i, char in enumerate(line):
            if char == " ":
                continue

            if i in columnIndexes.keys():
                if columnIndexes[i] not in towers:
                    towers[columnIndexes[i]] = Tower(columnIndexes[i], [char])
                else:
                    towers[columnIndexes[i]].items.append(char)

    return towers, bottomIndex


crates, bottomIndex = parse_blocks(data)

for line in data[bottomIndex:]:
    if line == "":
        continue

    elements = line.split(" ")
    amount = int(elements[1])
    fromTower = int(elements[-3])
    toTower = int(elements[-1])

    crates[toTower].items = list(reversed(crates[fromTower].items[:amount])) + crates[toTower].items
    crates[fromTower].items = crates[fromTower].items[amount:]

print("".join([crates[i].items[0] for i in sorted(crates.keys())]))