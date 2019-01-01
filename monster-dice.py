#!/usr/bin/env python3
import random

red = ['hit', 'hit', 'hit', 'bra', 'run', 'run']
yellow = ['hit', 'hit', 'bra', 'bra', 'run', 'run']
green = ['hit', 'run', 'run', 'bra', 'bra', 'bra']
hero = ['hit', 'hit', 'run', 'run', '2hit', '2bra']
heroin = ['hit', 'hit', 'bra', 'run', 'run', 'run']
santa = ['hit', '2bra', 'helm', 'bra', 'ebar', 'run']



def turn(number):
    hits = 0
    bras = 0
    rolls = 0
    runs = 0
    ebar = 0
    old_roll = []
    bucket = [red, red, red, green, green, green, green, \
       green, green, yellow, yellow, yellow, hero, heroin, santa]

    while len(bucket) > 2 and hits < 3:
        current_roll = []
        sample_size = 3 - len(old_roll)
        print("#old roll: ", len(old_roll), " sample_size: ", sample_size)
        roll = random.sample(bucket, sample_size)
        for item in roll:
            bucket.remove(item)
        current_roll = roll + old_roll
        old_roll = []
        print("#current roll: ", current_roll)

        for dice in current_roll:
            dice_result = random.choice(dice)
            print("#dice: ",dice_result)
            if dice_result == 'hit':
                hits += 1
            if dice_result == '2hit':
                hits += 2
            if dice_result== 'run':
                runs += 1
                old_roll.append(dice)
            if dice_result == 'bra':
                bras += 1
            if dice_result == '2bra':
                bras += 2
            if dice_result == 'helm':
                bras -= 1
            if dice_result == 'ebar':
                ebar += 1

        rolls += 1
        print("#Number: ", number, " Rolls: ", rolls, " Hits: ", hits, " Brains: ", bras)
    return(number,rolls,hits,bras)

results = []

for x in range(1, 10000):
    results.append(turn(x))

for result in results:
    print(result)
