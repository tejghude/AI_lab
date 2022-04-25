graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = [] 
queue = []   

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
     print('Visited :',visited)
     print('Queue :',queue , "\n" )

     t = queue.pop(0)
     for n in graph[t]:
        if n not in visited :
          visited.append(n)
          queue.append(n)  

print("Breadth-First Search")
bfs(visited, graph, '5')
