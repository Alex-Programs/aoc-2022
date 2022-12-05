# Get A
def get_a(line):
    return set(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1))

def get_b(line):
    return set(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1))

# Part 1
print(sum([1 for line in open("input.txt").readlines() if get_a(line).issubset(get_b(line)) or get_b(line).issubset(get_a(line))]))

# Part 2
print(sum([1 for line in open("input.txt").readlines() if len(get_a(line).intersection(get_b(line))) > 0]))

# Part 1 and 2 but they're not calling functions anymore
print(sum([1 for line in open("input.txt").readlines() if set(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)).issubset(set(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1))) or set(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1)).issubset(set(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)))]))
print(sum([1 for line in open("input.txt").readlines() if len(set(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)).intersection(set(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1)))) > 0]))

# Part 1 and 2 but they're totally unreadable
print(sum([1 for l in open("input.txt").readlines() if set(range(int(l.split(",")[0].split("-")[0]), int(l.split(",")[0].split("-")[1]) + 1)).issubset(set(range(int(l.split(",")[1].split("-")[0]), int(l.split(",")[1].split("-")[1]) + 1))) or set(range(int(l.split(",")[1].split("-")[0]), int(l.split(",")[1].split("-")[1]) + 1)).issubset(set(range(int(l.split(",")[0].split("-")[0]), int(l.split(",")[0].split("-")[1]) + 1)))]))
print(sum([1 for l in open("input.txt").readlines() if len(set(range(int(l.split(",")[0].split("-")[0]), int(l.split(",")[0].split("-")[1]) + 1)).intersection(set(range(int(l.split(",")[1].split("-")[0]), int(l.split(",")[1].split("-")[1]) + 1)))) > 0]))

# Part 1 and 2 but it's actually one line now
print(sum([1 for l in open("input.txt").readlines() if set(range(int(l.split(",")[0].split("-")[0]), int(l.split(",")[0].split("-")[1]) + 1)).issubset(set(range(int(l.split(",")[1].split("-")[0]), int(l.split(",")[1].split("-")[1]) + 1))) or set(range(int(l.split(",")[1].split("-")[0]), int(l.split(",")[1].split("-")[1]) + 1)).issubset(set(range(int(l.split(",")[0].split("-")[0]), int(l.split(",")[0].split("-")[1]) + 1)))]), sum([1 for l in open("input.txt").readlines() if len(set(range(int(l.split(",")[0].split("-")[0]), int(l.split(",")[0].split("-")[1]) + 1)).intersection(set(range(int(l.split(",")[1].split("-")[0]), int(l.split(",")[1].split("-")[1]) + 1)))) > 0]))

# Cursed
H='input.txt';G=open;D=sum;F=range;E=set;C='-';B=',';A=int;print(D([1 for D in G(H).readlines()if E(F(A(D.split(B)[0].split(C)[0]),A(D.split(B)[0].split(C)[1])+1)).issubset(E(F(A(D.split(B)[1].split(C)[0]),A(D.split(B)[1].split(C)[1])+1)))or E(F(A(D.split(B)[1].split(C)[0]),A(D.split(B)[1].split(C)[1])+1)).issubset(E(F(A(D.split(B)[0].split(C)[0]),A(D.split(B)[0].split(C)[1])+1)))]),D([1 for D in G(H).readlines()if len(E(F(A(D.split(B)[0].split(C)[0]),A(D.split(B)[0].split(C)[1])+1)).intersection(E(F(A(D.split(B)[1].split(C)[0]),A(D.split(B)[1].split(C)[1])+1))))>0]))