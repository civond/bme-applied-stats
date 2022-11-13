import pandas as pd
import statistics
import math

no_exercise = [240,261,271,275,276,281]
exercise = [261,293,316,319,324,247]

mean_Noex = statistics.mean(no_exercise)
std_Noex = statistics.stdev(no_exercise)
n_Noex = len(no_exercise)

mean_Ex = statistics.mean(exercise)
std_Ex = statistics.stdev(exercise)
n_Ex = len(exercise)

print("Mean no exercise: " + str(mean_Noex))
print("Standard Dev no exercise: " + str(std_Noex))
print("Mean exercise: " + str(mean_Ex))
print("Standard Dev exercise: " + str(std_Ex))

mean_diff = mean_Noex - mean_Ex

pooled_variance = (((n_Noex-1)*(std_Noex**2))
                   + ((n_Ex-1)*(std_Ex**2)))\
                  /(n_Ex+n_Noex-2)
standard_error = math.sqrt(pooled_variance*((1/(n_Ex)) + (1/(n_Noex))))

t = 2.228 #from t-table

print("Pooled Variance: " + str(pooled_variance))
print("Standard Error: " + str(standard_error))
print("Mean Difference: " + str(mean_diff))

lower = mean_diff-(standard_error*(t))
upper = mean_diff+(standard_error*(t))

t_value = mean_diff/standard_error


print("Confidence Interval: {%s,%s}" % (lower, upper))
print("Test Statistic: " + str(t_value))

#Question 2
kid = [-3.23,-1.78,-0.72,-0.57,0.32,0.46,1.07,1.77,2.22]
unrelated = [-3.26,-2.71,-0.13,-3.24,-2.56,-0.62,0.12,1.12,1.74]
difference = []

i=0
while i in range(0,len(kid)):
    difference.append(round(kid[i]-unrelated[i],2))
    i+=1
mean_diff_goat = statistics.mean(difference)
print("Mean Difference: " + str(mean_diff_goat))

temp = []
for item in difference:
    temp.append((item-mean_diff_goat)**2)

STError_goat = (1/math.sqrt(len(temp)))*\
               math.sqrt(sum(temp)/(len(temp)-1))

print("Standard Error: "+ str(STError_goat))
