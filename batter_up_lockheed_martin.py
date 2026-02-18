#batter_up_lockheed_martin

import math
import sys

score = 0

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

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
 problem_input = sys.stdin.readline().rstrip()
 input = problem_input.split(':') #separate by space
 first_argument = str(input[0]) #Moreland
 second_argument = (input[1]) #K,2b, 1b, hr
 print(first_argument,second_argument)


SLG = score/4
print(SLG)