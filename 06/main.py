import sys
if len(sys.argv) > 1 and sys.argv[1] == "prod":
    print("USING PROD INPUT")
    with open("input-prod.txt") as f:
        data = f.read().split("\n")
else:
    print("USING DEV INPUT")
    with open("input-test.txt") as f:
        data = f.read().split("\n")

for line in data:
    print(line)