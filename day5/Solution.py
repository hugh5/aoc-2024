import sys
from collections import defaultdict

def solution():
    lines = sys.stdin.read().splitlines()
    ordering = defaultdict(set)
    order_mode = True
    part1, part2 = 0, 0

    def get_correct_ordering(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and (key in ordering[arr[j]]):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr[len(arr)//2]

    for line in lines:
        if len(line) == 0:
            order_mode = False
            continue
        if order_mode:
            num1, num2 = map(int, line.split("|"))
            ordering[num1].add(num2)
        else:
            update = list(map(int, line.split(",")))
            seen = set()
            for num in update:
                seen.add(num)
                if len(ordering[num].intersection(seen)) != 0:
                    part2 += get_correct_ordering(update)
                    break
            else:
                part1 += update[len(update) // 2]

    return part1, part2

if __name__ == '__main__':
    print(solution())