import csv
import matplotlib.pyplot as plt

f = open('weather1909.csv',encoding='euc-kr')
data = csv.reader(f)
next(data)
weatherList = []

for x in data:
    if(x[-1] != '') :
        if(x[0].split("-")[1] == '02' and x[0].split("-")[2] == '14' ):
            weatherList.append(float(x[-1]))

print(weatherList)
plt.plot(weatherList, color="skyblue")
plt.show()
f.close()

