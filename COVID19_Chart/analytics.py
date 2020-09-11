#!/usr/bin/env python
# coding: utf-8

# In[1]:
from COVID19_Chart.config import INITIAL_DATE, LATEST_UPDATE
import pandas as pd
import glob


# In[2]:



# In[6]:
FIELD_NAMES = [
    "positive", "negative", "pending", "hospitalizedCurrently", "inIcuCurrently", 
    "onVentilatorCurrently","recovered","hospitalized","totalTestsViral","positiveTestsViral",
    "negativeTestsViral","positiveCasesViral","deathConfirmed","deathProbable", "death"
]
EXCLUDED_TERRITORIES = ["AS", "GU", "MP", "PR", "VI"]

def initData():
    all_data = pd.DataFrame()
    for f in glob.glob("Data/CovidTrackingProject/Daily/State/*/daily.csv"):
        df = pd.read_csv(f)
        all_data = all_data.append(df,ignore_index=True, sort=False)
    all_data['date'] = pd.to_datetime(all_data['date'], format='%Y%m%d')
    # Exclude territories. Can separate or make optional in future.
    all_data = all_data[~all_data['state'].isin(EXCLUDED_TERRITORIES)]

    return all_data

# In[7]:

def filterDate(all_data, start_date, end_date):
    data_in_daterange = all_data[(all_data['date'] >= start_date) & (all_data['date'] <= end_date)]
    return data_in_daterange

# In[37]:

def filterColumns(data_in_daterange, columns):
    filtered_data = data_in_daterange.groupby(["state"])[list(enum for enum in columns)].sum()
    return filtered_data

# In[40]:

def update_chart(all_data, start_date=INITIAL_DATE,  end_date=LATEST_UPDATE):
    s_date = pd.to_datetime(start_date, format='%Y%m%d')
    e_date = pd.to_datetime(end_date, format='%Y%m%d')
    data_in_daterange = filterDate(all_data, s_date, e_date)

    filtered_data = filterColumns(data_in_daterange, FIELD_NAMES)
    filtered_data.to_csv(r'COVID19_Chart/static/data/output.csv')


# In[42]:
all_data = initData()
update_chart(all_data)
# %%
