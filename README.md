# Focus-tracker

# TRACKING YOUR FOCUS WITH PYTHON

This Python program allows you to track and visualize your focus time. It logs the timestamps of your focus sessions and provides insights into your total focus time.

# PREREQUISITES

To run this program, make sure you have the following installed:

Python
pandas library
numpy library
time module
pathlib module
plotly library

# HOW TO USE

Open a text file named "focus.txt" in the same directory as the Python program. This file will be used to store the timestamps of your focus sessions.

Run the program by executing the following command in the terminal or command prompt:

# COMMAND: python filename.py

Replace filename.py with the actual name of the Python file.

# ####The program has two main parts:

Tracking Focus Time: When prompted, press the Enter key to start tracking your focus time. To stop tracking, press Enter again. The program will calculate the duration of your focus session and display the tracked time.

Visualizing Focus Time: The program will generate a visualization of your focus time based on the data stored in the "focus.txt" file. The visualization includes a bar chart showing the focus time for each date and a line chart showing the trend of focus time over time.

The visualization will be displayed on the screen, showing the average focus time and the focus time for each date.

Optionally, you can uncomment the code related to the Streamlit library and run the program with Streamlit to create a dashboard app for tracking and visualizing your focus time. This will provide a more interactive and user-friendly experience.

# HOW IT WORKS

The program uses a text file "focus.txt" to store the timestamps of the beginning and ending of each focus session.

The trackfocus() function tracks an interval of time separated by a simple input from the user. It records the start and end timestamps in the "focus.txt" file.

The loadFocus() function reads the data from the "focus.txt" file and extracts the start and end timestamps of each focus session.

The create_focus_df() function creates a pandas DataFrame from the focus session data, grouping the sessions by date and calculating the total focus time for each date.

The calculateFocusTime() function calculates the total focus time tracked on a given day.

The plotFocus() function creates a visualization of the focus time using the plotly library. It generates a bar chart showing the focus time for each date and a line chart showing the trend of focus time over time.

The program calls the necessary functions to track focus time, create the DataFrame, and plot the focus time visualization.

Feel free to modify and customize this program according to your needs. Stay focused!
