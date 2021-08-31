import os
import math

import numpy as np
import pandas as pd
np.warnings.filterwarnings('ignore')
from color import color
#pylint: disable=unused-variable

basedir = os.path.abspath(os.path.dirname(__file__))
master = pd.read_csv(basedir + '/data/master.csv')

dv = pd.read_csv(basedir + "/data/dv.csv")
dv[dv.columns[4:]] = dv[dv.columns[4:]].apply(pd.to_numeric)

# converts date to correct format, for homogeneity
dv['date'] = pd.to_datetime(dv['date'])
dv['date'] = dv['date'].dt.strftime('%Y-%m-%d')

# finding the days elapsed and making a new column, so this data can be plotted. Basically our time axis
dv['Weeks Elapsed'] = (pd.Timestamp.now().normalize() - pd.to_datetime(dv['date'])) / np.timedelta64(1, 'D')
dv['Weeks Elapsed'] /= 7
dv['Weeks Elapsed'] = dv['Weeks Elapsed'].values[::-1]

#below will be used to implement a ranged slider, so users can select dates of interest from new time column found above
max_time = dv['Weeks Elapsed'].iat[-1]
max_time = math.ceil(max_time)
interval = int(math.ceil(max_time/10))

intervals = []
for i in range(0,interval+1):
    intervals.append(i*10)

#assigning a unique color to each state, so the color is constant at all times
dv['Color'] = "any"
abbreviations = dv.abbr.unique()

color_index = 0
for i in abbreviations:
    dv.loc[dv.abbr == i, 'Color'] = color[color_index]
    color_index += 1
#print(dv[dv["State/Territory/Federal Entity"] == "Alaska"]) #check for colors you do not like

def Return_Data():
    return(dv)