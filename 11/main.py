with open("input.txt") as f:
    data = f.read().split("\n")

def process_operation(operation, indata):
    splitted = operation.split(" ")
    match splitted:
        case "old", "*", "old":
            return indata * indata
        case "old", "*", value:
            return indata * int(value)
        case "old", "+", value:
            return indata + int(value)
        case "old", "-", value:
            return indata - int(value)
        case "old", "/", value:
            return indata / int(value)
        case "old", "%", value:
            return indata % int(value)


class Monkey():
    def __init__(self, starting, operation, mid, modtest, on_true, on_false):
        self.mid = int(mid)
        self.items = starting
        self.operation = operation
        self.modtest_value = int(modtest)
        self.on_true_mid = int(on_true)
        self.on_false_mid = int(on_false)
        self.activity = 0

    def modtest(self, x):
        return x % self.modtest_value == 0

    def __repr__(self):
        return f"""Monkey ID {self.mid}
Items: {self.items}
Operation: {self.operation}
Modtest: {self.modtest_value}
On True: Throw to {self.on_true_mid}
On False: Throw to {self.on_false_mid}\n\n"""


monkeys = []
mid = 0
starting = []
operation = ""
modtest = 0
on_true = 0
on_false = 0
for line in data:
    line = line.strip()

    if line == "":
        #print(mid, starting, operation, modtest, on_true, on_false)
        monkeys.append(Monkey(starting, operation, mid, modtest, on_true, on_false))
        continue

    if line.startswith("Monkey "):
        mid = int(line.split(" ")[1].replace(":", ""))
        continue

    if line.startswith("Starting items"):
        starting = [int(x.replace(",", "")) for x in line.split(" ")[2:]]
        continue

    if line.startswith("Operation"):
        operation = line.replace("Operation: new = ", "")
        continue

    if line.startswith("Test:"):
        modtest = int(line.split(" ")[-1])
        continue

    if line.startswith("If true:"):
        on_true = int(line.split(" ")[-1])
        continue

    if line.startswith("If false:"):
        on_false = int(line.split(" ")[-1])
        continue

from math import prod

cap = prod([x.modtest_value for x in monkeys])

for tick in range(10000):
    print(tick)
    #print("___ NEXT ROUND ___")
    for monkey in monkeys:
        if len(monkey.items) == 0:
            continue

        for index, item in enumerate(monkey.items):
            #print(f"Monkey {str(monkey.mid)} inspects item", item)
            newdata = process_operation(monkey.operation, item)
            #print("Due to operation", monkey.operation, "the new data is", newdata)
            #newdata = int(newdata / 3)
            #print("Due to division by 3, the new data is", newdata)
            # Adjust for ludicrous numbers
            newdata = newdata % cap

            if monkey.modtest(newdata):
                #print("Monkey throws item", newdata, "to monkey", monkey.on_true_mid, "due to modtest being true")
                target = [x for x in monkeys if x.mid == monkey.on_true_mid][0]
                target.items.append(newdata)
            else:
                #print("Monkey throws item", newdata, "to monkey", monkey.on_false_mid, "due to modtest being false")
                target = [x for x in monkeys if x.mid == monkey.on_false_mid][0]
                target.items.append(newdata)

            monkey.activity += 1

        monkey.items = []

        #print("__________ NEXT MONKEY __________")

#for monkey in monkeys:
    #print(monkey.items)

most_active = sorted(monkeys, key=lambda x: x.activity, reverse=True)

two_most_active = most_active[:2]
monkey_business = two_most_active[0].activity * two_most_active[1].activity

print("The two most active monkeys multiplied together is", monkey_business)