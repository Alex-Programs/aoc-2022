import sys
if len(sys.argv) > 1 and sys.argv[1] == "prod":
    print("USING PROD INPUT")
    with open("input-prod.txt") as f:
        data = f.read().split("\n")
else:
    print("USING DEV INPUT")
    with open("input-test.txt") as f:
        data = f.read().split("\n")

data = data[0]

for i, char in enumerate(data):
    if i < 14:
        continue

    chars = {}
    for char in data[i-14:i]:
        chars[char] = chars.get(char, 0) + 1

    if max(chars.values()) < 2:
        print(i, data[i], chars)
        break