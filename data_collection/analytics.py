#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd
import glob


# In[2]:


# In[6]:

def initData():
    exclude_states = ["PR", "MP", "AU", "GU", "VI"]
    all_data = pd.DataFrame()
    for f in glob.glob("Data/CovidTrackingProject/Daily/State/*/daily.csv"):
        df = pd.read_csv(f)
        all_data = all_data.append(df,ignore_index=True, sort=False)
    all_data['date'] = pd.to_datetime(all_data['date'], format='%Y%m%d')
    all_data = all_data[~all_data.state.isin(exclude_states)]
    return all_data

# In[7]:

def filterDate(all_data, start_date, end_date):
    current_data = all_data[(all_data['date'] == end_date)]
    data_in_daterange = all_data[(all_data['date'] >= start_date) & (all_data['date'] <= end_date)]
    return current_data

# In[37]:

def filterColumns(data_in_daterange, columns):
    filtered_data = data_in_daterange.groupby(["state"])[list(enum for enum in columns)].sum()
    return filtered_data

# In[40]:

def update_chart(all_data, start_date="03012020", end_date="08121820"):
    s_date = pd.to_datetime(start_date, format='%Y%m%d')
    e_date = pd.to_datetime(end_date, format='%Y%m%d')
    data_in_daterange = filterDate(all_data, s_date, e_date)
    columns = [
        "positive", "negative", "hospitalizedCurrently", "hospitalizedCumulative", "inIcuCurrently", "inIcuCumulative",
        "onVentilatorCurrently","recovered", "death","deathConfirmed","deathProbable"
    ]
    filtered_data = filterColumns(data_in_daterange, columns)
    filtered_data.to_csv(r'static/data/output.csv')

# TODO: Estimate cumulative based on "currently" history
# TODO: Compare HospitalizedCumulative to Hospitalized 
# TODO: Obtain better death counts
# TODO: Average grade for that state
# In[42]:
all_data = initData()

update_chart(all_data, "20200322", "20200902")
# %%
