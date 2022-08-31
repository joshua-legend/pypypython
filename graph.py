import csv
import random

import matplotlib.pyplot as plt

weight,height=[],[]

for i in range(100):
    weight.append(random.randint(100,200))
    height.append(random.randint(20,100))

plt.rc('font', family="Malgun Gothic")
plt.scatter(weight, height, s=weight,c=weight, cmap='rainbow')
plt.xlabel("키")
plt.ylabel("몸무게")
plt.colorbar(label="키")
plt.show()
#