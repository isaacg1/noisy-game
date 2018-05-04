# noisy-game

The noisy iterated prisoner's dilemma is played as follows:

Each participant plays 100 rounds against each other player.
Each round works as follows:
* Choose a flip probability uniformly in [0, 0.5]
* Play for 300 moves

On each move, each participant knows:
* Their past (preflip) plays this round
* Their opponent's postflip plays this round.

Then, the participant chooses a play:
'c' for cooperate
'd' for defect

Then, the play is flipped with probability equal to the flip probability.
If the post-flip value is 'c',
the opponent gets 2 points.
If the post-flip value is 'd',
the player gets 1 point.

After all rounds have been played,
players will be scored according to simulated evolution.
Each player starts with an equal share of the population.
A player's share in the next round is proportional to
* The player's previous share
* The average score against all opponents (including the player itself), weighted by opponent's share.

The sum over shares over 100 evolution runs is the final result.

This system means that it's important to do well against opponents who do well.
