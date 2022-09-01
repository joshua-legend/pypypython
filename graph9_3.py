import matplotlib.pyplot as plt
import csv
f = open('card.csv',encoding='utf8')
data = csv.reader(f)
# next(data)
# ['이용일시', '승인번호', '본인구분', '브랜드', '이용카드', '가맹점명', '이용금액', '이용구분', '매입상태']
taxi = [0,0,0]

data = list(data)
for x in data:
   if ("택시" in x[5]) and (x[-1] == "전표매입"):
       month = int(x[0].split('-')[1]) - 10
       taxi[month] += int(x[6])

print(taxi)