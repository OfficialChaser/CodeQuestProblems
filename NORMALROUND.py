# NOTE: This is not a practice problem. It is a feature that allows normal rounding in python. 
# CodeQuest doesn't like the round() function

import math

def normal_round(n, decimals=0):
    expoN = n * 10 ** decimals
    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        return math.floor(expoN) / 10 ** decimals
    return math.ceil(expoN) / 10 ** decimals

# Example
num = normal_round((4/19), 3)
print(num)
# Prints = 0.211
num2 = normal_round((1/2))
print(num2)