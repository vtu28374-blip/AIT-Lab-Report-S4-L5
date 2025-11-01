graph = {
    'a': [('b', 2)],
    'b': [('c', 3)],
    'c': [('d', 1)],
    'd': [('a', 4)]
}

total_cost = 0
for node in ['a', 'b', 'c', 'd']:
    neighbor, cost = graph[node][0]
    print(f"cost from {node} to {neighbor}: {cost}")
    total_cost += cost

print(f"Total cost: {total_cost}")
