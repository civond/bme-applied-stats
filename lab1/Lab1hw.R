##Lab Hw#1

library(ggplot2);
library(scales);
library(ggpubr);
library(dplyr);

#Question 1A
data = read.csv(file="C:/Users/doria/OneDrive/Desktop/Storage/School/AppliedStatistics/Lab1/chap02q19FireflySpermatophoreMass.csv", sep=";", header=T);

freq<-table(data);
freqTable<-as.data.frame(freq);

ggplot(data=data, aes(x=spermatophoreMass)) +
  #geom_bar(fill="lightblue") + 
  geom_histogram(bins=16, fill='purple', color='black', alpha=0.7) +
  theme(#panel.border = element_blank(),  #these 3 lines gets rid of grid
        #panel.grid.major = element_blank(),
        #panel.grid.minor = element_blank(),
        axis.text.x = element_text(angle = 45, vjust = 0.5),
        axis.title.y = element_text(size=13),
        axis.title.x = element_text(size=13),
        plot.title=element_text(size=18)) +
  labs(title="Photinus ignitus Spermatophore Mass Distribution", 
       x="Spermatophore Mass",
       y="Frequency") +
  scale_y_continuous(breaks=pretty_breaks()) +
  scale_x_continuous(breaks = scales::pretty_breaks(n = 8));
  
#Question 2C
col1 <- c("1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005");
col2 <- c("53","54","55","56","58","60","63","64","62","62","62");
df_bmi <- data.frame(col1, col2);

ggplot(df_bmi, aes(x=col1, y=col2)) +
  geom_line(group = 1,color="red") +
  geom_point() +
  labs(title="Percentage of Adults over 18 with a BMI greater than 25", 
       x="Year",
       y="Percentage (%)") +
  theme(plot.title=element_text(size=15));