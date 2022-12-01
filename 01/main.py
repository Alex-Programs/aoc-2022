with open("input.txt") as f:
    data = f.read()

totals = []
total = 0
for line in data.split("\n"):
    try:
        total += int(line)
    except:
        totals.append(total)
        total = 0

print(max(totals))
totals = sorted(totals)
print(totals[-3:])
print(sum(totals[-3:]))