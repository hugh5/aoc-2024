import sys

def solution():
    xmas = "XMAS"
    directions = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0) ,          (1, 0),
            (-1, 1) , (0, 1) , (1, 1),
    ]
    rows = sys.stdin.read().split("\n")
    max_y = len(rows)
    max_x = len(rows[0])
    def find_xmas(x, y, dx, dy, ch):
        if 0 <= x < max_x and 0 <= y < max_y:
            if ch == "S":
                return rows[y][x] == "S"
            elif ch == rows[y][x]:
                return find_xmas(x+dx, y+dy, dx, dy, xmas[xmas.find(ch) + 1])
        return False

    part1 = 0
    for j in range(max_y):
        for i in range(max_x):
            for dx, dy in directions:
                if find_xmas(i, j, dx, dy, xmas[0]):
                    part1 += 1

    x_directions = [
            (-1, -1), (1, -1),
            (-1, 1), (1, 1),
    ]
    def find_x_mas(x,y):
        if 0 < x < max_x - 1 and 0 < y < max_y -1:
            if rows[y][x] == "A":
                m_count = 0
                s_count = 0
                for dx, dy in x_directions:
                    if rows[y+dy][x+dx] == "M":
                        m_count += 1
                    if rows[y+dy][x+dx] == "S":
                        s_count += 1
                if rows[y-1][x-1] != rows[y+1][x+1] and m_count == 2 and s_count == 2:
                    return True
        return False
    part2 = 0
    for j in range(max_y):
        for i in range(max_x):
            if find_x_mas(i, j):
                part2 += 1
    return part1, part2

if __name__ == '__main__':
    print(solution())