#!/usr/bin/env python
# coding: utf-8

# # Get COVID-19 Data
# 
# 
# ### Python Script Get COVID-19 Data
# 
# Downloads JSON data from api.covid19india.org and returns it in a Pandas DataFrame.
# 
# See [covid19india.org](https://www.covid19india.org/) for more info.
# 
# The data is split into 8 jSON files (as of July 9)
# 
# `read_json_data(no_of_files = 8)` <br>
# Change `no_of_files` when calling the function if necessary.

# In[1]:


import numpy as np
import pandas as pd
import urllib.request, json 


# In[2]:


api = "api.covid19india.org/"

def read_json_data(no_of_files = 8):
    """Read json data from api and return a dataframe with the data"""
    
    lst = []

    for i in range(1, no_of_files+1):
        with urllib.request.urlopen("https://" + api + "raw_data" + str(i) + ".json") as url:
            data = json.loads(url.read().decode())
            lst.append(pd.json_normalize(data['raw_data']))
        
                                     
    raw_data = pd.concat(lst, ignore_index = True)
                                     
    return raw_data


# In[ ]:


raw_data = read_json_data()

