import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/doria/OneDrive/Desktop/Storage/School/AppliedStatistics/bme-applied-stats/lab8/Data/chap13q20StressAndIncompatibleMates.csv')
print(df.head())

plt.hist(df['corticosterone_concentration_compatible'],
         alpha=0.5,
         bins=25,
         color='cyan',
         width=1.5,
         edgecolor='black')

plt.hist(df['corticosterone_concentration_incompatible'],
         alpha=0.5,
         bins=25,
         color='red',
         width=1.5,
         edgecolor='black')

plt.title('Blood Corticosterone Concentration',
          fontsize=20)
plt.xlabel('Blood Corticosterone (ng/mL)',
           fontsize=14)
plt.ylabel('Frequency',
           fontsize=14)
plt.legend(['Compatible','Incompatible'])

#Question 2
accidental = ['110:acc','117:acc','133:acc','135:acc','140:acc','168:acc','171:acc','238:acc','255:acc']
infanticide = ['211:infant','232:infant','246:infant','251:infant','275:infant']
joined = accidental+infanticide

joined.sort(reverse=False)

rank=0
temp = []

while rank in range(0,len(joined)):
    temp.append(joined[rank]+':'+str(rank+1))
    rank+=1

acc = 0
infant = 0

for item in temp:
    split = item.split(':')
    if split[1] == 'acc':
        acc+= int(split[2])
    else:
        infant += int(split[2])
print('Accidental rank  sum: '+str(acc))
print('Infanticide rank sum: ' + str(infant))
