#TRACKING YOUR FOCUS WITH PYTHON
#the tracking part for focus tracking
# The code has two main parts:
# 1. Creating the dataframe with the create_focus_df() function
#2. Plotting the focus using the plotly library in the plotfocus() function.
#The cool thing about this is that it gives you an idea of how much time you
#spend actually concentrated on activities, and how that varies in time.
import sys
import pandas as pd
import numpy as np
import time
import pathlib
import plotly.graph_objs as go #as pg
from test import loadFocus
from datetime import datetime
# import streamlit as st
# from os.path import dirname, join
# current_dir = dirname(__file__)
# FOCUS_DATA_PATH = join(current_dir, "./focus.txt")
# with open(file_path, 'r') as f:

FOCUS_DATA_PATH = "./focus.txt"

def logFocusTime(start, end):
    if not pathlib.path(FOCUS_DATA_PATH).is_file():
        with open(FOCUS_DATA_PATH, "w+") as focus:
            focus.write(f"{start} {end}")
            focus.write("\n")
    else:
        with open(FOCUS_DATA_PATH, 'a') as focus:
            focus.write(f"{start} {end}")
            focus.write("\n")

#This function (trackFocus) simply tracks an interval of time separated by 
#a simple input from the user (like hitting return key)
def trackfocus():                    
    start = int(time.time())          
    end_session = input("press to terminate tracking")
    end = int(time.time())
    total = (end - start) / 3600  
    print(f"Tracked: {total} hours")
    today_total = calculateFocusTime()
    print(f"Total focus time tracked today: {today_total}")
    logFocusTime(start, end)

#The loadFocus function logs the timestamps of the beginning and ending  of a session
def loadFocus():
    with open(FOCUS_DATA_PATH, "r") as focus:
        focusData = [f.strip("\n")  for f in focus.readlines()]

    timeStarts = np.array([int(f.split()[0]) for f in focusData])
    timeEnds = np.array([int(f.split()[1]) for f in focusData])

    durations = (timeEnds - timeStarts)/3600
    timeStartsStamp = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')\
                        for ts in timeStarts]

    dateStartsStamp = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d')\
                        for ts in timeStarts]


    return timeStartsStamp,dateStartsStamp,durations



def create_focus_df():
    today = datetime.strftime(datetime.today(),format="%Y-%m-%d")
    timeStartsStamp,dateStartsStamp,durations=loadFocus()
    df = pd.DataFrame(dict(dates=dateStartsStamp, focus=durations))
    return df

#This function (calculate...) returns the total amount of time tracked on a given day,
def calculateFocusTime():
    df = create_focus_df()
    todayFocus = df[df["dates"]==today]["focus"].sum()

    return todayFocus


#BELOW WILL BE A SCRIPT FOR VISUALIZATION OF FOCUS TIME
#- to visualiza focus time, we eill need 2 functions, one for creating a dataframe tp store our data properly, and another for plotting.

def plotFocus(df):
    df_focus_daily = pd.DataFrame(df.groupby("dates")["focus"].sum())
    mean_focus_time = round(df_focus_daily["focus"].mean(),2)
    focusBar = go.Bar(x=df_focus_daily.index,y=df_focus_daily["focus"],
                       name="Focus",marker_color="red")
    focusTrend = go.Scatter(x=df_focus_daily.index,y=df_focus_daily["focus"],    
                    name="Focus",marker_color="red")
    fig = go.Figure(data=[focusTrend,focusBar])
    fig.update_layout(title=f"Overview,  Average Focus Time: {mean_focus_time} hours")
    fig.update_yaxes(title="Focus (h)")
    fig.update_xaxes(title="Dates & Months (DM)")

    return fig


df = create_focus_df()
fig = plotFocus(df)
fig.show()


# # creating the dashboard app
# st.title("Focus Tracker")

# df_focus = create_focus_df()

# fig = plotFocus(df_focus)

# st.write(fig)
