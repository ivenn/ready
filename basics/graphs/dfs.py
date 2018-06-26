from utils import test_graphs


def dfs_recur(graph, start):

    parents = {start: None}

    def dfs(v):
        for u in graph[v]:
            if u not in parents:
                parents[u] = v
                dfs(u)

    dfs(start)

    return parents


def dfs_iter(graph, start):

    parents = {start: None}
    stack = [start, ]

    while stack:
        v = stack.pop()

        for u in graph[v]:
            if u not in parents:
                parents[u] = v
                stack.append(u)

    return parents


BLACK = "BLACK"
GREY = "GREY"
WHITE = "WHITE"


class DFS:

    def __init__(self, graph):
        self.time = 0
        self.graph = graph

    def _dfs_visit(self, start):
        start.color = GREY
        self.time += 1
        start.dis_t = self.time
        for v in self.graph[start]:
            if v.color == WHITE:
                v.parent = start
                self._dfs_visit(v)

        start.color = BLACK
        self.time += 1
        start.fin_t = self.time

    def do(self):
        for v in self.graph:
            v.color = WHITE
            v.parent = None

        for v in sorted(self.graph, key=lambda x: x.val):
            if v.color == WHITE:
                self._dfs_visit(v)


if __name__ == "__main__":
    for g in test_graphs:
        start = sorted(g.keys(), key=lambda vertex: vertex.val)[0]
        print("dfs_recur", dfs_recur(g, start))
        print("dfs_iter ", dfs_iter(g, start))
        print(DFS(g).do())

