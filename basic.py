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

