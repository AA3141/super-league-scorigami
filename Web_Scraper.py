# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:25:39 2021

@author: Amritz
"""

"""Plan:
    1. Obtain seasons pages                       DONE
    2. Obtain all IDs of the competitions         DONE
    3. Obtain the score tables of each ID         DONE
    4. keep all the scores                        DONE
    5. Keep in a grid
"""
from bs4 import BeautifulSoup
import requests
import re


def getIDs(url = "https://www.rugbyleagueproject.org/competitions/super-league/seasons.html"):
    print("Getting IDs")
    headers =  {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}
    response = requests.get(url, timeout = 10, headers = headers)
    content = BeautifulSoup(response.content, "html.parser")
    
    response.close()
    
    ID_list = []
    #re.compile is used here to find all the hrefs that end with a number
    relevant_links = content.findAll('a', href = re.compile("[0-9]$"))
    for link in relevant_links:
        ID = re.findall(r"\d+", link.get('href'))
        ID_list.extend(ID)
    
    print("Done.")
    return ID_list


def getScores(url):
    headers =  {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
    }
    
    scores_list = []
    home_scores = []
    away_scores = []
    response = requests.get(url, timeout = 10, headers = headers)
    content = BeautifulSoup(response.content, "html.parser")
    response.close()
    
    scores = content.findAll("td", attrs = {"class":"n"})
    del scores[2::3] #deletes the number of spectators
    home_scores = [int(score.text) for score in scores[::2]]
    away_scores = [int(score.text) for score in scores[1::2]]
    scores_list.append([home_scores, away_scores])
    
    return scores_list    
        


    

#first dimension of scores_list = year
#second dimension = home/away
#third dimension = which match



