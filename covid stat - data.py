import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.io import excel
import datetime
import requests
from requests.models import Response
import re

#should replace with info from API
filename = 'owid-covid-data.xlsx'
#response = requests.get("http://apps.who.int/gho/athena/api/GHO/WHOSIS_000001.xls?filter=COUNTRY:BWA&profile=excel&format=xml",allow_redirects=True)
##print(response.status_code)
#open('data.xls', "wb").write(response.content)
#print(response.status_code)
#data=open("data.json",'w+')
#data.write(str(response.json()))
#data.write(response.text)
#df = pd.read_csv("data.xls")
df = pd.read_excel(filename)
#print(df.info())


#filter to countries , dates and toatl deaths


df=df[['total_deaths','location','date']]


#creates graph for a certain location
def create_graph(location):
    #1 filter for the location
    location_filter = df['location']==location
    dfOfLoc=df[location_filter]

    #2 create colums & plot
    total_deaths=dfOfLoc.loc[:,'total_deaths'].values
    date=dfOfLoc.loc[:,'date'].values
    plt.plot(date,total_deaths)

    #3 add notation
    now=datetime.datetime.now()-datetime.timedelta(days=1)
    today=str(now.year)+"/"+now.strftime('%m')+"/"+now.strftime('%d')

    plt.xlabel('2020/02/24-'+today, fontsize = 22);
    plt.ylabel('Total Deaths', fontsize = 22);
    plt.title('Total COVID-19 Deaths', fontsize = 24)

    plt.savefig('img.png',dpi=300)


create_graph("Israel")

print("check")




#2 create graph