# import csv
# import matplotlib.pyplot as plt
#
# f = open('weathers.csv',encoding='euc-kr')
# data = csv.reader(f)
# header=next(data)
# print(header)
#
# highest = 0
# date = ''
# dateList = []
# weatherList = []
#
# for x in data:
#     if(x[4] != '') :
#         dateList.append(x[0])
#         weatherList.append(x[4])
#         if(float(x[4]) > highest):
#             date = x[0]
#             highest = float(x[4])
#
#
# print(weatherList)
# print("서울에서 가장 높은 기온 {}C {}입니다.".format(highest,date))
# plt.plot(dateList, color="skyblue")
# plt.show()
# f.close()
#
# # for x in data:
# #     print(list(x))