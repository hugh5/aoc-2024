import math
from functools import cache

def solution():
    stones = list(map(int, open("input.txt", "r").read().split()))

    @cache
    def rec(stone, n):
        if n == 0:
            return 1
        elif stone == 0:
            return rec(1, n-1)
        elif (d := math.floor(math.log10(stone)) + 1) % 2 == 0:
            return rec(int(str(stone)[:d//2]), n-1) + rec(int(str(stone)[d//2:]), n-1)
        else:
            return rec(2024*stone, n-1)

    return sum(map(lambda s: rec(s, 25), stones)), sum(map(lambda s: rec(s, 75), stones))

if __name__ == '__main__':
    print(solution())