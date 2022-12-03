with open("input.txt") as f:
    data = f.read().split("\n")

lookup = "abcdefghijklmnopqrstuvwxyz"
lookup += lookup.upper()

values = []

for line in data:
    half = int(len(line)/2)
    c1 = line[:half]
    c2 = line[half:]
    print(c1, c2)

    duplicates = [x for x in c1 if x in c2]

    values.append(lookup.index(duplicates[0])+1)

print(str(values))
print(sum(values))

values = []

for index, line in enumerate(data):
    if index % 3 == 2:
        print("\n\n\n" + line)

        l1, l2 = data[index-1], data[index-2]

        print(l1, l2, line)
        both1 = [x for x in l1 if x in l2]
        print(both1)
        shared = [x for x in both1 if x in line]
        print(shared)

        values.append(lookup.index(shared[0])+1)

print(str(values))
print(sum(values))