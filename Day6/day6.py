
def possibilities_product(file):
    arr = []
    with open(file) as f:
        for line in f:
            line = line[line.find(':')+1::].strip(' ')
            line = ' '.join(line.split()).split(' ') #cleans up the multiple whitespaces
            arr.append(line)
    product = 1
    index_count = 0
    for i in arr[0]:
        times_exceed = 0
        for j in range(int(i)):
            time_left = int(i)- j
            if(time_left*j>int(arr[1][index_count])):
                times_exceed +=1
        if(times_exceed>0):
            product = product * times_exceed
        index_count += 1
    return product


def updated_possibilities_product(file):
    arr = []
    with open(file) as f:
        for line in f:
            line = line[line.find(':')+1::].replace(' ','').strip('\n')
            arr.append(int(line))
    times_exceeded = 0
    for i in range(arr[0]):
        time_left = arr[0] - i
        if(time_left*i> arr[1] ):
            times_exceeded +=1
    return times_exceeded
            

print(possibilities_product("input.txt"))
print(updated_possibilities_product("input.txt"))