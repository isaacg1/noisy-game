#!/bin/bash

time python3 noisy-game.py -b | tee reduced-results.txt &
time python3 noisy-game.py | tee results.txt
