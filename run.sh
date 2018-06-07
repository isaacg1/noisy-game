#!/bin/bash

time python3 noisy-game.py -b -f | tee reduced-results.txt &
time python3 noisy-game.py -f | tee results.txt
