import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Optional-Assignment/fifa_data.csv")

labels = '40-60', '20-40', '-20', '60-80', '80-100', '+100'
sizes = [len([x for x in df['Value'].values if len(x) < 2 or x.__contains__('K') or (len(x)>2 and float(x[1:len(x)-1]) <= 20)]),
         len([x for x in df['Value'].values if len(x)>2 and float(x[1:len(x)-1]) > 20 and float(x[1:len(x)-1]) <= 40]),
         len([x for x in df['Value'].values if len(x)>2 and float(x[1:len(x)-1]) > 40 and float(x[1:len(x)-1]) <= 60]),
         len([x for x in df['Value'].values if len(x)>2 and float(x[1:len(x)-1]) > 60 and float(x[1:len(x)-1]) <= 80]),
         len([x for x in df['Value'].values if len(x)>2 and float(x[1:len(x)-1]) > 80 and float(x[1:len(x)-1]) <= 100]),
         len([x for x in df['Value'].values if len(x)>2 and not x.__contains__('K') and float(x[1:len(x)-1]) > 100])]
sizes[0], sizes[2] = sizes[2], sizes[0]
explode = (0, 0.5, 0, 0.6, 0, 0.7)
print(sizes)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%.2f%%', startangle=90, labeldistance=1.0)
ax1.axis('square')

plt.title('Value Pie Chart\nDevided by 20M$', bbox={'facecolor':'0.5', 'pad':1}, x=0, y=0.9)
plt.legend()
plt.show()