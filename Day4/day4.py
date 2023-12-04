
def total_winning_points(file):
    total = 0
    with open(file) as f:
        for line in f:
            curr_winnings = 0
            line = line[line.find(':')+1::].lstrip().replace('  ',' ').strip('\n').split(' | ')
            winnings = {}
            win_nums = line[0].split(' ')
            for i in win_nums:
                if i not in winnings:
                    winnings[i] = 1
            for i in line[1].split(' '):
                if(i in winnings and curr_winnings==0):
                    curr_winnings = 1
                elif(i in winnings and curr_winnings !=0):
                    curr_winnings = curr_winnings * 2
            total += curr_winnings
    return total


def total_scratchcards(file):
    with open(file) as f:
        total_copies = {}
        scartchcards = 0
        for line in f:
            card = int(line[line.find("Card")+5:line.find(":")])
            if(card in total_copies):
                total_copies[card] += 1
            else:
                total_copies[card] = 1
            line = line[line.find(':')+1::].lstrip().replace('  ',' ').strip('\n').split(' | ')
            winnings = {}
            win_nums = line[0].split(' ')
            for i in win_nums:
                if(i not in winnings):
                    winnings[i] = 1
            count = 0
            for i in line[1].split(' '):
                if(i in winnings):
                    count += 1
            for s in range(card+1,card+count+1):
                if(s not in total_copies):
                    total_copies[s] = 1
                else:
                    total_copies[s] += total_copies[card]
        #print(total_copies)
        for i in total_copies:
            scartchcards += total_copies[i]
    return scartchcards

            


print(total_winning_points("input.txt"))
print(total_scratchcards("input.txt"))


