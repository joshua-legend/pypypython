import csv
import random

import matplotlib.pyplot as plt

dice = []
for i in range(110):
    dice.append(random.randint(1,6))
plt.hist(dice,bins=61)
plt.show()