

def sum_length_galaxies(file):
    galaxy = []
    gal = []
    pair_gals = {}
    total = 0
    empty_row = ['.'] * len(galaxy)
    count = 0
    with open(file) as f:
        for line in f:
            galaxy.append(list(line.strip('\n')))
    row = list(range(len(galaxy)))
    col = list(range(len(galaxy[0])))
    for i in range(len(galaxy)):
        for j in range(len(galaxy[i])):
            if(galaxy[i][j]=='#'):
                if(i in row):
                    row.remove(i)
                if(j in col):
                    col.remove(j)
    for i in row:
        galaxy.insert(i+count,empty_row.copy())
        count +=1
    for i in range(len(galaxy)):
        count = 0
        for j in col:
            galaxy[i].insert(j+count,'.')
            count +=1
    for i in range(len(galaxy)):
        for j in range(len(galaxy[i])):
            if(galaxy[i][j]=='#'):
                gal.append([i,j])
    for g1 in gal:
        for g2 in gal:
            if(g1==g2 or (tuple(g1),tuple(g2)) in pair_gals or (tuple(g2),tuple(g1)) in pair_gals):
                continue
            total += (abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]))
            #total += get_shortest_dist(galaxy,g1,g2) #the long way 
            pair_gals[(tuple(g1),tuple(g2))] = 1
    return total


def print_gal(arr):
    for i in range(len(arr)):
        print(arr[i])

def get_shortest_dist(arr,cor1,cor2):
    queue = [cor1]
    visited = {}
    steps = 0
    while(len(queue)!=0):
        curr_len = len(queue)
        for i in range(curr_len):
            row = queue[i][0]
            col = queue[i][1]
            if(row==cor2[0] and col==cor2[1]):
                return steps
            if((row,col) in visited):
                continue
            visited[(row,col)] = 1
            if(row+1<=len(arr)-1):
                queue.append([row+1,col])
            if(col-1>=0):
                queue.append([row,col-1])
            if(col+1<=len(arr[0])-1):
                queue.append([row,col+1])
        steps +=1
        for i in range(curr_len):
            queue.pop(0)


def sum_length_million_galaxies(file):
    galaxy = []
    gal = []
    pair_gals = {}
    total = 0
    with open(file) as f:
        for line in f:
            galaxy.append(list(line.strip('\n')))
    row = list(range(len(galaxy)))
    col = list(range(len(galaxy[0])))
    for i in range(len(galaxy)):
        for j in range(len(galaxy[i])):
            if(galaxy[i][j]=='#'):
                if(i in row):
                    row.remove(i)
                if(j in col):
                    col.remove(j)
    for i in range(len(galaxy)):
        for j in range(len(galaxy[i])):
            if(galaxy[i][j]=='#'):
                curr_row = i
                curr_col = j
                for r in row:
                    count = 0
                    if(i>r):
                        curr_row += 999999
                for c in col:
                    if(j>c):
                        curr_col += 999999
                gal.append([curr_row,curr_col])
    for g1 in gal:
        for g2 in gal:
            if(g1==g2 or (tuple(g1),tuple(g2)) in pair_gals or (tuple(g2),tuple(g1)) in pair_gals):
                continue
            total += (abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]))
            pair_gals[(tuple(g1),tuple(g2))] = 1
    return total



print(sum_length_galaxies("input.txt"))
print(sum_length_million_galaxies("input.txt"))