from collections import defaultdict
class Region:
    def __init__(self, ch):
        self.plant = ch
        self.plots = set()
        self.perimeter = 0
        self.sides = 0

    def add(self, item):
        self.plots.add(item)

    def __contains__(self, item):
        return item in self.plots

    def inc_perimeter(self):
        self.perimeter += 1

    def num_sides(self):
        sides = 0
        for x, y in self.plots:
            # Left side
            if (x - 1, y) not in self.plots:
                if (x, y - 1) in self.plots:
                    if (x - 1, y - 1) in self.plots:
                        sides += 1
                else:
                    sides += 1
            # Right side
            if (x + 1, y) not in self.plots:
                if (x, y - 1) in self.plots:
                    if (x + 1, y - 1) in self.plots:
                        sides += 1
                else:
                    sides += 1
            # Top Side
            if (x, y - 1) not in self.plots:
                if (x - 1, y) in self.plots:
                    if (x - 1, y - 1) in self.plots:
                        sides += 1
                else:
                    sides += 1
            # Bottom Side
            if (x, y + 1) not in self.plots:
                if (x - 1, y) in self.plots:
                    if (x - 1, y + 1) in self.plots:
                        sides += 1
                else:
                    sides += 1
        return sides

    def price(self):
        return len(self.plots) * self.perimeter

    def price2(self):
        return len(self.plots) * self.num_sides()

def solution():
    data = open("input.txt", "r").read().splitlines()
    max_y = len(data)
    max_x = len(data[0])
    visited = set()
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    regions = defaultdict(list)

    def bfs(x, y, ch):
        if (x, y) not in visited:
            if data[y][x] == ch:
                regions[ch][-1].add((x, y))
                visited.add((x, y))

        for dx, dy in directions:
            if 0 <= x+dx < max_x and 0 <= y+dy < max_y:
                if (x+dx, y+dy) not in visited:
                    if data[y+dy][x+dx] == ch:
                        bfs(x+dx, y+dy, ch)

    for j in range(max_y):
        for i in range(max_x):
            if (i, j) not in visited:
                plant = data[j][i]
                regions[plant].append(Region(plant))
                bfs(i, j, plant)

    for j in range(max_y):
        for i in range(max_x):
            region = None
            for r in regions[data[j][i]]:
                if (i, j) in r:
                    region = r
                    break
            if i == 0 or data[j][i-1] != region.plant:
                region.inc_perimeter()
            if i == max_x - 1 or data[j][i+1] != region.plant:
                region.inc_perimeter()
            if j == 0 or data[j-1][i] != region.plant:
                region.inc_perimeter()
            if j == max_y - 1 or data[j+1][i] != region.plant:
                region.inc_perimeter()

    part1 = 0
    part2 = 0
    for l in regions.values():
        for region in l:
            part1 += region.price()
            part2 += region.price2()

    return part1, part2

if __name__ == '__main__':
    print(solution())
