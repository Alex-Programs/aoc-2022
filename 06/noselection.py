with open("input-prod.txt") as f:
    data = f.read().split("\n")

data = data[0]

index = 0

def has_duplicates(l):
    duplicateCount = 0
    for i in l:
        for j in l:
            duplicateCount += (i == j)

    return duplicateCount > len(l)


for i, char in enumerate(data):
    isNotDuplicate = not has_duplicates(data[i - 14:i])  # int(len(set(data[i - 14:i])) == len(data[i - 14:i]))
    isIndexZero = int(index == 0)
    greaterThan14 = int(i > 14)

    index = index + ((isNotDuplicate * i) * isIndexZero * greaterThan14)

print(index, data[index])
