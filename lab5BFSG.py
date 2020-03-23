import queue as q
graph = {'A': ['C', 'B'],
         'B': ['E','D', 'A'],
         'C': ['A', 'F'],
         'D': ['H','G','B'],
         'E': ['B','I'],
         'F': ['J','C'],
         'G': ['L','K','D'],
         'H':['D'],
         'I':['M','E'],
         'J':['F'],
         'K':['G'],
         'L':['G'],
         'M':['I']}
q=q.LifoQueue()
def dfs(start,graph,goal):
    q.put(start)
    list = []
    visited= [start]    
    while not q.empty():
        node=q.get()
        list.append(node)
        if node == goal:
            return list
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                q.put(neighbor)
                visited.append(neighbor)
    return list
ans = dfs('A',graph,'G') 
print(ans)
