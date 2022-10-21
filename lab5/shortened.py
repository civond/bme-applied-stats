import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.patches as mpatches
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

x=[];y=[];
s_pol = 10;s_non = 49;c_pol = 27;c_non = 32;

for i in range(0,s_pol):
    x.append('shortened')
    y.append('pollinated')
for i in range(0,s_non):
    x.append('shortened')
    y.append('not pollinated')
for i in range(0,c_pol):
    x.append('control')
    y.append('pollinated')
for i in range(0,c_non):
    x.append('control')
    y.append('not pollinated')

df = pd.DataFrame({'shortened': x, 'control': y})

s_pol_r = round(100*s_pol/(s_non+s_pol),1)
s_non_r = round(100*s_non/(s_non+s_pol),1)
c_pol_r = round(100*c_pol/(c_non+c_pol),1)
c_non_r = round(100*c_non/(c_non+c_pol),1)

print(s_pol_r)

props={}
props[('shortened','pollinated')]={'facecolor':'#ff8080', 'edgecolor':'white'}
props[('shortened','not pollinated')]={'facecolor':'#ff5050', 'edgecolor':'white'}
props[('control','pollinated')]={'facecolor':'#0099ff','edgecolor':'white'}
props[('control','not pollinated')]={'facecolor':'#66c2ff','edgecolor':'white'}

labelizer=lambda k:{('shortened','not pollinated'):str(s_non)+' ('+str(s_non_r)+'%)',
                    ('shortened','pollinated'):str(s_pol)+' ('+str(s_pol_r)+'%)',
                    ('control','not pollinated'):str(c_non)+' ('+str(c_non_r)+'%)',
                    ('control','pollinated'):str(c_pol)+' ('+str(c_pol_r)+'%)'}[k]

mosaic(df, ['shortened', 'control'],
       labelizer=labelizer,
       axes_label=False,
       properties=props)

p1 = mpatches.Patch(color='#ff8080', label='shortened, pollen')
p2 = mpatches.Patch(color='#ff5050', label='shortened, no pollen')
p3 = mpatches.Patch(color='#0099ff', label='control, pollen')
p4 = mpatches.Patch(color='#66c2ff', label='control, no pollen')

plt.title('Pollination of Disa draconis',
          fontweight="bold")

plt.legend(#bbox_to_anchor=(1.02, 1),
           borderaxespad=0,
           loc='upper right',
           handles=[p1,p2,p3,p4],
            shadow=True,
           prop = {'size' : 6})
plt.xlabel('Group')
plt.ylabel('Proportion')
plt.show()
#df.head()