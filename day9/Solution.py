import sys


def solution():
    line = sys.stdin.read().strip()
    files = []

    for i, num in enumerate(map(int, line)):
        if i % 2 == 0:
            files.extend([i//2]*num)
        else:
            files.extend([None]*num)

    part1 = list(files)
    left = part1.index(None)
    right = len(part1) - 1
    while left < right:
        while part1[right] is None and right > left:
            right -= 1
        if right <= left:
            break
        part1[left] = part1[right]
        part1[right] = None
        left = part1.index(None, left)

    part1_res = 0
    for i, file in enumerate(part1):
        if file is not None:
             part1_res += i * file

    part2 = list(files)
    rev = list(reversed(part2))

    def find_block(max_i, size):
        i = 0
        while i + size <= max_i:
            if part2[i:i+size] == [None] * size:
                return i
            i += 1
        return -1

    file_id = part2[len(part2)-1]

    while file_id >= 0:
        left = part2.index(file_id)
        right = len(rev) - 1 - rev.index(file_id)
        block_size = right - left + 1
        i = find_block(left, block_size)
        if i != -1:
            part2[i:i+block_size] = [file_id] * block_size
            part2[left:left+block_size] = [None] * block_size
        file_id -= 1

    part2_res = 0
    for i, file in enumerate(part2):
        if file is not None:
            part2_res += i * file

    return part1_res, part2_res


if __name__ == '__main__':
    print(solution())
