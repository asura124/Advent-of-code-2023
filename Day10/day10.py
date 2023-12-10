

def steps_farthest(file):
    maze = []
    row = 0
    with open(file) as f:
        for line in f:
            if(line.find('S')!=-1):
                queue = [[row,line.find('S')]]
            line = list(line.strip('\n'))
            maze.append(line)
            row +=1
    visited = {}
    steps = -1
    while(len(queue)!=0):
        curr_len = len(queue)
        for i in range(curr_len):
            r,c = queue[i][0],queue[i][1]
            if((r,c) in visited): #if we already visited node
                continue
            visited[(r,c)] = 1
            if(maze[r][c]=='S'): #beginning where we don't care about our current pipe shape
                if(r-1>=0):
                    if(maze[r-1][c]=='.'):
                        pass
                    elif(maze[r-1][c]=='|' or maze[r-1][c]=='F' or maze[r-1][c]=='7'):
                        if((r-1,c) in visited):
                            pass
                        else:
                            queue.append([r-1,c])
                if(r+1<=len(maze)-1):
                    if(maze[r+1][c]=='.'):
                        pass
                    elif(maze[r+1][c]=='|' or maze[r+1][c]=='L' or maze[r+1][c]=='J'):
                        if((r+1,c) in visited):
                            pass
                        else:
                            queue.append([r+1,c])
                if(c-1>=0):
                    if(maze[r][c-1]=='.'):
                        pass
                    elif(maze[r][c-1]=='-' or maze[r][c-1]=='L' or maze[r][c-1]=='F'):
                        if((r,c-1) in visited):
                            pass
                        else:
                            queue.append([r,c-1])
                if(c+1<=len(maze[r])-1):
                    if(maze[r][c+1]=='.'):
                        pass
                    elif(maze[r][c+1]=='-' or maze[r][c+1]=='7' or maze[r][c+1]=='J'):
                        if((r,c+1) in visited):
                            pass
                        else:
                            queue.append([r,c+1])
            else:
                if(r-1>=0):
                    if(maze[r-1][c]=='.'):
                        pass
                    elif((maze[r-1][c]=='|' or maze[r-1][c]=='7' or maze[r-1][c]=='F' ) and (maze[r][c]=='|' or maze[r][c]=='J' or maze[r][c]=='L')):
                        if((r-1,c) in visited):
                            pass
                        else:
                            queue.append([r-1,c])
                if(r+1<=len(maze)-1):
                    if(maze[r+1][c]=='.'):
                        pass
                    elif((maze[r+1][c]=='|' or maze[r+1][c]=='L' or maze[r+1][c]=='J') and (maze[r][c]=='|' or maze[r][c]=='F' or maze[r][c]=='7')):
                        if((r+1,c) in visited):
                            pass
                        else:
                            queue.append([r+1,c])
                if(c-1>=0):
                    if(maze[r][c-1]=='.'):
                        pass
                    elif((maze[r][c-1]=='-' or maze[r][c-1]=='L' or maze[r][c-1]=='F') and (maze[r][c]=='-' or maze[r][c]=='J' or maze[r][c]=='7')):
                        if((r,c-1) in visited):
                            pass
                        else:
                            queue.append([r,c-1])
                if(c+1<=len(maze[r])-1):
                    if(maze[r][c+1]=='.'):
                        pass
                    elif((maze[r][c+1]=='-' or maze[r][c+1]=='J' or maze[r][c+1]=='7') and (maze[r][c]=='-' or maze[r][c]=='F' or maze[r][c]=='L')):
                        if((r,c+1) in visited):
                            pass
                        else:
                            queue.append([r,c+1])
            visited[(r,c)] = 1
        steps += 1
        for s in range(curr_len):
            queue.pop(0)
    return steps


print(steps_farthest("input.txt"))