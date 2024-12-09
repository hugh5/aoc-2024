import sys
from collections import deque


def solution():
    data = map(int, sys.stdin.read().strip())
    part1 = []
    part2 = []
    free_positions = deque()
    free_positions2 = []

    file_id = 0
    file_position = 0
    for i, num in enumerate(data):
        if i % 2 == 0:
            part1.extend([file_id] * num)
            part2.append((file_position, num))
            file_position += num
            file_id += 1
        else:
            free_positions.extend(range(len(part1), len(part1) + num))
            free_positions2.extend(range(len(part1), len(part1) + num))
            part1.extend([-1] * num)
            file_position += num

    highest_pos = len(part1) - 1
    while len(free_positions) > 0 and free_positions[0] < highest_pos:
        part1[free_positions.popleft()] = part1[highest_pos]
        part1[highest_pos] = -1
        while highest_pos >= 0 and part1[highest_pos] == -1:
            highest_pos -= 1

    for fid in range(len(part2) - 1, -1, -1):
        file_pos, size = part2[fid]
        for i in range(len(free_positions2) - size + 1):
            if free_positions2[i] > file_pos:
                break
            if free_positions2[i:i + size] == list(range(free_positions2[i], free_positions2[i] + size)):
                part2[fid] = (free_positions2[i], size)
                free_positions2[i:i + size] = []
                break

    return (
        sum(map(lambda x: x[0] * x[1] if x[1] != -1 else 0, enumerate(part1))),
        sum(map(lambda x: sum(map(lambda i: i * x[0], range(x[1][0], x[1][0] + x[1][1]))), enumerate(part2)))
    )


if __name__ == '__main__':
    print(solution())
