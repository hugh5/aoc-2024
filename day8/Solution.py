import sys
from collections import defaultdict


def solution():
    lines = sys.stdin.read().splitlines()
    antennas = defaultdict(list)
    max_y = len(lines)
    max_x = len(lines[0])
    part1 = set()
    part2 = set()

    for j, row in enumerate(lines):
        for i, col in enumerate(row):
            if col != ".":
                antennas[col].append((i, j))

    def valid(x ,y):
        return 0 <= x < max_x and 0 <= y < max_y

    for key, value in antennas.items():
        part2.update(set(value))
        for a in range(len(value) - 1):
            for b in range(a + 1, len(value)):
                anti1 = tuple(map(lambda c: 2*c[0]-c[1], zip(value[a], value[b])))
                anti2 = tuple(map(lambda c: 2*c[0]-c[1], zip(value[b], value[a])))
                if valid(*anti1):
                    part1.add(anti1)
                if valid(*anti2):
                    part1.add(anti2)
                dx, dy = tuple(map(lambda c: c[0] - c[1], zip(value[a], value[b])))
                x, y = value[b]
                while valid(x + dx, y + dy):
                    part2.add((x + dx, y + dy))
                    x += dx
                    y += dy
                dx, dy = -dx, -dy
                x, y = value[a]
                while valid(x + dx, y + dy):
                    part2.add((x + dx, y + dy))
                    x += dx
                    y += dy

    return len(part1), len(part2)

if __name__ == '__main__':
    print(solution())