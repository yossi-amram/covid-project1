Description :

***CREDIT :This app uses as data the excel file 'owid-covid-data.xlsx' , citation:
Hannah Ritchie, Edouard Mathieu, Lucas Rodés-Guirao, Cameron Appel, Charlie Giattino, Esteban Ortiz-Ospina, Joe Hasell, Bobbie Macdonald, Diana Beltekian and Max Roser (2020) - "Coronavirus Pandemic (COVID-19)". 
Published online at OurWorldInData.org. 
Retrieved from: 'https://ourworldindata.org/coronavirus' [Online Resource]

This simple app creates graphs and histograms of number of Covid19 deaths in locations in the world.

It has 2 python files :
1. 'covid stat - gui.py' - This code creates the GUI for the app
2. 'covid_data.py' - This code handles the data and the graph/histogram creation.

It uses as a data set an excel file: 'owid-covid-data.xlsx' , taken from "ourworldindata.org" see ***CREDIT.

This folder also includes:
# 'GUI screenshot.png' a screenshot of the GUI running.
#Folder containing histograms & graphs for example, produced by the app.

NOTE: 
1.the data set is large so the app takes some time to load (about 30sec on my machine)
2,matplotlib throws an error somtimes when a file that is edited that already exists is open in windows 
while the program is running.
