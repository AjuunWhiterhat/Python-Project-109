import csv
import statistics
import plotly.figure_factory
import pandas as pd
from turtle import st
import plotly.figure_factory as ff

data = pd.read_csv("StudentsPerformance.csv")
readingList = data["reading score"].to_list()

readingMean = statistics.mean(readingList)
readingMedian = statistics.median(readingList)
readingMode = statistics.mode(readingList)

print("Mean, Median, Mode of Reading score is {},{},{}".format(readingMean,readingMode,readingMode))

std_reading = statistics.stdev(readingList)

print("Standard deviation for the reading score is {}".format(std_reading))

reading1_std_start,reading1_std_end = readingMean - std_reading,readingMean + std_reading
reading2_std_start,reading2_std_end = readingMean - (2*std_reading),readingMean + (2*std_reading)
reading3_std_start,reading3_std_end = readingMean - (3*std_reading),readingMean + (3*std_reading)

first_std_reading = [result for result in readingList if result>reading1_std_start and result<reading1_std_end]
print("{}% This is the amount of data lies within 1st Standard Deviation".format(len(first_std_reading)*100/len(readingList)))

second_std_reading = [result for result in readingList if result>reading2_std_start and result<reading2_std_end]
print("{}% This is the amount of data lies within 2nd Standard Deviation".format(len(second_std_reading)*100/len(readingList)))

third_std_reading = [result for result in readingList if result>reading3_std_start and result<reading3_std_end]
print("{}% This is the amount of data lies within 3rd Standard Deviation".format(len(third_std_reading)*100/len(readingList)))



