


def total_winnings(file):
    hands = []
    bid = {}
    suits = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    with open(file) as f:
        for line in f:
            line = line.strip('\n').split(' ')
            bid[line[0]] = int(line[1])
            hands.append(line[0])
    #print(hands)
    for i in range(len(hands)):
        for j in range(len(hands)-i-1):
            hand_one = get_hand_type(hands[j])
            hand_two = get_hand_type(hands[j+1])
            if(hand_one>hand_two):
                hands[j],hands[j+1] = hands[j+1], hands[j]
            elif(hand_one==hand_two):
                for p in range(5):
                    if(suits.index(hands[j][p])<suits.index(hands[j+1][p])):
                        hands[j],hands[j+1] = hands[j+1], hands[j]
                        break
                    elif(suits.index(hands[j][p])==suits.index(hands[j+1][p])):
                        continue
                    else:
                        break
    total = 0
    for i in range(len(hands)):
        total = total + (bid[hands[i]] * (i+1))
    return total




def get_hand_type(hand):
    unique = list(set(hand))
    if(len(unique)==len(hand)): #all cards are different
        return 1
    elif(len(unique)==1): #all cards are the same -> 5 of a kind
        return 7
    elif(len(unique)==4) : #1 cards are the same and 3 are different -> 1 pair
        return 2
    occur = []
    for i in unique:
        occur.append(hand.count(i))
    if(4 in occur): #there were 4 of a kind
        return 6
    elif(3 in occur and 2 in occur): #full house
        return 5
    elif(3 in occur):
        return 4
    else:
        return 3


def joker_total_winnings(file):
    hands = []
    bid = {}
    suits = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
    with open(file) as f:
        for line in f:
            line = line.strip('\n').split(' ')
            bid[line[0]] = int(line[1])
            hands.append(line[0])
    for i in range(len(hands)):
        for j in range(len(hands)-i-1):
            hand_one = get_joker_hand_type(hands[j])
            hand_two = get_joker_hand_type(hands[j+1])
            if(hand_one>hand_two):
                hands[j],hands[j+1] = hands[j+1], hands[j]
            elif(hand_one==hand_two):
                for p in range(5):
                    if(suits.index(hands[j][p])<suits.index(hands[j+1][p])):
                        hands[j],hands[j+1] = hands[j+1], hands[j]
                        break
                    elif(suits.index(hands[j][p])==suits.index(hands[j+1][p])):
                        continue
                    else:
                        break
    total = 0
    for i in range(len(hands)):
        total = total + (bid[hands[i]] * (i+1))
    return total



def get_joker_hand_type(hand):
    occur = {}
    for i in hand:
        if(i not in occur):
            occur[i] = 1
        else:
            occur[i] +=1
    jack_occur = 0
    num_pair_occur = 0
    num_triplet_occur = 0
    num_quad_occur = 0
    no_match_occur = 0
    for i in occur:
        if(occur[i]==5):
            return 7
        elif(i != 'J'):
            if(occur[i]==4):
                num_quad_occur +=1
            elif(occur[i]==3):
                num_triplet_occur +=1
            elif(occur[i]==2):
                num_pair_occur +=1
            else:
                no_match_occur +=1
        else:
            jack_occur = occur[i]
    if(num_quad_occur==1 and jack_occur==1):
        return 7
    elif(num_quad_occur>0 and jack_occur==0):
        return 6
    elif(num_triplet_occur==1 and num_pair_occur==1):
        return 5
    elif(num_triplet_occur==1 and jack_occur>0):
        return 5+jack_occur
    elif(num_triplet_occur==1 and no_match_occur>0):
        return 4
    elif(num_pair_occur==2 and jack_occur==0):
        return 3
    elif(num_pair_occur==2 and jack_occur>0):
        return 5
    elif(num_pair_occur==1 and jack_occur==0):
        return 2
    elif(num_pair_occur==1 and jack_occur==1):
        return 4
    elif(num_pair_occur==1 and jack_occur==2):
        return 6
    elif(num_pair_occur==1 and jack_occur==3):
        return 7
    elif(no_match_occur==5 and jack_occur==0):
        return 1
    elif(no_match_occur==4 and jack_occur==1):
        return 2
    elif(no_match_occur==3 and jack_occur==2):
        return 4
    elif(no_match_occur==2 and jack_occur==3):
        return 6
    else:
        return 7


    
print(total_winnings('input.txt'))
print(joker_total_winnings("input.txt"))