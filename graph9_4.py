import matplotlib.pyplot as plt
import csv
f = open('card.csv',encoding='utf8')
data = csv.reader(f)

def foodCheck(store):
    list = ["형제", "스타벅스", "이마트", "파리바게트"]
    for x in list:
        if(x in store):
            return True
# next(data)
# ['이용일시', '승인번호', '본인구분', '브랜드', '이용카드', '가맹점명', '이용금액', '이용구분', '매입상태']
taxi = [0,0,0]

foodlist = ["형제","스타벅스","이마트","파리바게트"]
delivery = [0,0,0]
data = list(data)
for x in data:
   if ("택시" in x[5]) and (x[-1] == "전표매입"):
       month = int(x[0].split('-')[1]) - 10
       taxi[month] += int(x[6])
   if (foodCheck(x[5])) and (x[-1] == "전표매입"):
       month = int(x[0].split('-')[1]) - 10
       delivery[month] += int(x[6])

print(delivery)
plt.rc('font', family='Malgun Gothic')
plt.title('10~12월 지출현황')
plt.plot(['10월','11월','12월'], delivery, color='crimson', label='음식 지출액')
plt.plot(['10월','11월','12월'], taxi, color='indigo', label='택시비 지출액')
plt.legend()
plt.show()



