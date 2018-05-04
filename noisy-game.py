import random

def flip(flip_prob, play):
    assert play == 'c' or play == 'd'
    if random.random() < flip_prob:
        if play == 'c':
            return 'd'
        else:
            return 'c'
    else:
        return play

ROUNDS = 100
PLAYS = 300
# results[i][j] = i's score against j.
def score(players):
    random.seed(0)
    results = [[0 for _ in range(len(players))] for _ in range(len(players))]
    for i in range(len(players)):
        for j in range(i+1):
            p1 = players[i]
            p2 = players[j]
            p1_score = 0
            p2_score = 0
            for _ in range(ROUNDS):
                flip_prob = random.uniform(0, 0.5)
                p1_plays = []
                p1_flipped = []
                p2_plays = []
                p2_flipped = []
                for _ in range(PLAYS):
                    p1_play = p1(p1_plays, p2_flipped)
                    p2_play = p2(p2_plays, p1_flipped)
                    p1_flip = flip(flip_prob, p1_play)
                    p2_flip = flip(flip_prob, p2_play)
                    if p1_flip == 'c':
                        p2_score += 2
                    else:
                        p1_score += 1
                    if p2_flip == 'c':
                        p1_score += 2
                    else:
                        p2_score += 1
                    p1_plays.append(p1_play)
                    p1_flipped.append(p1_flip)
                    p2_plays.append(p2_play)
                    p2_flipped.append(p2_flip)
            # OVerwrite if i = j is intentional
            print(p1_score, p1.__name__, p2_score, p2.__name__)
            results[i][j] = p1_score
            results[j][i] = p2_score
    return results

def evolutions(results):
    assert False

if __name__ == '__main__':
    from basic import cooperate, defect, random_player
    players = [cooperate, defect, random_player]
    results = score(players)
    print(results)
    final_results = evolutions(results)
    for player, final in zip(players, final_results):
        print(player.name, final)
