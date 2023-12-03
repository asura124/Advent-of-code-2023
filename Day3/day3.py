

def sum_part_num(file):
    arr = []
    total = 0
    with open(file) as f:
        for line in f:
            temp = []
            for l in line:
                temp.append(l)
            arr.append(temp)
    start_index = [-1,-1]
    end_index = [-1,-1]
    curr_num = ""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j].isnumeric() and start_index==[-1,-1]):
                start_index = [i,j]
                curr_num += arr[i][j]
            elif(arr[i][j].isnumeric() and start_index!=[-1,-1]):
                curr_num += arr[i][j]
            elif(not arr[i][j].isnumeric() and start_index!=[-1,-1]):
                end_index = [i,j-1]
                if(check_adj(arr,start_index,end_index,int(curr_num))):
                    total += int(curr_num)
                start_index = [-1,-1]
                end_index = [-1,-1]
                curr_num = ""
    return total

def check_adj(arr,start_index,end_index,curr_num):
    for i in range(start_index[0]-1,end_index[0]+2):
        for j in range(start_index[1]-1,end_index[1]+2):
            if(i>=0 and i < len(arr)-1 and j>=0 and j<len(arr[i])-1):
                if(not arr[i][j].isnumeric() and arr[i][j]!='.'):
                    return True
    return False


def sum_gear_part(file):
    arr = []
    total = 0
    with open(file) as f:
        for line in f:
            temp = []
            for l in line:
                temp.append(l)
            arr.append(temp)
    start_index = [-1,-1]
    end_index = [-1,-1]
    curr_num = ""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j]=='*'):
                gear = get_gear_nums(arr,i,j)
                if(len(gear)==2):
                    total = total + (int(gear[0])*int(gear[1]))
    return total


def get_gear_nums(arr,start,end):
    check = {}
    our_gears = []
    for i in range(start-1,start+2):
        for j in range(end-1,end+2):
            if(i>=0 and i < len(arr) and j>=0 and j<len(arr[i])):
                if(arr[i][j].isnumeric() and (i,j) not in check):
                    check[(i,j)] = 1
                    curr_num = arr[i][j]
                    for c in range(1,j+1):
                        if(arr[i][j-c].isnumeric()):
                            curr_num = arr[i][j-c] + curr_num
                            check[(i,j-c)] = 1
                        else:
                            break
                    for c in range(1,len(arr[i])-j):
                        if(arr[i][j+c].isnumeric()):
                            curr_num = curr_num + arr[i][j+c]
                            check[(i,j+c)] = 1
                        else:
                            break
                    our_gears.append(curr_num)
    return our_gears




print(sum_part_num("input.txt"))
print(sum_gear_part("input.txt"))

