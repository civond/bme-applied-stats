import pandas as pd
import numpy as np
import math
import statistics
from  itertools import  zip_longest
import scipy.stats as stats
from bioinfokit.analys import stat
import statsmodels.api as sm
from statsmodels.formula.api import ols

unbiased = [82.16, 62.16, 79.83, 82.33, 75.83, 127.33, 87.16, 74.16]
male_biased = [118 , 87 , 123 , 150 , 94 , 133 , 206 , 162 ,156]
female_biased = [80.16 , 6 , 53.17 , 121.34 , 69 , 57.82 , 62.16 , 66.5 ]

L = [unbiased,male_biased,female_biased]
iterables = (reversed(it) for it in L)
out = list(reversed(list(zip_longest(*iterables, fillvalue=np.nan))))

df = pd.DataFrame(out, columns=['Unbiased',
                                'Male-Bias',
                                'Fem-Bias'])
dftest =df.dropna()
fvalue, pvalue = stats.f_oneway(dftest['Unbiased'], dftest['Male-Bias'], dftest['Fem-Bias'])
print(fvalue, pvalue)


df_melt = pd.melt(df.reset_index(), id_vars=['index'],
                  value_vars=['Unbiased',
                              'Male-Bias',
                              'Fem-Bias'])


df_melt = df_melt.dropna().reset_index()
df_melt.drop(["level_0", "index"], axis = 1, inplace=True)
df_melt.columns=['treatment','value']
print(df_melt.head(25))

res = stat()
res.tukey_hsd(df=df_melt, res_var='value', xfac_var='treatment', anova_model='value ~ C(treatment)')
print(res.tukey_summary)



#Handwritten Portion----------
unb_mean = statistics.mean(unbiased)
unb_stdev = statistics.stdev(unbiased)
unb_count = len(unbiased)

male_mean = statistics.mean(male_biased)
male_stdev = statistics.stdev(male_biased)
male_count = len(male_biased)

fem_mean = statistics.mean(female_biased)
fem_stdev = statistics.stdev(female_biased)
fem_count = len(female_biased)

X_hat = (1/25)*(unb_count*unb_mean + male_count*male_mean + fem_count*fem_mean)
SS_groups = unb_count*(unb_mean-X_hat)**2 + male_count*(male_mean-X_hat)**2 + fem_count*(fem_mean-X_hat)**2
MS_Groups = SS_groups/2
print("X hat: " + str(X_hat))
print("SS Groups: " + str(SS_groups))
print("MS_Groups: " + str(MS_Groups))

SS_error = (unb_count-1)*unb_stdev**2 + (male_count-1)*male_stdev**2 + (fem_count-1)*fem_stdev**2
df_error = 25-3
MS_Error = SS_error/df_error
print("SS_Error: " + str(SS_error))
print("df error: " + str(df_error))
print("MS_Error: " + str(MS_Error))

F = MS_Groups/MS_Error
print("F: " + str(F))

data = {'Mean' : [unb_mean, male_mean, fem_mean],
      'Stdev' : [unb_stdev, male_stdev, fem_stdev],
      'Count' : [unb_count, male_count, fem_count]}

results = pd.DataFrame(data,
                  index= ['Unbiased',
                          'Male_Biased',
                          'Fem_Biased'])
print(results)

Q_st_error = math.sqrt(MS_Error*((1/2)+(1/22)))
print(Q_st_error)