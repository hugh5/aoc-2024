import sys
import re

def solution():
    input = sys.stdin.read()
    op_regex = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    op_iter = list(op_regex.finditer(input))
    part1 = 0
    for op in op_iter:
        match_str = op.group()
        num1, num2 = map(int, re.findall(r'\d{1,3}', match_str))
        part1 += num1 * num2

    do_regex = re.compile(r'do\(\)')
    dont_regex = re.compile(r"don't\(\)")
    do_iter = list(do_regex.finditer(input))
    dont_iter = list(dont_regex.finditer(input))
    operations = sorted(op_iter + do_iter + dont_iter, key=lambda x: x.start())

    part2 = 0
    do = True
    for op in operations:
        match_str = op.group()
        if op.re == op_regex and do:
            nums = re.findall(r'\d{1,3}', match_str)
            num1, num2 = list(map(int, nums))
            part2 += num1 * num2
        elif op.re == do_regex:
            do = True
        elif op.re == dont_regex:
            do = False

    return part1, part2


if __name__ == '__main__':
    print(solution())