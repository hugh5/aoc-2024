import sys
from collections import Counter

def solution():
    lines = list(map(lambda line: list(map(int, line.split())), sys.stdin.read().split("\n")[:-1]))

    left = sorted(map(lambda x: x[0], lines))
    right = sorted(map(lambda x: x[1], lines))
    part1 = sum(map(lambda x: abs(x[0] - x[1]), zip(left,right)))

    occur = Counter(right)
    part2 = sum(key * occur.get(key, 0) for key in left)
    return part1, part2


if __name__ == '__main__':
    print(solution())