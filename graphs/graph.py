"""Graph algorithms: BFS, DFS and Dijkstra's shortest path.

Graphs are stored as adjacency lists (dict of node -> list of (neighbour, weight)).
"""
import heapq
from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        self.adj.setdefault(u, []).append((v, weight))
        self.adj.setdefault(v, [])
        if not self.directed:
            self.adj[v].append((u, weight))

    def bfs(self, start):
        visited = [start]
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbour, _ in self.adj.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited

    def dfs(self, start, visited=None):
        if visited is None:
            visited = []
        visited.append(start)
        for neighbour, _ in self.adj.get(start, []):
            if neighbour not in visited:
                self.dfs(neighbour, visited)
        return visited

    def dijkstra(self, start):
        """Returns a dict of shortest distances from start to every node."""
        dist = {node: float("inf") for node in self.adj}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neighbour, weight in self.adj[node]:
                new_d = d + weight
                if new_d < dist[neighbour]:
                    dist[neighbour] = new_d
                    heapq.heappush(pq, (new_d, neighbour))
        return dist


if __name__ == "__main__":
    # small map of towns, weights are km (roughly)
    g = Graph()
    g.add_edge("Nairobi", "Thika", 45)
    g.add_edge("Nairobi", "Machakos", 63)
    g.add_edge("Thika", "Nyeri", 105)
    g.add_edge("Machakos", "Kitui", 106)
    g.add_edge("Nyeri", "Nanyuki", 58)
    print("BFS from Nairobi:", g.bfs("Nairobi"))
    print("DFS from Nairobi:", g.dfs("Nairobi"))
    print("Shortest distances:", g.dijkstra("Nairobi"))
