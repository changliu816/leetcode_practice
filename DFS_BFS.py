######### DFS
# Solution 1: Stack
def dfs():
  stack=root
  While stack:
    current=stack.pop()
    for neighbor in adjacentlist[current]:
      if neighbor not in visitedlist:
        stack.append(neighbor)
    visitedlist.append(current)
return visitedlist
    
 # Solution 2: recursive

def dfs( vertex):
  for neigbhor in vertex:
    if neighbor not in adjacentlist[vertex]:
      dfs(neighbor)
  return 

######### BFS
def bfs():
  quene=root
  While quene:
    current=quene.pop()
    for neighbor in adjacentlist[current]:
      if neighbor not in visitedlist:
        quene.insert(0,neighbor)
    visitedlist.append(current)
return visitedlist
  
  
  
