# noisy-game

The noisy iterated prisoner's dilemma is played as follows:

Each participant plays 100 rounds against each other player.
Each round works as follows:
* Choose a flip probability uniformly in [0, 0.5]
* Play for 300 moves

On each move, each participant knows:
* Their past plays this round
* Their opponent's plays this round, subject to noise. Each opponent's past play in list is wrong with probability equal to the flip probability.

Then, the participant chooses a play:
'c' for cooperate
'd' for defect

If they choose 'c',
the opponent gets 2 points.
If choose 'd',
the player gets 1 point.

After all rounds have been played,
each player has a raw score. However, this score weights success against opponents that do well and opponents that do poorly equally.

In this challenge, it is more important to succeed against opponents who do well.

Players will be scored according to simulated evolution.

Each player starts with an equal share of the population.
A player's share in the next round is proportional to
* The player's previous share
* The average score against all opponents (including the player itself), weighted by opponent's share.

After 100 evolution iterations, the player's share of the population is its final score for this run.

The overall score will be the sum of final scores over 100 runs.

This system means that it's important to do well against opponents who do well.
