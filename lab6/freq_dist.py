import pandas as pd
import matplotlib.pyplot as plt
import statistics

values = [-5.19,-1.20 ,-0.50,-0.33,-0.15,-0.15,-0.15,-0.07,0.02,0.02,0.28,0.37,0.45,1.76,2.80]
mean = statistics.mean(values)
stdev = statistics.stdev(values)
sample_size = len(values)

plt.hist(values,
         color='g',
         edgecolor='black',
         bins=20)
plt.title('Median Angle of Direction Change')
plt.xlabel('Degrees per Second')
plt.ylabel('Angle')

print('Mean: ' + str(mean))
print('Standard Deviation: '+ str(stdev))
print('Sample Size: ' + str(sample_size))

plt.show()