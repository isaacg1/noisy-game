import random

def cooperate(my_plays, their_flipped_plays):
    return 'c'

def defect(my_plays, their_flipped_plays):
    return 'd'

def random_player(my_plays, their_flipped_plays):
    if random.random() < 0.5:
        return 'c'
    else:
        return 'd'

def tit_for_tat(my_plays, their_flipped_plays):
    if not their_flipped_plays:
        return 'c'
    else:
        return their_flipped_plays[-1]

def threshold(my_plays, their_flipped_plays):
    if len(their_flipped_plays) < 10:
        return 'c'
    opp_c_freq = their_flipped_plays.count('c')/len(their_flipped_plays)
    if opp_c_freq > 0.6:
        return 'c'
    else:
        return 'd'

def exploit_threshold(my_plays, their_flipped_plays):
    if len(their_flipped_plays) < 10:
        return 'c'
    opp_c_freq = their_flipped_plays.count('c')/len(their_flipped_plays)
    if opp_c_freq > 0.6:
        if random.random() < opp_c_freq - 0.6:
            return 'd'
        else:
            return 'c'
    else:
        return 'd'

