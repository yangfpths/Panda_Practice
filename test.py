from collections import deque
def split_tuple(token):
    temp = token.split(",")
    return int(temp[0]), int(temp[1])
token = input().split()
row, column = split_tuple(token[0])
start_position = split_tuple(token[1])
end_position = split_tuple(token[2])
block = []
total_node = []
for tokens in token[4:]:
    block.append(split_tuple(tokens))
del(token[:])
for i in range(int(row)+1):
    for j in range(int(column)+1):
        total_node.append((i, j))
unblock_node = list((set(total_node)-set(block)))
del(total_node[:])
del(block[:])
def neighbours(unblock_node,position):
    x,y = position
    potential_node = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
    exist_node = [node for node in potential_node if node in unblock_node]
    return exist_node

def bfs(unblock_node,start_position,end_position):
    queue = deque([(start_position,[start_position])])
    while queue:
        node,path = queue.popleft()
        for neighbour in neighbours(unblock_node,node):
            if neighbour not in path:
                if neighbour ==end_position:
                    return path+[end_position]
                else:
                    queue.append((neighbour,path+[neighbour]))
    return "no way out"

path = bfs(unblock_node,start_position,end_position)
if path =="no way out":
    print(path)
else:
    for node in path:
        x,y = node
        print("["+str(x)+","+str(y)+"]",end ="")

'''2,2 0,0 2,2 3 0,1 2,0 2,1'''