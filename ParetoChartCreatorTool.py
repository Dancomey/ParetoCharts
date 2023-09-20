#A program that creates a Pareto Chart from data that the user supplies
# Reference: https://levelup.gitconnected.com/how-to-make-pareto-chart-in-matplotlib-ff9b6ec7fadf

#By: Dan Comey

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


data = input("Please enter something: ")
print("You entered:", data)








# #Dictionary of sales by state
# sales_dict = {"Arkansas": 10, "Texas": 8, "Maine": 3, "Georgia": 5, "Alaska": 1, "Florida": 20, "Vermont": 2, "California": 1}

# #Creating a dataframe with the above dictionary
# df = pd.DataFrame.from_dict(sales_dict, orient= "index",columns= ["sales_per_state"])
# #print(df.head())

# #sorting the values of the dataframe in descending order
# df.sort_values(by= "sales_per_state", ascending= False, inplace= True)


# #creating the histogram portion of the chart

# fig, ax = plt.subplots(figsize= (16, 9))

# ax.bar(x= df.index, height= df["sales_per_state"], width = 0.98, edgecolor = "Black")

# ax.set_ylim(0, 22)
# ax.set_yticks(range(0, 24, 2))

# ax.set_title("Weekly Sales by State", fontsize= 28)

# ax.set_ylabel("Sales ($)", fontsize= 18)

# # plt.savefig("histogram1.png")


# #creating the line portion of the chart

# #new column for the cumulative sum of the (sorted) data
# df["cumsum"] = df["sales_per_state"].cumsum()

# #new column for the relative cumulative sum
# df["relcumsum"] = df["cumsum"] / df["sales_per_state"].sum()


# #adding second Y-axis for the line plot
# ax2 = ax.twinx()
# ax2.plot(df["relcumsum"], marker = "o", linewidth = 3.0, markersize = 6.0, color = "black")

# ax2.set_ylabel("Cumulative Percentage", fontsize= 18)


# ax.spines['top'].set_visible(False)
# ax2.spines['top'].set_visible(False)


# for x_val, y_val in zip(range(len(df)),df["relcumsum"]):
# 	text = f"{y_val:.0%}"
# 	ax2.text(x = x_val - 0.10, y = y_val + 0.015, s = text, color = "black", ha = "center", va = "center")


# ax2.axhline(y=0.8, color='red', linestyle='--')

# plt.savefig("histogram3.png")

