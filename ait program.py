Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Task-1

from collections import deque

def create_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for i in range(n):
        node = input(f"Enter name of node {i + 1}: ")
        graph[node] = []
    
    e = int(input("Enter number of edges (paths): "))
    for i in range(e):
        src = input(f"Enter source node for edge {i + 1}: ")
        dest = input(f"Enter destination node for edge {i + 1}: ")
        graph[src].append(dest)
...     
...     return graph
... 
... def dfs(graph, node, visited=None):
...     if visited is None:
...         visited = set()
...     if node not in visited:
...         print(f"Visited: {node}")
...         visited.add(node)
...         for neighbor in graph[node]:
...             dfs(graph, neighbor, visited)
... 
... def bfs(graph, start):
...     visited = set()
...     queue = deque([start])
...     while queue:
...         node = queue.popleft()
...         if node not in visited:
...             print(f"Visited: {node}")
...             visited.add(node)
...             queue.extend(graph[node])
... 
... def main():
...     print("===== Graph Creation =====")
...     graph = create_graph()
... 
...     print("\n===== Graph Structure =====")
...     for node, neighbors in graph.items():
...         print(f"{node} -> {neighbors}")
... 
...     start = input("\nEnter starting node for traversal: ")
... 
...     print("\n===== DFS Traversal =====")
...     dfs(graph, start)
... 
...     print("\n===== BFS Traversal =====")
...     bfs(graph, start)
... 
... if __name__ == "__main__":
