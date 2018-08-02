# Solution 1: Stack
stack=[]
While stack:
  current=stack.pop()
  for neighbor in adjacentlist[current]:
    if neighbor not in visitedlist:
      stack.append(neighbor)
  visitedlist.append(current)
    
 # Solution 2: recursive

def dfs( vertex):
  for neigbhor in vertex:
    if neighbor not in adjacentlist[vertex]:
      dfs(neighbor)
  return 
  
  
  
