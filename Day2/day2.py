

def ID_sum(file):
    with open(file) as f:
        bag = {'red':12,'green':13,'blue':14}
        total = 0
        for line in f:
            curr_game = line[0:line.find(':')].replace('Game ','')
            each_game_set = line[line.find(':')+1::].replace('\n','').split(';')
            possible = True
            for game in each_game_set:
                game = game.split(',')
                for g in game:
                    g = g.lstrip().split(' ')
                    if(bag[g[1]]<int(g[0])):
                        possible = False
            if(possible):
                total += int(curr_game)
    return total

def sum_power_set(file):
    total = 0
    with open(file) as f:
        for line in f:
            colors = {'red':0,'green':0,'blue':0}
            each_game = line[line.find(':')+1::].replace('\n','').lstrip().replace(';',',').split(',')
            for g in each_game:
                g = g.lstrip().split(' ')
                if(colors[g[1]]<int(g[0])):
                    colors[g[1]] = int(g[0])
            product = 1
            for c in colors:
                product = product * colors[c]
            total += product
    return total


print(ID_sum("input.txt"))
print(sum_power_set("input.txt"))