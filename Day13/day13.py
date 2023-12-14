

def sum_sumarizes(file):
    total = 0
    with open(file) as f:
        arr = []
        for line in f:
            if(line=='\n'):
                total += (100*horizontal_value(arr)) + (vertical_value(arr))
                arr = []
            else:
                arr.append(list(line.strip('\n')))
    return total

def horizontal_value(arr):
    reflection = True
    for i in range(len(arr)-1):
        if(arr[i]==arr[i+1]):
            up = i
            down = i+1
            while(down<len(arr) and up>=0):
                if(arr[up]==arr[down]):
                    pass
                else:
                    reflection = False
                up-= 1
                down+= 1
            if(reflection):
                return i+1
            reflection = True
    return 0 

def vertical_value(arr):
    arr = [list(i) for i in zip(*arr)] #transpose the array
    reflection = True
    for i in range(len(arr)-1):
        if(arr[i]==arr[i+1]):
            up = i
            down = i+1
            while(down<len(arr) and up>=0):
                if(arr[up]==arr[down]):
                    pass
                else:
                    reflection = False
                up-= 1
                down+= 1
            if(reflection):
                return i+1
            reflection = True
    return 0


print(sum_sumarizes("input.txt"))
