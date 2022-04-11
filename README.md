# surfs_up

## Project Overview 
The project intailed an analysis the temperature trends for the months of June and December in Oahu, Hawaii, in order to evaluate the year-round sustainability of a surf and ice cream shop. Python, Pandas, SQLite and SQLAlchemy were used to perform this analysis.

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

#### Total precipitation levels and amount of precipitation at the most active stations for June and December

    #December
    session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()
    session.query(Measurement.prcp).filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 6).all()
    #June
    session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 12).all()
    session.query(Measurement.prcp).filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 12).all()

#### Swell Analysis

Given that this proposed business is a surfshop as well a an ice cream shop an analysis of the best time of the year to surf at differnt locations in Oahu would be helpfull in finding the best locations to place the business. In addition, an analysis of the surfing conditions will help the shop staff make sure that the shop has the right surf gear for the surf conditions. The National Oceanic and Atmospheric Administration's (NOAA) National Weather Service's (NWS) National Data Bouy Center (NDBC) website (https://www.ndbc.noaa.gov/) provides access to ocean data bouys at locations around the island of Ohau.  Based on the latitude/longitude of the weather stations used for the weather analysis I plotted the locations of the stations using Gmap to see which parts of the island we analysed the weather.

        #plot the weather station locations
        import gmaps
        # Import API key
        from config import Google_API_KEY
        # Configure gmaps API key
        gmaps.configure(api_key=Google_API_KEY)
        HI_coord = (21.5, -158.05)
        fig = gmaps.figure(center=HI_coord, zoom_level=9.5)
        #heat_layer = gmaps.heatmap_layer(locations, weights=max_temp,dissipating=False,
                     #max_intensity=300, point_radius=4)
        marker_layer = gmaps.marker_layer(locations)
        #fig.add_layer(heat_layer)
        fig.add_layer(marker_layer)

#### Map of Weather Station Locations
![image](https://github.com/blueschistrocks/surfs_up/blob/0cc29b70920aa723027dcbd61d6ea92d370e70a4/Images/Gmap-Oahu.png)

Most of the stations are located along the northeastern and southern facing shore. If a shop is to be located in these areas data on the swell height, power and direction during different times of the year would be useful in determining when to expect higher customer visits and types of surfing gear they may need. Since the northeastern shore faces northeast swell from between 0 and 95 degrees may provide the best surf. The southern shore faces south swell from 95 to 270 degrees may provide the best surf. I obtained data from the NDBC for Station 51004 - Southeast Hawaii, which is located to the southeast of the Hawaian Islands. Using Pandas and MatplotLib I did some minor ETL and graphed the relevent swell data.

#### Plot of Data Buoy Data
![image](https://github.com/blueschistrocks/surfs_up/blob/1a99672ddd23b2b7a349e6d867ba13ef68e3dc51/Images/DataBouy_plot(2021).png)

A review of the plot inidcates that there appears to be plenty of swell year round for both the northeastern and southern shores. However the swells arriving from the northeast appear to have the highest swell hieghts and have the highest swells between December and March. Swell peroid is a good indicator of the power of a swell, generally the swell peroid tends to be higher with the northeast swells.

Based on this review a shop located along the northeast shore should have swell year round with the biggest and most powerfull swells in the winter.  Bigger swells usually mean more broken surfboards, so the staff in the shop should plan to have plently of heavey duty surf gear, surfboard repair kits and new surfboards on hand because Burkhart breaks boards Barney, like for fun!
