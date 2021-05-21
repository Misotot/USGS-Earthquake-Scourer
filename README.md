# USGS-Earthquake-Scourer

This program first downloads some specific data from the USGS website and stores it in a MongoDB database. 

Then it runs some cleaning and modeling processess before extracting the neccesary information from JSON data and groups the remaining data into regions.

Extensive cleaning has to be done to regions because there is a lot of variation in naming (S, South, south, sth, etc).

I try and create a few visualizations and save some plot points. 

The program downloads 5,000 earthquakes from USGS and saves from to a MongoDB DB. 
