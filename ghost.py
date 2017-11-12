# import libraries 
import numpy as np
import pandas 
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from math import sqrt
from collections import Counter
style.use('fivethirtyeight')

# import dataset 
import pandas 
with open ("skater_stats_2017-11-10.csv",'r') as csvfile:
    nhl_def=pandas.read_csv(csvfile)

#subset ice time (total ice time greater than the mean)
nhl_def=nhl_def[nhl_def.TOI>951.45]

#select columns (zone starts)
distance_columns=nhl_def[['OZS%','DZS%','NZS%']]

#selected player
selected_player=nhl_def[nhl_def["Player"]=="SHAYNE.GOSTISBEHERE"].iloc[0]

#euclidean distance function 
def euclidean_distance(row):
    """
    A simple euclidean distance function
    """
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_player[k]) ** 2
    return math.sqrt(inner_value)

# find the distance from a player
ghost_distance=nhl_def.apply(euclidean_distance,axis=1)

#normalize the data 
nhl_def_norm=(distance_columns-distance_columns.mean())/distance_columns.std()

#find the nearest neighbor 
from scipy.spatial import distance 

#fill in the na values in nhl_def_norm
nhl_def_norm.fillna(0,inplace=True)

#normalized vector
ghost_norm=nhl_def_norm[nhl_def["Player"]=="SHAYNE.GOSTISBEHERE"]

#distance between GOSTISBEHERE and every other defenseman (zone starts)
euc_distance=nhl_def_norm.apply(lambda row: distance.euclidean(row,ghost_norm),axis=1)

#create a new dataframe with distances between GOSTISBEHERE and every other defenseman
distance_df=pandas.DataFrame(data={"dist":euc_distance,"idx": euc_distance.index})
distance_df.sort("dist",inplace=True)

#find the most similar player to GOSTISBEHERE
most_similar=nhl_def.loc[int(second_smallest)]["Player"]
close=distance_df.iloc[5]["idx"]
close1=nhl_def.loc[int(close)]["Player"]

