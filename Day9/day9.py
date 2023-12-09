
def sum_extrapolated(file):
    total = 0
    with open(file) as f:
        for line in f:
            line = line.strip('\n').split(' ')
            line = [int(x) for x in line]
            total += (get_extrapolated(line) + line[-1])
    return total

def get_extrapolated(arr):
    diff_arr = []
    if(arr.count(0)==len(arr)):
        return 0
    for i in range(len(arr)-1):
        diff_arr.append(arr[i+1]-arr[i])
    return diff_arr[-1] + get_extrapolated(diff_arr)


def sum_extrapolated_backwards(file):
    total = 0
    with open(file) as f:
        for line in f:
            line = line.strip('\n').split(' ')
            line = [int(x) for x in line]
            total += (line[0] - get_extrapolated_backwards(line))
    return total

def get_extrapolated_backwards(arr):
    diff_arr = []
    if(arr.count(0)==len(arr)):
        return 0
    for i in range(len(arr)-1):
        diff_arr.append(arr[i+1]-arr[i])
    return diff_arr[0] - get_extrapolated_backwards(diff_arr)


print(sum_extrapolated("input.txt"))
print(sum_extrapolated_backwards("input.txt"))