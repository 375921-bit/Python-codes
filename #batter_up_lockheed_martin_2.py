#batter_up_lockheed_martin_2

import math

score = 0

player = input("Insert a player:")
stats = input("Write in the stats(out, single, double, triple, HR):")

# scoring
out = 0
single = 1
double = 2
triple = 3
HR = 4

# update scoring
if out:
 score += 0
if single:
 score += 1
if double:
 score += 2
if triple:
 score += 3
if HR:
 score += 4

SLG = score/4

print(player + " has " + SLG + "%")
