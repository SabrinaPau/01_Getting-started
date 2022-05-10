import random
import time
import sys
import ast
import os

random.seed(59)

# This code finds speed dating pairings combinations by brute force.
# Script takes list of names in a string cast as second argument
# and output option (list, 1 or overview, 2) as first argument
# e.g.: $ python speeddating.py 2 "['Sergio', 'Matthias', 'Andrew']"
# Uneven lists do get a 'Joker' added


# functions
def permutations(items):
    '''returns list of permutations of given list's elements'''
    pairs = [(items[i],items[j]) for i in range(len(items)) for j in range(i+1, len(items))]
    return pairs

def is_pair_in(candidates, pairs):
    '''Function takes tuple of candidates and checks if either is in each pair of provided list
        Arguments:
        candidates: tuple of candidates, eg. ('Name1', 'Name2')
        pairs: list of tuples of pairings, eg. [('Name1', 'Name2'), ('Name1', 'Name3'), ('Name1', 'Name4')]
        '''
    global found
    found = False
    for i in range(0, len(pairs)):
        if candidates[0] == pairs[i][0]:
            found = True
            break
        elif candidates[0] == pairs[i][1]:
            found = True
            break
        elif candidates[1] == pairs[i][0]:
            found = True
            break
        elif candidates[1] == pairs[i][1]:
            found = True
            break
        else:
            found = False

    return found

def gen_rounds(rounds, n_rounds, n_rooms, pairs):
    '''generates list of speed dating rounds containing unique pairings
       rounds = empty list to append rounds
       n_rounds = count of possible dating rounds
       n_rooms = count of possible parallel datings
       pairs = list of permutations
       '''
    while len(rounds) < n_rounds: # do the search for rounds as long as possible number of rooms is found
        actual_round = []
        i = 1
        while len(actual_round) < n_rooms and i <= 100: # trying a hundred times to fill the room wit unique people up to number of possible paralles speed datings 
            i += 1
            random.shuffle(pairs) # to make the pop.function pop a n arbitrary pair 
            candidates = pairs.pop()
            if is_pair_in(candidates, actual_round): # if one or both actual candidates to append to the round are already existing in round, move them back in pairings list 
                pairs.append(candidates)
            else:
                actual_round.append(candidates) # if candidates are not in actual round, append to actual round

        # if the search for unique combinations for the actual round
        # didn't led to the possible number of dates,
        # move all pairs of this actual round back to pairs list - to try again.
        if len(actual_round) == n_rooms:
            rounds.append(actual_round)
        else:
            pairs.extend(actual_round)

    return rounds

def add_joker(items):
    '''append 'Joker' string to name list in case of uneven count of elements - to allow group building'''
    if len(items) % 2 == 1:
        items.append('Joker')
    else:
        pass

    return items


# main script
# -----------

if __name__ == "__main__":

    # assign script parameter as list
    view = int(sys.argv[1])
    items = ast.literal_eval(sys.argv[2])

    # append 'Joker' to list in case of uneven count of elements - to allow group building
    items = add_joker(items)

    # make permutations from list of given names 
    pairs = permutations(items)

    # helper variables
    n_pairs = len(pairs) # number of possible pairings
    n_participants = len(items) # number of participating people
    n_rounds = n_participants - 1 # speed dating rounds
    n_rooms = n_participants / 2 # number of simultaneous speed datings per round
    rounds = [] # empts list of rounds to append to

    # generate list of rounds 
    rounds = gen_rounds(rounds, n_rounds, n_rooms, pairs)

    # clears screen
    os.system("clear")

    # final print of speed dating rounds
    if view == 2:
        c = 1
        print('Speed Dating Pairings:\n')
        for round in rounds:
            print(f'Round {str(c).zfill(2)}: ', round)
            time.sleep(.15) # sleep for .15 seconds
            c += 1
    elif view == 1:
        for round in rounds:
            for pair in round:
                print(pair)
            print('---')
    else:
        pass
