import csv
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random
import statistics
import pandas as pd 

df = pd.read_csv("data3.csv")

data = df ["Math_score"].tolist()
def random_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean  =  statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_mean(100)
    mean_list.append(set_of_means)    
mean = statistics.mean(mean_list)
print("Mean of Distribution is ", mean)            

fig = ff.create_distplot([data],["Math Scores"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20], mode = "lines", name = "MEAN"))
fig.show()

#mean = statistics.mean(data)
#sd = statistics.stdev(data)

#print("Mean is", mean)
#print("Stnadard Deviation is ", sd)