# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 2023
@author: manoj
"""


import pandas as pd
import matplotlib.pyplot as plt
import random as random


def read_data(visualise_type):
    """ "
    This function will read data from all required data sets
    """

    if visualise_type == "Line":
        Co2_Data = pd.read_csv("Global_Co2.csv")
        return Co2_Data

    if visualise_type == "Bar_Plot":
        Games_Data = pd.read_csv("Most Played Games 2022.csv")
        return Games_Data

    if visualise_type == "Piechart":
        UK_Transport_Data = pd.read_csv("UK Transportation Percentage 2022.csv")
        return UK_Transport_Data


def addlabels(x, y):
    """
    This function is to add value lables to bar chart
    """

    for i in range(len(x)):
        plt.text(
            i,
            y[i] / 0.969,
            y[i],
            ha="center",
        )


def line_plot():
    """
    This function plots Co2 Emission  by 4 countries for the period 2017 to 2021
    """


# Calling the function to read data
Co2_dataset = read_data("Line")
print(Co2_dataset)
plt.figure()
Year = Co2_dataset["Year"]
Argentina = Co2_dataset["Argentina"]
Australia = Co2_dataset["Australia"]
Canada = Co2_dataset["Canada"]
Austria = Co2_dataset["Austria"]
# Plot the countries with label
plt.plot(Year[:5], Argentina[:5], marker="o", label="Argentina")
plt.plot(Year[:5], Australia[:5], marker="o", label="Australia")
plt.plot(Year[:5], Canada[:5], marker="o", label="Canada")
plt.plot(Year[:5], Austria[:5], marker="o", label="Austria")
# Showing the legend
plt.legend()
# Setting X-axis limits
plt.xlim(2017, 2022)
# Assigining Title, X-axis label, Y-axis label
plt.title("Co2 Emission by Country (2017-2021)")
plt.xlabel("Years")
plt.ylabel("Co2 Emission in (tons)")
# Saving the image
plt.savefig("line.png", bbox_inches="tight", dpi=500)
plt.show()


def bar_plot():
    """
    This function plots top 10 computer games of 2022
    """


# Calling the function to read data
Games_dataset = read_data("Bar_Plot")
print(Games_dataset)
Name = Games_dataset["Name"]
Play_count = Games_dataset["All_time peak"]
Rank = Games_dataset["Rank"]
hexadecimal_aplha = "123456789ABCDEF"
plt.figure()
# Plot the Name of the game with label in bar plot
bars = plt.bar(Name, Rank)
# Generating random hexadecimal value for assigining color to each bar
col = [
    "#" + "".join([random.choice(hexadecimal_aplha) for j in range(6)])
    for i in range(10)
]
# Assigining each bar with a random color
for i in range(len(col)):
    bars[i].set_color(col[i])
plt.xticks(rotation=90, horizontalalignment="center")
plt.ylim(0, 12)
# calling the function to add value labels
addlabels(Name, Rank)
# Assigining Title, X-axis label, Y-axis label
plt.xlabel("Computer Games")
plt.ylabel("Rank")
plt.title("Top 10 computer games of 2022")
# Saving the image
plt.savefig("bar.png", bbox_inches="tight", dpi=500)
plt.show()


def piechar():
    """
    This function creates pie chart showing the Percentage of workers usually travelling to work in UK
    """


# Calling the function to read data
Transport_data = read_data("Piechart")
print(Transport_data)
Mode_of_transportation = Transport_data["Mode"]
Percentage = Transport_data["Percentage"]
plt.figure()
# Plot the pie chart with percentage values and setting pieplot properties
plt.pie(
    Percentage,
    labels=Mode_of_transportation,
    autopct="%1.f%%",
    startangle=270,
    pctdistance=0.6,
    wedgeprops={"linewidth": 3.0, "edgecolor": "white"},
)
# Giving axis values
plt.axis("equal")
# Showing the legend and setting its loaction
plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1))
plt.title("Percentage of workers usually travelling to work in UK - 2022", fontsize=10)
# Saving the image
plt.savefig("pie.png", bbox_inches="tight", dpi=500)
plt.show()


# Calling function to visualise line plot
line_plot()

# Calling function to visualise Bar plot
bar_plot()

# Calling function to visualise Piechart
piechar()
