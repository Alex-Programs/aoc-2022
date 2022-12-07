with open("input.txt") as f:
    data = f.read().split("\n")

from collections import defaultdict
from dataclasses import dataclass

path = []


@dataclass
class Node:
    name: str
    children: list
    parent: object
    size: int


tree = Node("/", [], None, 0)

currentNode = None
for line in data:
    match line.split(" "):
        case "$", "cd", "/":
            currentNode = tree
        case "$", "cd", "..":
            currentNode = currentNode.parent
        case "$", "cd", x:
            childrenWithName = [child for child in currentNode.children if child.name == x]
            if len(childrenWithName) == 0:
                newNode = Node(x, [], currentNode, 0)
                currentNode.children.append(newNode)
            else:
                newNode = childrenWithName[0]

            currentNode = newNode

        case "$", "ls":
            pass
        case "dir", _:
            pass
        case size, name:
            newNode = Node(name, [], currentNode, int(size))
            currentNode.children.append(newNode)


def dfs(current):
    for node in current.children:
        if len(node.children) == 0:
            current.size += node.size
        else:
            othernode = dfs(node)
            current.size += othernode.size

    return current


sized = dfs(tree)

print(sized)

class State:
    sum = 0
    toDelete = 9999999999999999999999
    toFree = 0

def flatten(parent, totalSizes):
    for node in parent.children:
        if len(node.children) > 0:
            flatten(node, totalSizes)

    if parent.size < 100000 and len(parent.children) > 0:
        State.sum += int(parent.size)

    if parent.size > State.toFree and parent.size < State.toDelete:
        State.toDelete = parent.size

    return 0


p1ans = 0
totalSizes = []

print(sized)
currentFree = 70000000 - sized.size
amountToFree = 30000000 - currentFree
State.toFree = amountToFree

flat = flatten(sized, 0)
print(State.sum)
print(State.toDelete)

print(flat)
