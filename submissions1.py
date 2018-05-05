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

def stubborn_stumbler(m, t, s):
    if not t:
        s.append(dict(last_2=[], last_3=[]))
    if len(t) < 5:
        return 'c'
    else:
        # Records history to state depending if the last two and three
        # plays were equal
        s = s[0]
        if t[-2:].count(t[-1]) == 2:
            s['last_2'].append(t[-1])
        if t[-3:].count(t[-1]) == 3:
            s['last_3'].append(t[-1])
    c_freq = t.count('c')/len(t)
    # Checks if you've consistently defected against me
    opp_def_3 = s['last_3'].count('d') > s['last_3'].count('c')
    opp_def_2 = s['last_2'].count('d') > s['last_2'].count('c')
    # You've wronged me too much
    if opp_def_3 and opp_def_2:
        return 'd'
    # If we're not sure, employ random chance, biased towards niceness
    elif opp_def_2:
        return 'c' if random.random() > 0.25 else 'd'
    # Otherwise, if you're consistently co-operating, co-operate more
    # the less naive you are
    else:
        return 'c' if random.random() > c_freq - 0.5 else 'd'

def slider(m, t, s):
    z = [[0, 1], [0, 2], [1, 3], [2, 3]]
    x = 0
    for y in t:
      x = z[x][y == 'c']
    return 'd' if x < 2 else 'c'
