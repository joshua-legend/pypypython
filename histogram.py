import csv
import matplotlib.pyplot as plt

f = open('weather1909.csv',encoding='euc-kr')
data = csv.reader(f)
next(data)
weatherList = []

for x in data:
    if(x[-1] != '') :
        if(x[0].split("-")[1] == '02'):
            weatherList.append(float(x[-1]))

plt.hist(weatherList, bins=500,color="red")
plt.show()
f.close()

