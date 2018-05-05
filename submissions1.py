import random

def tit_for_whoops(m, t, s):
    if len(t) < 2:
        return 'c'
    else:
        return 'd' if all([x == 'd' for x in t[-2:]]) else 'c'

def growing_distrust(mine, theirs, state):
    # Start with trust.
    if len(mine) == 0:
        state.append(dict(betrayals=0, trust=True))
        return 'c'

    state_info = state[0]

    # If we're trusting and we get betrayed, trust less.
    if state_info['trust'] and theirs[-1] == 'd':
        state_info['trust'] = False
        state_info['betrayals'] += 1

    # Forgive, but don't forget.
    if random.random() < 0.5 ** state_info['betrayals']:
        state_info['trust'] = True

    return 'c' if state_info['trust'] else 'd'
