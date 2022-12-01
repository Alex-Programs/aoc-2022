totals=sorted([sum([int(y) for y in x.split("\n")]) for x in open("input.txt").read().split("\n\n")])
print(max(totals))
print(sum(totals[-3:]))