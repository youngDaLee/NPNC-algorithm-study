from lib2to3.pgen2.token import GREATEREQUAL


class Solution:
    def __init__(self):
        self.dx = [1, -1, 1, -1]
        self.dy = [1, 1, -1, -1]
        self.n = 0
        self.result = []

    def make_next_coord(self, x, y):
        if x+1 == self.n:
            x = 0
            y += 1
        else:
            x += 1
        return x, y

    def make_check_list(self, x, y, graph, queen):
        graph_list = [(graph, queen)]
        if queen <= 0 or graph[x][y] != 0:
            return graph_list

        new_graph = []

        for i in range(self.n):
            g = []
            for j in range(self.n):
                if i == x and j == y:
                    print(graph[x][y])
                    g.append('Q')
                elif i == x or j == y:
                    g.append('.')
                else:
                    g.append(graph[i][j])
            new_graph.append(g)

        print()
        print(x, y)
        for i in range(1, self.n):
            for j in range(4):
                _dx = self.dx[j]*i + x
                _dy = self.dy[j]*i + y
                if _dx < 0 or _dx >= self.n or _dy < 0 or _dy >= self.n:
                    continue
                if graph[_dx][_dy] == 'Q':
                    return []
                new_graph[_dx][_dy] = '.'

        print(new_graph)
        graph_list.append((new_graph, queen-1))
        return graph_list
        ''' king
        for i in range(8):
            _dx = self.dx[i] + x
            _dy = self.dy[i] + y

            if (_dx < 0 or _dx >= self.n ) or (_dy < 0 or _dy >= self.n ):
                continue

            if graph[_dx][_dy] == 'Q':
                return ['.']
        return ['.', 'Q']
        '''

    def dfs(self, x, y, graph, queen):
        if x+1 == self.n and y+1 == self.n or queen==0:
            if queen == 1 and graph[x][y] == 0:
                queen -= 1
                graph[x][y] = 'Q'

            if queen == 0:
                res = []
                for g in graph:
                    res.append(''.join(g))
                self.result.append(res)
            return
        if x >= self.n:
            return

        graph_list = self.make_check_list(x, y, graph, queen)

        for graph, q in graph_list:
            if q != queen:
                next_x = x + 1
                next_y = 0
            else:
                next_x, next_y = self.make_next_coord(x, y)
            self.dfs(next_x, next_y, graph, q)


    def solveNQueens(self, n: int):
        self.n = n

        # make graph
        graph = []
        for i in range(n):
            li = [0] * n
            graph.append(li)

        self.dfs(0, 0, graph, n)

        return self.result


s = Solution()

res = s.solveNQueens(4)
print(res)