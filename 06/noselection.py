# Doesn't work
# Need to make it stop overwriting the index

with open("input-prod.txt") as f:
    data = f.read().split("\n")

data = data[0]

index = 0

for i, char in enumerate(data):
    isShorter = int(len(set(data[i - 14:i])) == len(data[i - 14:i]))
    isZero = int(index == 0)
    greaterThan14 = int(i > 14)

    index = index + ((isShorter * i) * isZero * greaterThan14)

print(index, data[index])