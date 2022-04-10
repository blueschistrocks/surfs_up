# surfs_up

## Project Overview 
The project intailed an analysis the temperature trends for the months of June and December in Oahu, Hawaii, in order to evaluate the year-round sustainability of a surf and ice cream shop business. Python, Pandas, SQLite and SQLAlchemy were used to perform this analysis.

## Resources
- Data Sources: 
- Software: Python 3.7 and Jupyter Notebook 6.0.3

## Results Discussion

June temperatures in the years 2010 to 2017 ranged from a low of 64 to a high of 85 degrees fahrenheit. December temperatures in the years 2010 to 2016 ranged from low of 56 to a high of 83 degrees fahrenheit. The average temperature in June in the years 2010 to 2017 was 75 degrees fahrenheit and December's average temperature in the years 2010 to 2016 was 71 degrees fahrenheit. 50% of June and December temperatures in the years analyzed were above 75 and 71 degrees fahrenheit, respectively. The standard deviation for December's temperatures was slightly higher than for June indicating that temparatures were more varied in December. 


## Summary
In genreral the temparatue differenace between June and December in Oahu Hawaii does not tend to vary, however December has slighly cooler tempuratures than June. Based on this analysis the weather should be suiteable for an surf and icecream shop.

## Images of Analysis Output

#### December Temperature DateFrame
![image](https://github.com/blueschistrocks/surfs_up/blob/b3beec2a22bf9fd85057370fdcd90ac957234de5/Images/Dec_temp_df.png)<br>
#### December Temperature Statistics
![image](https://github.com/blueschistrocks/surfs_up/blob/b3beec2a22bf9fd85057370fdcd90ac957234de5/Images/Dec_temp_stats.png)<br>
#### June Temperature DateFrame
![image](https://github.com/blueschistrocks/surfs_up/blob/b3beec2a22bf9fd85057370fdcd90ac957234de5/Images/June_temp_df.png)<br>
#### June Temperature Statistics
![image](https://github.com/blueschistrocks/surfs_up/blob/b3beec2a22bf9fd85057370fdcd90ac957234de5/Images/June_temp_stats.png)<br>

## Additional Analysis

  session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()

  session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 12).all()


Given that this proposed business is a surfshop aas well a an ice cream shop an analysis of the best time of the year to surf at differnt locations in Oahu would be helpfull in finding the best locations to place the business. The National Oceanic and Atmospheric Administration's (NOAA) National Weather Service's (NWS) National Data Bouy Center website (https://www.ndbc.noaa.gov/)provides access to ocean data bouys at locations around the island of Ohau.



