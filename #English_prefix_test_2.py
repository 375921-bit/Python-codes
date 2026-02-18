#English_prefix_test_2

import math

score = 0

# Contra-
answer_1 = input("What does the prefix contra- mean?")
if answer_1 == ("Against"):
    print("Correct")
    score += 1
elif answer_1 != ("Against"):
    print("Incorrect")

# Demi-
answer_2 = input("What does the prefix demi- mean?")
if answer_2 == ("Half"):
    print("Correct")
    score += 1
elif answer_2 != ("Half"):
    print("Incorrect")

# Dia-
answer_3 = input("What does the prefix dia- mean?")
if answer_3 == ("Across") or ("Through") or ("Across/Through"):
    print("Correct")
    score += 1
elif answer_3 != ("Across") or ("Through") or ("Across/Through"):
    print("Incorrect")

# Dys-
answer_4 = input("What does the prefix dys- mean?")
if answer_4 == ("Bad"):
    print("Correct")
    score += 1
elif answer_4 != ("Bad"):
    print("Incorrect")

print("Your score out of 9:")
print(score)
print("")
print("Your grade:")
print(score/9*100)