from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src, dest):
        """Add an edge between source and destination"""
        if src not in self.adj_list:
            self.add_vertex(src)
        if dest not in self.adj_list:
            self.add_vertex(dest)

        self.adj_list[src].append(dest)
        if not self.directed:
            self.adj_list[dest].append(src)

    def remove_edge(self, src, dest):
        """Remove the edge between src and dest."""
        if src in self.adj_list and dest in self.adj_list[src]:
            self.adj_list[src].remove(dest)
        if not self.directed and dest in self.adj_list and src in self.adj_list[dest]:
            self.adj_list[dest].remove(src)

    def remove_vertex(self, vertex):
        """Remove a vertex and all associated edges."""
        if vertex in self.adj_list:
            del self.adj_list[vertex]
        for neighbors in self.adj_list.values():
            if vertex in neighbors:
                neighbors.remove(vertex)

    def get_vertices(self):
        """Return all vertices in the graph."""
        return list(self.adj_list.keys())

    def get_edges(self):
        """Return all edges in the graph as (src, dest) tuples."""
        edges = []
        for src in self.adj_list:
            for dest in self.adj_list[src]:
                if self.directed or (dest, src) not in edges:
                    edges.append((src, dest))
        return edges
    
    def bfs(self, start):
        discovered = {v: False for v in self.adj_list}
        q = deque()
        discovered[start] = True
        q.append(start)
        
        while q:
            v = q.popleft()
            print(v)
            for u in self.adj_list[v]:
                if not discovered[u]:
                    discovered[u] = True
                    q.append(u)
    
    def dfs(self, start):
        discovered = {v: False for v in self.adj_list}
        stack = [start]
        
        while stack:
            v = stack.pop()
            if not discovered[v]:
                print(v)
                discovered[v] = True
                for u in reversed(self.adj_list[v]):  
                    if not discovered[u]:
                        stack.append(u)

    def __repr__(self):
        return "\n".join(f"{v}: {n}" for v, n in self.adj_list.items())
