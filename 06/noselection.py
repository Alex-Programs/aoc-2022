# Doesn't work
# Need to make it stop overwriting the index

with open("input-test.txt") as f:
    data = f.read().split("\n")

data = data[0]

index = 0

for i, char in enumerate(data):
    if i > 4:
        print(int(len(set(data[i - 4:i])) == len(data[i - 4:i])), i)
        print(int(index != 0), i)
        index = (int(len(set(data[i - 4:i])) == len(data[i - 4:i])) * i) * int(index == 0)
        print(index)
        print("----")

print(index, data[index])