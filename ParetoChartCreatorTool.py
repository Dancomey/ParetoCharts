#A program that creates a Pareto Chart from data that the user supplies
# Reference: https://levelup.gitconnected.com/how-to-make-pareto-chart-in-matplotlib-ff9b6ec7fadf

#By: Dan Comey

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import json
import random


def CreatePareto(df, column_name, axis_label, chart_title, file_name):
    #sorting the values of the dataframe in descending order
    df.sort_values(by= column_name, ascending= False, inplace= True)


    #creating the histogram portion of the chart

    fig, ax = plt.subplots(figsize= (16, 9))

    ax.bar(x= df.index, height= df[column_name], width = 0.98, edgecolor = "Black")

    ax.set_ylim(0, int(1.1*df[column_name].max()))
    ax.set_yticks(range(0, int(1.1*df[column_name].max()), 5))

    ax.set_title(chart_title, fontsize= 28)

    ax.set_ylabel(axis_label, fontsize= 18)

    #creating the line portion of the chart

    #new column for the cumulative sum of the (sorted) data
    df["cumsum"] = df[column_name].cumsum()

    #new column for the relative cumulative sum
    df["relcumsum"] = df["cumsum"] / df[column_name].sum()


    #adding second Y-axis for the line plot
    ax2 = ax.twinx()
    ax2.plot(df["relcumsum"], marker = "o", linewidth = 3.0, markersize = 6.0, color = "black")

    ax2.set_ylabel("Cumulative Percentage", fontsize= 18)


    ax.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)


    for x_val, y_val in zip(range(len(df)),df["relcumsum"]):
        text = f"{y_val:.0%}"
        ax2.text(x = x_val - 0.10, y = y_val + 0.015, s = text, color = "black", ha = "center", va = "center")


    ax2.axhline(y=0.8, color='red', linestyle='--')

    plt.savefig(file_name)
    print("chart created: " + file_name)

user_data = input("Please enter data in dictionary form: ")
column_name = input("Please enter the column name: ")
axis_label = input("Please enter the axis label: ")
chart_title = input("Please enter the chart title: ")
dict_data = json.loads(user_data)

# column_name = "SumTotal"
# axis_label = "Sales (units)"
# chart_title = "Test with grocery store data"


# dict_data = test_data = {
#     "Arkansas": random.randint(1, 100),
#     "Texas": random.randint(1, 100),
#     "Maine": random.randint(1, 100),
#     "Georgia": random.randint(1, 100),
#     "Alaska": random.randint(1, 100),
#     "Florida": random.randint(1, 100),
#     "Vermont": random.randint(1, 100)
# }


# #Creating a dataframe with the above dictionary
# df = pd.DataFrame.from_dict(dict_data, orient= "index",columns= [column_name])

file_path = "/Users/dancomey/Documents/GitHub/ParetoChart/ParetoCharts/GroceriesDataSet.csv"

df = pd.read_csv(file_path)

# Calculate the sum total per group and create a new column
df['SumTotal'] = df.groupby('Item')['Quantity Sold (kilo)'].transform('sum').astype(int)

columns_to_delete = ['Date', 'Time', 'Item Code', 'Quantity Sold (kilo)', 'Unit Selling Price (RMB/kg)', 'Sale or Return']
df = df.drop(columns=columns_to_delete)


print(df.head())


CreatePareto(df, column_name, axis_label, chart_title, "GroceryChart.png")




    

