class Life:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.frame = [[0 for x in range(width)] for y in range(height)]

    def import_frame(self, fname):
        with open(fname, 'r') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            line_vals = list(map(int, line.split(' ')))
            self.frame[i] = [line_vals[j] if j < len(line_vals) else self.frame[i][j] for j in range(len(self.frame[i]))]

    def tick(self):
        next_gen = [[0 for x in range(self.width)] for y in range(self.height)]
        f = self.frame
        for i in range(self.height):
            for j in range(self.width):
                u = i - 1 #up
                d = i + 1 if i + 1 < self.height else 0 #down
                l = j - 1 #left
                r = j + 1 if j + 1 < self.width else 0 #right
                alive_neighbours = f[u][l] + f[u][j] + f[u][r] + f[i][l] + f[i][r] + f[d][l] + f[d][j] + f[d][r]
                if f[i][j]:
                    if  1 < alive_neighbours < 4:
                        next_gen[i][j] = 1
                else:
                    if alive_neighbours == 3:
                        next_gen[i][j] = 1
        self.frame = next_gen
