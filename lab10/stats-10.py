import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression
from scipy import stats
import numpy as np
from sklearn.metrics import r2_score

df = pd.read_csv("C:/Users/doria/OneDrive/Desktop/Storage/School/AppliedStatistics/bme-applied-stats/lab10/Data/chap16q15LanguageGreyMatter.csv")
plt.scatter(df.proficiency,
            df.greymatter,
            s=15)

plt.title("Language Proficiency vs Grey Matter",
          fontsize=15)
plt.xlabel("Second Language Proficiency Score")
plt.ylabel("Gray Matter Density (mm^3/voxel)")

#plt.show()
print(df.corr(method ='pearson'))

def calculate_pvalues(df):
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            tmp = df[df[r].notnull() & df[c].notnull()]
            pvalues[r][c] = pearsonr(tmp[r], tmp[c])[1]
    return pvalues
print(calculate_pvalues(df))
plt.clf()

#Question 2
df2 = pd.read_csv("C:/Users/doria/OneDrive/Desktop/Storage/School/AppliedStatistics/bme-applied-stats/lab10/Data/chap16q23ChocolateAndNobel.csv")
plt.scatter(df2.chocolateConsumption,
            df2.nobelPrizes,
            s=15)

plt.title("Chocolate Consumption vs Nobel Prizes",
          fontsize=15)
plt.xlabel("Chocolate Consumption")
plt.ylabel("Nobel Prizes (per 100 million)")

coef, p=spearmanr(df2.chocolateConsumption,df2.nobelPrizes)
print("Spearman's P: " + str(coef))
print("P value: " + str(p))
#print(df2.corr(method ='pearson'))
plt.show()
#plt.clf()


#Question 3
df3 = pd.read_csv("C:/Users/doria/OneDrive/Desktop/Storage/School/AppliedStatistics/bme-applied-stats/lab10/Data/chap17q20GrasslandNutrientsPlantSpecies.csv")
plt.scatter(df3.nutrients,
            df3.species,
            s=15,
            color="orange")

nutrients = df3['nutrients'].to_list()
species = df3['species'].to_list()


model = LinearRegression()
corr_matrix = np.corrcoef(nutrients, species)
corr = corr_matrix[0, 1]
R_sq = corr ** 2

print('ddfdf',R_sq)
print(df3.corr(method ='pearson'))
#Regression
slope, intercept, r_value, p_value, std_err = stats.linregress(nutrients,species)
line = slope*np.array(nutrients)+intercept

plt.plot(nutrients,
         line,
         'r',
         label='y={:.2f}x+{:.2f}'.format(slope,intercept))
print("Standard Error: ",std_err)
#plt.plot(X, Y_pred , color='blue')

plt.title("Nutrients Added vs Plant Species Found",
          fontsize=15)
plt.xlabel("Number of Nutrients Added")
plt.ylabel("Number of Plant Species")
plt.legend(fontsize=9)
#plt.show()
plt.clf()

#Question 4
df4 = pd.read_csv("C:/Users/doria/OneDrive/Desktop/Storage/School/AppliedStatistics/bme-applied-stats/lab10/Data/chap17q35FatherAgeMutations.csv")
plt.scatter(df4.Age,
            df4.NewMutations,
            s=15,
            color="green")
age = df4['Age'].to_list()
mutations = df4['NewMutations'].to_list()
slope, intercept, r_value, p_value, std_err = stats.linregress(age,mutations)

print("Standard Error: ",std_err)

line = slope*np.array(age)+intercept
plt.plot(age,
         line,
         'r',
         label='y={:.2f}x+{:.2f}'.format(slope,intercept))

plt.title("Father Age vs. New Mutations Found",
          fontsize=15)
plt.xlabel("Age of Father (years)")
plt.ylabel("New Mutations Found")
plt.legend(fontsize=9)

#plt.show()

model = LinearRegression()
corr_matrix2 = np.corrcoef(age, mutations)
corr2 = corr_matrix2[0, 1]
R_sq2 = corr2 ** 2
print(R_sq2)