from Queue import Queue
import copy


WHITE = 'WHITE'
GRAY = 'GRAY'
BLACK = 'BLACK'


def bfs_cormen(graph, start):
    start.dist = 0
    start.color = GRAY
    start.parent = None

    for v in [v for v in graph if v is not start]:
        v.color = WHITE
        v.dist = None
        v.parent = None

    q = Queue()

    q.put(start)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if v.color == WHITE:
                v.color = GRAY
                v.dist = u.dist + 1
                v.parent = u
                q.put(v)
        u.color = BLACK


def bfs(graph, start):

    queue = Queue()
    queue.put(start)

    levels = {start: 0}
    visited = {start, }

    while not queue.empty():
        v = queue.get()
        neighbours = graph[v]

        to_do = [n for n in neighbours if n not in visited]

        for neighbour in to_do:
            queue.put(neighbour)
            visited.add(neighbour)
            levels[neighbour] = levels[v] + 1

    return levels


def dfs(graph, start, visited=None):
    print(start)
    if visited is None:
        visited = set()
    visited.add(start)
    for next in set(graph[start]) - visited:
        dfs(graph, next, visited)
    return visited


def dfs2(graph, start):

    parent = {start: None}

    def dfs_visit(s):

        for v in graph[s]:
            if v not in parent:
                parent[v] = s
                dfs_visit(v)

    dfs_visit(start)

    return parent


class DFS_Cormen:

    def __init__(self, graph):
        self.time = 0
        self.graph = graph

    def _dfs_visit(self, s):
        print('dfs_visit(%s)' % s)
        s.color = GRAY
        self.time += 1
        s.dis_t = self.time
        for v in self.graph[s]:
            if v.color == WHITE:
                v.parent = s
                self._dfs_visit(v)
            else:
                print("Skip %s" % v)
        s.color = BLACK
        self.time += 1
        s.fin_t = self.time

    def do(self):
        for v in self.graph:
            v.color = WHITE
            v.parent = None

        comp = 0
        for v in sorted(self.graph, key=lambda x: x.val):
            if v.color == WHITE:
                comp += 1
                self._dfs_visit(v)
            else:
                print('Skip %s' % v)
        print(comp)
