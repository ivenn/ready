class TopologicalSort:

    def __init__(self, graph):
        self.graph = graph
        self.time = 0
        self.visited = set()
        self.distances = {v: [None, None] for v in graph}
        self.res = []

    def __dfs(self, start):
        self.time += 1
        self.distances[start][0] = self.time

        for v in self.graph[start]:
            if v not in self.visited:
                self.__dfs(v)

        self.time += 1
        self.visited.add(start)
        self.distances[start][1] = self.time
        self.res.insert(0, start)

    def do(self):
        for v in sorted(self.graph):
            if v not in self.visited:
                self.__dfs(v)

        print("Start/Finish processing:")
        print(["%s:%s" % (v, self.distances[v]) for v in self.res])

        return self.res


shirt = "1-shirt"
tie = "2-tie"
jacket = "3-jacket"
belt = "4-belt"
watch = "5-watch"
briefs = "6-briefs"
pants = "7-pants"
shoes = "8-shoes"
socks = "9-socks"


graph = {shirt: [tie, belt],
         tie: [jacket],
         jacket: [],
         belt: [jacket],
         watch: [],
         briefs: [pants, shoes],
         pants: [belt, shoes],
         shoes: [],
         socks: [shoes],
         }


print(TopologicalSort(graph).do())
