with open("input.txt") as f:
    data = f.read()

# Rock: A, X
# Paper: B, Y
# Scissors: C, Z

score = 0
beats = {"A": "Z", "B": "X", "C": "Y"}
score_lookup = {"X": 1, "Y": 2, "Z": 3}
draws = {"A": "X", "B": "Y", "C": "Z", "X": "A", "Y": "B", "Z": "C"}

"""
score = 0
for line in data.split("\n"):
    print(line)
    theirs, mine = line.split(" ")

    if beats.get(theirs) == mine:
        print(f"Theirs {theirs} beats theirs {mine}")
        score += score_lookup.get(mine)
    elif draws.get(theirs) == mine:
        print(f"Draw of {theirs} and {mine}")
        score += 3 + score_lookup.get(mine)
    else:
        print(f"Mine beats theirs")
        score += 6 + score_lookup.get(mine)


print(score)
"""

# Second

score = 0
for line in data.split("\n"):
    print(line)
    theirs, what = line.split(" ")
    if what == "Y":
        # End in draw
        score += 3 + score_lookup.get(draws.get(theirs))

    if what == "X":
        # lose
        score += 0 + score_lookup.get(beats.get(theirs))

    if what == "Z":
        # win
        poss = "XYZ"
        poss = poss.replace(draws.get(theirs), "")
        poss = poss.replace(beats.get(theirs), "")
        score += 6 + score_lookup.get(poss)

print(score)