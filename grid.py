# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:26:43 2021

@author: Amritz
"""

import numpy as np
import pandas as pd

def scores_to_DataFrame(arr):
    df = pd.DataFrame()
    df_away = pd.DataFrame()
    
    for i in range(len(arr)):
        df = df.append(arr[i][0])
        df_away = df_away.append(arr[i][1])
    
    df = pd.concat([df, df_away], axis = 1, ignore_index = True)
    df.columns = ["Home", "Away"]
    return df

    #df = df.append([place for i in range(len(arr)) for place in arr[i]])
    
def comparison(df):
    highest_score = max(df.max())
    #make a winner vs loser thing
    #swap values if away < home, and change column name
    df.loc[df["Home"] < df["Away"], ["Home","Away"]] = \
        df.loc[df["Home"] < df["Away"], ["Away", "Home"]].values
    df.columns = ["Winner", "Loser"]
    table = pd.crosstab(df.Loser, df.Winner)
    
    Winner = [i for i in range(0, highest_score+1)]
    Loser = [i for i in range(0, highest_score+1)]
    table = table.reindex(index=Loser, columns=Winner, fill_value=0)
    return table