import sys


def solution():
    lines = sys.stdin.read().splitlines()
    start = (-1, -1)
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            if ch == "^":
                start = col, row
                break
        else:
            continue
        break

    max_y = len(lines)
    max_x = len(lines[0])

    part1 = set()
    x, y = start
    dy = -1
    dx = 0
    while 0 < x < max_x - 1 and 0 < y < max_y - 1:
        part1.add((x, y))
        y += dy
        x += dx
        if not 0 < x < max_x - 1 or not 0 < y < max_y - 1:
            break
        if lines[y+dy][x+dx] == "#":
            dy, dx = dx, -dy


    part2 = 0
    for barrier_y in range(max_y):
        for barrier_x in range(max_x):
            if lines[barrier_y][barrier_x] == "#" or lines[barrier_y][barrier_x] == "^":
                continue
            x, y = start
            dx, dy = 0, -1
            seen = set()
            while True:
                if (x, y, (dx, dy)) in seen:
                    part2 += 1
                    break

                seen.add((x, y, (dx, dy)))
                if not (0 <= x + dx < max_x) or not (0 <= y + dy < max_y):
                    break
                if lines[y+dy][x+dx] == '#' or y+dy == barrier_y and x+dx == barrier_x:
                    dy, dx = dx, -dy
                else:
                    x = x + dx
                    y = y + dy

    return len(part1) + 1, part2


if __name__ == '__main__':
    print(solution())