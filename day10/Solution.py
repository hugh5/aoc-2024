
def solution():
    data = list(map(lambda row: list(map(int, row)), open("input.txt", "r").read().splitlines()))
    heads = []
    for j, row in enumerate(data):
        for i, num in enumerate(row):
            if num == 0:
                heads.append((i, j))

    max_y = len(data)
    max_x = len(data[0])
    directions = [(0,1), (0,-1), (-1, 0), (1, 0)]

    def dfs(x, y, h):
        p1 = set()
        p2 = 0
        for dx, dy in directions:
            if 0 <= x+dx < max_x and 0 <= y+dy < max_y:
                if data[y+dy][x+dx] == h + 1:
                    if h + 1 == 9:
                        p1.add((x+dx, y+dy))
                        p2 += 1
                    else:
                        pos, count = dfs(x+dx, y+dy, h+1)
                        p1.update(pos)
                        p2 += count
        return p1, p2

    part1 = 0
    part2 = 0
    for x,y in heads:
        result = dfs(x, y, 0)
        part1 += len(result[0])
        part2 += result[1]
    return part1, part2




if __name__ == '__main__':
    print(solution())