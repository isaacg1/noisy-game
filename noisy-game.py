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
                p1_state = []
                p2_plays = []
                p2_flipped = []
                p2_state = []
                for _ in range(PLAYS):
                    p1_play = p1(p1_plays, p2_flipped, p1_state)
                    p2_play = p2(p2_plays, p1_flipped, p2_state)
                    p1_flip = flip(flip_prob, p1_play)
                    p2_flip = flip(flip_prob, p2_play)
                    if p1_play == 'c':
                        p2_score += 2
                    else:
                        p1_score += 1
                    if p2_play == 'c':
                        p1_score += 2
                    else:
                        p2_score += 1
                    p1_plays.append(p1_play)
                    p1_flipped.append(p1_flip)
                    p2_plays.append(p2_play)
                    p2_flipped.append(p2_flip)
            # Overwrite if i = j is intentional
            results[i][j] = p1_score
            results[j][i] = p2_score
    return results

EVOLUTIONS = 100
EVOLUTION_STEPS = 100
def evolutions(results):
    num_players = len(results)
    scores = [0 for _ in range(num_players)]
    for _ in range(EVOLUTIONS):
        weights = [1/num_players for _ in range(num_players)]
        for _ in range(EVOLUTION_STEPS):
            new_weights = []
            for i in range(num_players):
                old_weight = weights[i]
                average_score = sum(weight * result for weight, result in zip(weights, results[i]))
                new_weights.append(old_weight * average_score)
            normalizer = sum(new_weights)
            weights = [new_weight/normalizer for new_weight in new_weights]
        for i in range(num_players):
            scores[i] += weights[i]
    return scores

if __name__ == '__main__':
    from basic import cooperate, defect, random_player, tit_for_tat, threshold, exploit_threshold
    from submissions1 import tit_for_whoops, growing_distrust
    players = [cooperate, defect, random_player, 
            tit_for_whoops, growing_distrust]
    results = score(players)
    final_results = evolutions(results)
    for player, final in sorted(zip(players, final_results), key=lambda p:-p[1]):
        print("{}: {:.6}".format(player.__name__, final))
