import sys
import re

def solution():
    stdin = sys.stdin.read()
    op_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    op_iter = list(op_regex.finditer(stdin))
    part1 = 0
    for op in op_iter:
        part1 += int(op.group(1)) * int(op.group(2))

    do_regex = re.compile(r'do\(\)')
    dont_regex = re.compile(r"don't\(\)")
    do_iter = list(do_regex.finditer(stdin))
    dont_iter = list(dont_regex.finditer(stdin))
    operations = sorted(op_iter + do_iter + dont_iter, key=lambda x: x.start())

    part2 = 0
    do = True
    for op in operations:
        if op.re == op_regex and do:
            part2 += int(op.group(1)) * int(op.group(2))
        elif op.re == do_regex:
            do = True
        elif op.re == dont_regex:
            do = False

    return part1, part2


if __name__ == '__main__':
    print(solution())