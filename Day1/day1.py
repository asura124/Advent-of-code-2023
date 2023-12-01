
def calibration_sum(file):
    total = 0
    with open(file) as f:
        for line in f:
            curr_num = ""
            for c in range(len(line)):
                if((line[c]).isnumeric()):
                    curr_num = line[c] + curr_num
                    break
            for c in range(len(line)):
                if(line[-1-c].isnumeric()):
                    curr_num = curr_num + line[-1-c]
                    break
            total += int(curr_num)
    return total

def modified_calibration_sum(file):
    total = 0
    letters = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    with open(file) as f:
        for line in f:
            curr_num=""
            first_num=""
            last_num = ""
            first_pos = 99999
            last_pos = -99999
            for l in letters:
                if(line.find(l)<first_pos and line.find(l)!=-1):
                    first_num = letters[l]
                    first_pos = line.find(l)
                if(line.rfind(l)>last_pos and line.rfind(l)!=-1):
                    last_num = letters[l]
                    last_pos = line.rfind(l)
            for c in range(len(line)):
                if((line[c]).isnumeric()):
                    if(c<first_pos):
                        curr_num = line[c] + curr_num
                    else:
                        curr_num = str(first_num) + curr_num
                    break
            for c in range(len(line)):
                if(line[-1-c].isnumeric()):
                    if((len(line)-1-c)>last_pos):
                        curr_num = curr_num + line[-1-c]
                    else:
                        curr_num = curr_num + str(last_num)
                    break
            if(curr_num == ""): curr_num = str(first_num) + str(last_num)
            total += int(curr_num)
    return total

print(calibration_sum("input.txt"))
print(modified_calibration_sum("input.txt"))