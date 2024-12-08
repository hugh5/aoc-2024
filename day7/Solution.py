import re
import sys


def solution():
    lines = sys.stdin.read().splitlines()
    regex = re.compile(r'(\d+):([ \d+]+)')

    def is_true(curr, target, numbers):
        if len(numbers) == 0:
            return curr == target
        return (
                is_true(curr+numbers[0], target, numbers[1:]) or
                is_true(curr*numbers[0], target, numbers[1:]) or
                is_true(int(str(curr) + str(numbers[0])), target, numbers[1:])
            )

    result = 0
    for line in lines:
        match = regex.match(line)
        target = int(match.group(1))
        nums = list(map(int, match.group(2).split()))
        if is_true(nums[0], target, nums[1:]):
            result += target
    return result

if __name__ == '__main__':
    print(solution())