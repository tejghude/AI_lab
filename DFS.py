graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

v = []
def dfs(v, graph, node): 
    if node not in v:
        v.append(node)
        print ("Visited :",v,"\n")
    
        for n in graph[node]:
            dfs(v, graph, n)

print("Depth-First Search")
dfs(v, graph, '5')
