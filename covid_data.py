import pandas as pd
import matplotlib.pyplot as plt




#this class handles the data frame
class covidData:

    def __init__(self,filename):
        self.globalDF = pd.read_excel(filename)
        self.today=self.globalDF['date'][len(self.globalDF)-1]





    #creates graph for a certain location
    def create_graph(self,location, absolute):

        df=self.globalDF

        #1 - filter for the location
        location_filter = df['location']==location
        dfOfLoc=df[location_filter]

        #2 - create colums & plot
        if absolute:
            deaths=dfOfLoc.loc[:,'total_deaths'].values
            label_str='Total Deaths'
        else:
            deaths=dfOfLoc.loc[:,'total_deaths_per_million'].values
            label_str='Total Deaths per million'
        
        date=dfOfLoc.loc[:,'date'].values
        plt.plot(date,deaths , c='b', label=label_str)


        #3 - add notation
        plt.xlabel('2020/02/24-'+self.today.replace('-','/'), fontsize = 18);
        plt.ylabel(label_str, fontsize = 18);
        plt.title(label_str+' in '+location, fontsize = 22)
        plt.legend()

        #4 -  create graph
        plt.savefig(label_str+' in '+location+'.png',dpi=300)
        plt.close()
        print("finished")
        return (label_str+' in '+location+'.png')

    #creates a histogram of distribution of death total among countries
    #can be used for any date in the data set
    def create_histogram(self, date, absolute=False):

        
        #number of bins in histo, for numeric reasons (around square root of the number of locations)
        BINS=14

        #1 - filter for the date
        df=self.globalDF
        date_filter = df['date']==date
        dfOfDate=df[date_filter]

        #2 - check the mode: absolute or per million
        if absolute:
            label_str='Total Deaths'
            dfOfDate[['total_deaths']].hist(bins=BINS)
        else:
            label_str='Total Deaths per million'
            dfOfDate[['total_deaths_per_million']].hist(bins=BINS)

        #3 - add 
        plt.xlabel(label_str, fontsize=18)
        plt.ylabel('Number of Countries', fontsize = 18)
        plt.title(label_str+' Histogram', fontsize = 22)

        #4 - create histogram
        plt.savefig(label_str+' Histogram.png',dpi=300)
        plt.close()
        print("finished histo")
        return (label_str+' Histogram.png')

