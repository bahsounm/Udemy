'''
    BFS
    searching graph algorithm
    think of 2 things
    1) breadth meand broad and wide, progress horizzontally then veritacally
    2) use a queue for keeping track of verticies 

    visit a node, add its adjacent nodes to the queue, mark recent as visited and then add its adjeacent
    we visit nodes at the same level before we move to the next level
    
    O (V + E)
'''
def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)




'''
    DFS
    searching graph algorithm
    think of 2 things
    1) depth means vertical search before a horizontal search
    2) use a stack for keeping track of verticies 

    like above but since its a stack this is how we move vertically instead of horizontally

'''

def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=" ")

        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)


