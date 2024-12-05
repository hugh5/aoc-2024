import sys

def solution():
    lines = list(map(lambda line: list(map(int, line.split())), sys.stdin.read().split("\n")[:-1]))

    diff = map(lambda line: [curr - prev for prev, curr in zip(line[:-1], line[1:])], lines)
    safe = map(lambda line: all(map(lambda x: 1 <= x <= 3, line)) or all(map(lambda x: -3 <= x <= -1, line)), diff)
    part1 = sum(safe)

    combos = map(lambda line: [line] + [line[:i] + line[i+1:] for i in range(len(line))], lines)
    diff2 = map(lambda report: map(lambda level:
                                   [curr - prev for prev, curr in zip(level[:-1], level[1:])], report), combos)
    safe2 = map(lambda combo: map(lambda report: all(map(lambda x: 1 <= x <= 3, report)) or
                                                 all(map(lambda x: -3 <= x <= -1, report)), combo), diff2)
    part2 = sum(map(any, safe2))
    return part1, part2

if __name__ == '__main__':
    print(solution())

