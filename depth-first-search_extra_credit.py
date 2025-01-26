## Extra credit: DFS 
# Implement dfs to find the # of unique cycles in a graph. 

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
n = list(range(7))
e = [(i, i+1) for i in range(len(n)-1)]
more = [(1,5),(2,5),(2,3),(3,4)]
e = e+more
print(f"all edges: {e}")

for i in n:
    g.add_nodes_from(n)
g.add_edges_from(e)

fig = plt.figure()
nx.draw_networkx(g)
plt.savefig("fig.png")

def count_rings(graph) -> int:
    # count the # of unique cycles in a graph.
    adj_list = dict()
    for line in nx.generate_adjlist(graph):
        adj_list[int(line[0])] = [int(i) for i in line[1:] if i != ' ']
    print(f"adj_list: {adj_list}")
    MyCycles = set()

    def dfs_util(v, adj_list, visited, path):
        visited[v] = True
        path.append(v)

        for neighbor in adj_list[v]: # For v's neighbors
            if not visited[neighbor]: # if the neighbors haven't been visited
                path.append(neighbor) # append neighbor to path
                dfs_util(neighbor, adj_list, visited, path) # traverse graph
            elif neighbor in path: # if neighbor is in the path 
                # print(f"my path: {path}")
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:]
                MyCycles.add(tuple((sorted(cycle))))
                path.pop() # back track
        return False
        
    def checking_more_cycles(adj_list):
        visited = [False] * len(adj_list)
        for node in adj_list:
            if not visited[node]:
                dfs_util(node, adj_list, visited, [])
        return len(MyCycles)
    return checking_more_cycles(adj_list)
              
print(count_rings(g))
