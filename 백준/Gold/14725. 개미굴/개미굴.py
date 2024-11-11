import sys
from collections import defaultdict

input = sys.stdin.readline

# 트리 구조를 저장할 딕셔너리
ant_cave = lambda: defaultdict(ant_cave)

def insert(tree, foods):
    for food in foods:
        tree = tree[food]

def display(tree, depth):
    for key in sorted(tree.keys()):
        print('--' * depth + key)
        display(tree[key], depth + 1)

n = int(input().strip())
ant_tree = ant_cave()

for _ in range(n):
    data = input().strip().split()
    k = int(data[0])
    foods = data[1:]
    insert(ant_tree, foods)

display(ant_tree, 0)