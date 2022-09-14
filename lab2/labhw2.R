library(ggplot2);
library(tidyverse);
library(scales);

#Question 1A/1C
data = read.csv(file="C:/Users/doria/OneDrive/Desktop/Storage/School/AppliedStatistics/zebrafish-corpseflower/data/chap03q23ZebraFishBoldness.csv", sep=",", header=T);
ggplot(data, aes(x=genotype, y=secondsAggressiveActivity, fill=genotype)) + 
  geom_boxplot(alpha=0.7) +
  labs(title="Zebrafish Aggressive Activity", 
       x="Genotype",
       y="Seconds of Aggressive Activity");

wild <- subset(data, genotype == "wild type");
mutant <- subset(data, genotype == "Spd");
IQR(wild$secondsAggressiveActivity);
IQR(mutant$secondsAggressiveActivity);

#Question 2A/B
data2 = read.csv(file="C:/Users/doria/OneDrive/Desktop/Storage/School/AppliedStatistics/zebrafish-corpseflower/data/chap04q18Corpseflowers.csv", sep=",", header=T);
mean(data2$numberOfBeetles)
sd(data2$numberOfBeetles)

standard_error <- function(x) sd(x) / sqrt(length(x)) # Create own function
x <- data2$numberOfBeetles
standard_error(x)

#Question 2C
data2 <- tibble::rowid_to_column(data2, "index")


ggplot(data=data2, aes(x=index,y=numberOfBeetles)) +
  geom_line(color="blue") + 
  geom_point() +
  labs(title="Number of Beetles Visiting Per Night", 
       x="Night",
       y="Number of Beetles") +
  scale_x_continuous(breaks = scales::pretty_breaks(n = 8));
  

