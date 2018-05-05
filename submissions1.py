import random

def tit_for_whoops(m, t, s):
    if len(t) < 2:
        return 'c'
    else:
        return 'd' if all([x == 'd' for x in t[-2:]]) else 'c'


def growing_distrust(mine, theirs, state):
    # Start friendly.
    if len(mine) == 0:
        return 'c'

    # Be nice if we've already forgiven the opponent, and they're playing nice.
    if mine[-1] == 'c' and theirs[-1] == 'c':
        return 'c'

    # Get mad if we've been nice and they've been spiteful.
    betrayals = len([
        pair for pair in zip(mine, theirs[1:]) if pair == ('c', 'd')
    ])
    forgive_chance = 0.5 ** betrayals
    if random.random() < forgive_chance:
        return 'c'
    else:
        return 'd'
