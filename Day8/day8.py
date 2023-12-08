import math

def total_steps(file):
    directions = ""
    got_directions = False
    destinations = {}
    with open(file) as f:
        for line in f:
            if(not got_directions):
                directions = line.strip('\n')
                got_directions = True
            elif(line == '\n'):
                continue
            else:
                destinations[line[0:line.find('=')-1]] = line[line.find('=')+2::].replace('(','').replace(')','').strip('\n').split(', ')
    curr_destination = 'AAA'
    count = 0
    steps = 0
    while(curr_destination!='ZZZ'):
        if(count>len(directions)-1):
            count = 0
        if(directions[count]=='L'):
            curr_destination = destinations[curr_destination][0]
        else:
            curr_destination = destinations[curr_destination][1]
        count +=1
        steps +=1
    return steps


def total_steps_ending_with_z(file):
    directions = ""
    got_directions = False
    destinations = {}
    ending_with_a = []
    with open(file) as f:
        for line in f:
            if(not got_directions):
                directions = line.strip('\n')
                got_directions = True
            elif(line == '\n'):
                continue
            else:
                destinations[line[0:line.find('=')-1]] = line[line.find('=')+2::].replace('(','').replace(')','').strip('\n').split(', ')
                temp = line[0:line.find('=')-1]
                if(temp[-1]=='A'):
                    ending_with_a.append(temp)
    end_steps = []
    for i in range(len(ending_with_a)):
        count = 0
        steps = 0
        check_end_z = False
        while(not check_end_z):
            if(count>len(directions)-1):
                    count = 0
            if(directions[count]=='L'):
                ending_with_a[i] = destinations[ending_with_a[i]][0]
            else:
                ending_with_a[i] = destinations[ending_with_a[i]][1]
            count +=1
            steps +=1
            if(ending_with_a[i][2]=='Z'):
                check_end_z = True
        end_steps.append(steps)
    LCM = 1
    for i in end_steps:
        LCM = math.lcm(LCM,i)
    return LCM



print(total_steps("input.txt"))
print(total_steps_ending_with_z("input.txt"))