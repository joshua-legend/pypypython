import matplotlib.pyplot as plt
import csv
f = open('card.csv',encoding='utf8')
data = csv.reader(f)
next(data)
data = list(data)

spending = {}

for row in data:
    if(row[-1] == '전표매입'):
        store, payment = row[-4],row[-3]
        if store not in spending.keys():
            spending[store] = int(payment)
        else:
            spending[store] += int(payment)

# storeList = list(spending.keys())
# payList = list(spending.values())
#
# print(storeList)
# print(payList)
plt.rc('font', family='Malgun Gothic')
plt.title('10~12월 지출현황')
plt.barh(storeList,payList,color='indigo')
plt.show()