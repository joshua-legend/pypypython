import csv
import random

import matplotlib.pyplot as plt

singer = ['A','B','C','D','E']
week1=[]
week2=[]
for i in range(5):
    week1.append(random.randint(0, 100))
    week2.append(random.randint(0, 100))

plt.plot(singer,week1)
plt.plot(singer,week2)
plt.show()

