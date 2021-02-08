# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 23:00:26 2021

@author: user
"""

from Web_Scraper import getIDs, getScores
import time
import numpy as np
from multiprocessing import Pool
#import grid


if __name__ == '__main__':
 
    url = "https://www.rugbyleagueproject.org/competitions/super-league/seasons.html"

    start_time = time.time() 
    ID_list= getIDs(url)
    elapsed_time = time.time() - start_time
    print("Elapsed time of ID search:" , elapsed_time)
    
    url_links = ["https://www.rugbyleagueproject.org/competitions/" + ID + '/results.html' for ID in ID_list]
    
    #multiprocessing - reduced time taken from 65 seconds to roughly 10 seconds
    print("Getting scores:")
    start_time = time.time() 
    p = Pool(10)
    scores = p.map(getScores, url_links)
    p.terminate()
    p.join()
    elapsed_time = time.time() - start_time
    print("Elapsed time of lists:" , elapsed_time)
    
    arr = np.array([year[0] for year in scores])
    
    
    