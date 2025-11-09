# Create # streaming_analysis.py
# ---------------------------------------------------------------
# Spotify Wrapped Data Analysis
# This program analyzes personal Spotify listening history data
# using pandas and matplotlib, then outputs summary statistics
# and visualizations.
# ---------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# Step 1: Load Data
# ---------------------------------------------------------------
df = pd.read_csv('personal_listening_history.csv')

# Preview first few rows (optional for testing)
print("Preview of Data:")
print(df.head(), "\n")

# ---------------------------------------------------------------
# Step 2: Order Days and Months
# ---------------------------------------------------------------
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Convert to categorical for proper sorting
if 'month' in df.columns:
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

if 'day_of_week' in df.columns:
    df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=day_order, ordered=True)

# ---------------------------------------------------------------
# Step 3: Descriptive Statistical Analysis
# ---------------------------------------------------------------
# Average completion rate
completion_rate = df['completion_rate'].mean()

# Total listening time
total_time_seconds = df['duration_seconds'].sum()
tot
 code here
