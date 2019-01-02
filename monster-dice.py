#!/usr/bin/env python3
import random
import pandas as pd

verbose = 0

red = ['hit', 'hit', 'hit', 'bra', 'run', 'run']
yellow = ['hit', 'hit', 'bra', 'bra', 'run', 'run']
green = ['hit', 'run', 'run', 'bra', 'bra', 'bra']
hero = ['hit', 'hit', 'run', 'run', '2hit', '2bra']
heroin = ['hit', 'hit', 'bra', 'run', 'run', 'run']
santa = ['hit', '2bra', 'helm', 'bra', 'ebar', 'run']



def turn(number,hit_stop,brain_stop):
    hits = 0
    bras = 0
    rolls = 0
    runs = 0
    ebar = 0
    old_roll = []
    bucket = [red, red, red, green, green, green, green, \
       green, green, yellow, yellow, yellow, hero, heroin, santa]

    while len(bucket) > 2 and hits < hit_stop:
        current_roll = []
        sample_size = 3 - len(old_roll)
        if verbose:
           print("#old roll: ", len(old_roll), " sample_size: ", sample_size)
        roll = random.sample(bucket, sample_size)
        for item in roll:
            bucket.remove(item)
        current_roll = roll + old_roll
        old_roll = []
        if verbose:
           print("#current roll: ", current_roll)

        for dice in current_roll:
            dice_result = random.choice(dice)
            if verbose:
                print("#dice: ",dice_result)
            if dice_result == 'hit':
                hits += 1
            if dice_result == '2hit':
                hits += 2
            if dice_result== 'run':
                runs += 1
                if ebar:
                   bras += 1 
                else:
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
        if verbose:
           print("#Number: ", number, " Rolls: ", rolls, " Hits: ", hits, " Brains: ", bras)
        if brain_stop and bras >= brain_stop:
           print("Hit the brain stop: ",brain_stop,bras)
           break
    return(number,rolls,hits,bras)


def scenario_xy(target_score):
    player1_score = 0
    player2_score = 0

    while player1_score < target_score and player2_score < target_score:
      p1_results=turn(1,2,0)
      if p1_results[2] < 3:
         player1_score += p1_results[3]

      p2_results=turn(1,2,8)
      if p2_results[2] < 3:
         player2_score += p2_results[3]

    print("Player1: ", player1_score, " Player2: ", player2_score)
    return(player1_score,player2_score)
      
p1_wins = 0
p2_wins = 0
ties = 0
for x in range(1,1000):
   p1,p2 = scenario_xy(20)
   if p1 > p2:
      p1_wins += 1
   if p2 > p1:
      p2_wins += 1
   if p1 == p2:
      ties +=1
print("Player1 wins: ", p1_wins, "Player2 wins: ", p2_wins, " Ties: ", ties)


#df = pd.DataFrame(results, columns=['number', 'rolls', 'hits', 'brains'])
#print(df.describe())
