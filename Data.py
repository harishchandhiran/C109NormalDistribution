import statistics
import plotly.graph_objects as pg
import plotly.figure_factory as pff
import pandas as pd
import csv

file_data = pd.read_csv("data.csv")
data = file_data["reading score"].tolist()
mean = sum(data) / len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std = statistics.stdev(data)

first_std_deviation_start , first_std_deviation_end = mean-std , mean+std
second_std_deviation_start , second_std_deviation_end = mean-(2*std) , mean+(2*std)
third_std_deviation_start , third_std_deviation_end = mean-(3*std) , mean+(3*std)

fig = pff.create_distplot([data], ["reading score"], show_hist=False)
fig.add_trace(pg.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(pg.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(pg.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(pg.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(pg.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("mean:- ", mean)
print("median:- ", median)
print("mode:- ", mode)
print("mean:- ", mean)
print("Standard deviation:- ", std)
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))