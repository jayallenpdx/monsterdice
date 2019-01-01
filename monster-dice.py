#!/usr/bin/env python3
import random

red = ['hit', 'hit', 'hit', 'bra', 'run', 'run']
yellow = ['hit', 'hit', 'bra', 'bra', 'run', 'run']
green = ['hit', 'run', 'run', 'bra', 'bra', 'bra']
hero = ['hit', 'hit', 'run', 'run', '2hit', '2bra']
heroin = ['hit', 'hit', 'bra', 'run', 'run', 'run']
santa = ['hit', '2bra', 'helm', 'bra', 'ebar', 'run']

bucket = [red, red, red, green, green, green, green, \
       green, green, yellow, yellow, yellow, hero, heroin, santa]

hits = 0
bras = 0
rolls = 0
runs = 0
ebar = 0
old_roll = []

while len(bucket) > 2 and hits < 3:
    current_roll = []
    sample_size = 3 - len(old_roll)
    roll = random.sample(bucket, sample_size)
    current_roll = roll + old_roll
    print("current roll: ", current_roll)

    for dice in current_roll:
        dice_result = random.choice(dice)
        if dice_result == 'hit':
            hits += 1
            bucket.remove(dice)
        if dice_result == '2hit':
            hits += 2
            bucket.remove(dice)
        if dice_result== 'run':
            runs += 1
            old_roll.append(dice)
            bucket.remove(dice)
        if dice_result == 'bra':
            bras += 1
            bucket.remove(dice)
        if dice_result == '2bra':
            bras += 2
            bucket.remove(dice)
        if dice_result == 'helm':
            bras -= 1
            bucket.remove(dice)
        if dice_result == 'ebar':
            ebar += 1
            bucket.remove(dice)

    rolls += 1
    print("Rolls: ", rolls, " Hits: ", hits, " Brains: ", bras)
