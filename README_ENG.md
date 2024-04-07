________________________________________________________

![image](https://github.com/simonlobgromov/climate_proj_kg/assets/131668061/6ecd0a9a-8fa6-4947-982f-184d8edca21c)

# Visualization of Climate Indicators for Kyrgyzstan

# Introduction

In an era of perceptible climate changes exerting global impact on the natural systems of our planet, the importance of accurate and timely monitoring of natural resources and ecosystems becomes increasingly evident. One of the most important aspects of this monitoring is the study and analysis of snow cover, which plays a key role in the Earth's climate system, hydrology, and water resources. Specifically, for mountainous regions such as Kyrgyzstan, where glaciers and snow reserves are vital sources of fresh water, understanding the dynamics of snow cover is of particular relevance.

Modern remote sensing technologies and the analysis of satellite data open new horizons in the study of natural processes. In particular, the use of tools such as the Normalized Difference Snow Index (NDSI) and surface temperature measurements obtained from NASA satellite data allows for high-precision determination of the state and dynamics of snow cover. These parameters form the basis for assessing the current state of glaciers, their changes over time, and for predicting future changes associated with global warming.

The present work is dedicated to the analysis of snow cover dynamics based on satellite data in the context of assessing the state of Kyrgyzstan's glacial system. The study aims to identify trends in changes in snow cover and temperature conditions that may have long-term consequences for the region's water resources, ecosystems, and the socio-economic well-being of the population. The work presents the results of visualization and analysis of the obtained data, which allows conclusions to be drawn about the current state and trends in changes in glaciers and snow cover in Kyrgyzstan, as well as to assess potential risks and challenges facing the region in the near future.

Observations of snow cover and glaciers can be divided into two main types:

* **Instrumental**. Carried out directly on the terrain and include laboratory research with taken materials.
* **Remote**. Carried out via aerial photography or based on satellite data.

Although quality research often requires a combination of both approaches to obtain the most accurate and comprehensive picture, our work focuses on developing a monitoring methodology based exclusively on satellite data analysis. This approach allows us to cover large territories and get a generalized view of the dynamics of snow cover and the state of glaciers, which is especially valuable for regions with limited access or where traditional ground measurements are difficult or impossible.


# Method

In this section, we describe the analysis methods based on the study of the optical properties of snow and ice. The optical and infrared ranges allow us to assess the reflective characteristics of the snow cover, which is important for identifying its condition and changes. The application of different spectral channels is due to their sensitivity to specific snow parameters, including density, structure, and surface temperature. The choice of suitable spectral channels for monitoring purposes, as well as approaches to the processing and interpretation of satellite data, are discussed. This is a highly scientific topic, and we have taken the first step in this direction.

For the assessment of snow cover based on optical and infrared data, the following key metrics are used:

* **Normalized Difference Snow Index (NDSI)**: Used to assess the presence and extent of snow cover on the Earth's surface, based on the difference in reflective properties of snow in the visible and near-infrared spectrum.

* **Ice Cover Index**: Similar to NDSI but adapted for identifying and assessing icy and frozen surfaces, especially useful for glaciological studies.

* **Surface Temperature (LST - Land Surface Temperature)**: Reflects the temperature of the Earth's surface, including snow and ice, which is critical for assessing melting and freezing processes.

* **Albedo**: Describes the ability of a surface to reflect sunlight, which is especially important for snow and ice cover, as the high albedo of snow and ice affects the climate and energy balance.

* **Vegetation Area Index (NDVI)**: Although primarily used to assess vegetation, NDVI can serve as a secondary indicator of snow cover, as snow affects vegetation cover indicators.

* **Snow Depth**: While optical satellite data do not allow precise measurement of snow depth, indirect methods and modeling based on satellite data can provide depth estimates.

* **Snow Moisture**: An important parameter affecting avalanche risk and snow's effectiveness in absorbing water can be assessed through indirect satellite measurements and modeling.

* **Relief Map**: To assess processes in the snow and ice cover, it is necessary to accurately know the level of altitude above sea level, the angle of the slope surface, and the slope's exposure due to the dependence of these features on thermodynamic regimes.

* **Water Transparency in Inland Bodies of Water**: Turbidity indicates the presence of suspended microparticles in the water, which is an indicator of intense melting of perennial ices when rock particles included in the glacier body are released.

*

 **Historical Meteorological Data**: Data from weather stations on air temperature, precipitation, wind...

It can be seen that this is a fundamental study requiring deep analysis of the collected large volumes of data. At the moment, we have collected data from 2005 to the present time and have made a general analysis of them according to such features:

* **Normalized Difference Snow Index (NDSI)**
* **Surface Temperature (LST - Land Surface Temperature)**
* **Relief Map** (Elevation Model)

## MODIS

[MODIS](https://www.earthdata.nasa.gov/) (Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard NASA's Terra and Aqua satellites launched to observe Earth. MODIS is capable of collecting data in a wide range of wavelengths, allowing for diverse information about the state of the atmosphere, oceans, clouds, and the Earth's surface, including vegetation, snow cover, and glaciers.

## MODIS/Terra Snow Cover Daily L3 Global 500m SIN Grid V061

MODIS/Terra Snow Cover Daily L3 Global 500m SIN Grid V061 is a NASA satellite product for monitoring snow cover on a daily basis with global coverage and 500-meter resolution. Using data from the MODIS instrument on board the Terra satellite, this product calculates the Normalized Difference Snow Index (NDSI), which helps identify snow and effectively detects cloudiness and water surfaces for a more accurate assessment of snow cover. NDSI is calculated using the formula:

$$ NDSI= \frac {Green−SWIR}{Green+SWIR} $$

where "Green" denotes the reflection in the green spectrum, and "SWIR" — reflection in the short-wave infrared spectrum. This index is particularly useful for determining snow cover, as snow has high reflectance in the visible range and low in the infrared.

We receive the data in the form of a numerical array (table) for the specified observation polygon corresponding to the territory of Kyrgyzstan. Values can be interpreted according to this description:

```
{'long_name': 'NDSI snow cover from best observation of the day',
 'units': 'none',
 'valid_range': [0, 100],
 '_FillValue': 255,
 'missing_value': 200,
 'Key': ' 0-100=NDSI snow, 200=missing data, 201=no decision, 211=night, 237=inland water, 239=ocean, 250=cloud, 254=detector saturated, 255=fill'}
```

Where for all values from 0 to 100 we understand that this is the value of NDSI, scaled to this range. Taking into account the scale of observation, we understand that each value in the table (pixel) corresponds to a ground surface area of 500 by 500 meters. The value of 0 defines a surface completely devoid of snow cover, and a value of 100 corresponds to freshly fallen snow.

If we visualize the data for one calendar day of observations, we get a similar illustration:

![image](https://github.com/simonlobgromov/climate_proj_kg/assets/131668061/31afde72-2fac-4a84-9daa-2f634c41f260)

We can see that a large territory on the selected polygon is occupied by clouds, and the data contain artifacts in the form of unrecognized areas, which greatly complicates the analysis. In search of a solution to this problem, the idea was formulated that at least once a month every pixel was unequivocally identified as the Earth's surface, and it was assigned an NDSI value. Therefore, it was decided to filter only those pixels for which NDSI is known for each day of the month and to summarize all results for the month by averaging the index values. We also left those pixels empty, which correspond to the water surface (lakes, rivers, reservoirs). We got such a result, where there are no clouds and artifacts:

![image](https://github.com/simonlobgromov/climate_proj_kg/assets/131668061/e805624c-9282-4c9f-baf5-d86d0360fe36)

The image shows the aggregated NDSI for May 2023. The color corresponds to the value of NDSI from 0 (blue, absence of snow) to 100 (red, fresh snow). White color corresponds to water bodies. It is understood that fresh snow has special optical properties, and it is well distinguished optically. Over time, snow compacts, due to solar radiation its surface thaws, and the resulting ice crust changes its reflective properties, along with which NDSI decreases. NDSI close to maximum values characterizes those territories where snow falls regularly.

The attempt to summarize NDSI over a shorter time interval (for example, for 10 days) proved to be not very convenient due to the fact that, firstly

, it is not possible to completely exclude cloudiness, and secondly, this leads to the need to process a significantly larger volume of data. However, in the future, we will do a more detailed analysis, summarizing over a shorter time interval.

In the work, we calculated the statistics of the dynamics of changes in NDSI by month from January 2005 to the present time with reference to the altitude above sea level and built graphs. Also, based on NDSI data, we determined the approximate snow line for each calendar year.

## MODISAqua Land Surface Temperature3-Band Emissivity Daily L3 Global 1km SIN Grid Night V061

MODIS/Aqua Land Surface Temperature 3-Band Emissivity Daily L3 Global 1km SIN Grid Night V061 is a satellite product providing daily data on the land surface temperature (LST) and emissivity in three spectral channels with a resolution of 1 km. Data are collected by the MODIS instrument on the Aqua satellite during **nighttime**, which allows minimizing the influence of solar radiation and more accurately assess the thermal radiation of the Earth's surface. This product uses the sinusoidal grid (SIN Grid) for global coverage and has high precision due to a complex calculation methodology, including the emissivity of the surface.

Surface temperature (LST) is assessed based on radiance measured in the infrared range, taking into account the surface emissivity in three channels. Emissivity, in turn, characterizes the ability of a surface to emit energy in the form of heat and is a key parameter for accurate LST determination. The calculation of LST and emissivity can be expressed through formulas based on Planck's law of radiation, radiation transfer equations, and correction of atmospheric effects, but precise algorithms include complex models and calibrations, specific for each spectral channel and observation conditions.

We receive the data in the form of a numerical array (table) for the specified observation polygon, corresponding to the territory of Kyrgyzstan. Values can be interpreted according to this description:

```
{'long_name': 'Daily 1km Land-surface Temperature',
 'units': 'K',
 'scale_factor': 0.02,
 'add_offset': 0.0,
 'valid_range': [7500, 65535],
 '_FillValue': 0}
```
Where each value (pixel) corresponds to a territory area of $1 km^2$, and if the pixel value lies within the range of values $value$ &isin; $[7500, 65535]$, then we speak of the fact that we can determine the temperature value in Celsius for this pixel. The temperature conversion was performed using the formula:

$$T = value*0.02 - 273$$
Where $T$ is the temperature in degrees Celsius.

When analyzing the data, all the same problems were solved as for NDSI. Day observation data have extraneous values in the form of cloudiness, artifacts, and abnormal temperature values. This is what the visualization of one day of observation looks like:

![image](https://github.com/simonlobgromov/climate_proj_kg/assets/131668061/51683641-b8c6-4e7b-9164-d1a730b132a6)

After summarizing for the month and removing anomalies, we received averaged data for each month. It should be said that the surface temperature cannot change as rapidly as the air temperature. Also, for understanding the general temperature regime, we considered averaging the data for the month acceptable at this stage. Even when averaging for a month, we observe many unidentified pixels.

Below is an example of visualizing data on temperature for May 2023:

![image](https://github.com/simonlobgromov/climate_proj_kg/assets/131668061/afa75cd8-5f41-42d7-a415-224de1a12c76)


## ASTER Global Digital Elevation Model

The ASTER Global Digital Elevation Model (GDEM) is the result of a collaboration between NASA and the Ministry of Economy, Trade, and Industry of Japan (METI). This tool is a digital elevation model that provides detailed representation of the Earth's relief on a global level. ASTER GDEM is created based on data collected by the Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) instrument, which is installed on the Terra satellite launched by NASA.

We have received these high-resolution data in the form of multiple numerical arrays, which we have combined to create a height map for the territory of Kyrgyzstan.

![image](https://github.com/simonlobgromov/climate_proj_kg/assets/131668061/8dcb6f0f-8ad8-49d1-b995-aad2437cc9d7)

Next, it was necessary to correlate elevation values with NDSI and Surface Temperature data, for which coordinate grids were created. Coordinate grids were calculated based

 on the known coordinates of the polygon vertices using linear interpolation, for which coordinates were taken in the format "EPSG:3857". This format uses the Mercator projection, which represents the Earth's surface on a plane so that all meridians are parallel lines. The comparison of NDSI and Surface Temperature data with the elevation map was carried out by methods of mathematical modeling. Thus, for each pixel (a section of the Earth's surface 500 by 500 meters), we knew not only the snow index and temperature but also the altitude above sea level. This approach will be extended to new climatic data in the future.

## Elevation Gradient

To describe the terrain, we need to know not only the elevation but also the degree of elevation change and for each slope it is important to know its exposure - that is, to which side of the world the slope is facing. It is a known fact that the southern slopes are more often blown by winds, as a result of which there are more dynamic ascending flows and abundant cloud formation there. We have confirmed the fact that the southern slopes are more snow-covered due to more frequent precipitation.

So additional data on the relief were obtained. Here is an example illustration based on the relief gradient map: (The illustration has a distortion and does not correspond to the cartographic picture of the relief, as this picture is adapted to the polygon of observations for climatic data, which has the shape of a parallelogram)

![image](https://github.com/simonlobgromov/climate_proj_kg/assets/131668061/7a62db4b-6cd8-4f3d-ab60-0ac988e39b5c)

We have maps correlated with NDSI and surface temperature maps:
* With angles of slope inclination in degrees calculated by formulas

$$ (\frac{\partial h}{\partial l})_{max} = |\bigtriangledown h|_2 = \sqrt{(\frac{\partial h}{\partial x})^2 + (\frac{\partial h}{\partial y})^2} $$

$$ \alpha_{slope} = \arctan{(\frac{(\frac{\partial h}{\partial l})_{max}}{| dx, dy|_2})} $$

* With angles of slope exposure in degrees (0 - the slope is facing North, 90 - East, 180 - South, 270 - West)

Here is a visualization of the slope angle, where black color corresponds to flat areas, light describes steep slopes, the angle of which reaches 88 degrees:

![image](https://github.com/simonlobgromov/climate_proj_kg/assets/131668061/6505c5be-0d10-41cc-811a-de38b04cf153)




# Statistics and Visualization

Our study precedes a preliminary analysis of the obtained data. Based on them, dashboards were built, which are saved in this repository as Jupyter notebooks. A more detailed description of the proposed graphs is inside each file.

* `NDSI_Visualization_script.ipynb`
* `Surface_Temperature_Visualization_script.ipynb`
* `Snow_Line_Visualization_script.ipynb`

# Results

As part of our research, we conducted analyses of NDSI, snow line, and surface temperature time series based on satellite data for the period from 2005 to the current year. Despite clearly expressed seasonal fluctuations, no significant long-term trends were found that would indicate a change in the temperature regime or a stable decrease in snowiness in the studied altitude zones. These observations may suggest that the region under consideration is not yet significantly affected by global warming, at least within the scope of the features and time interval considered. However, the absence of identified trends does not exclude the need for further research. To gain a more detailed understanding of the potential impact of climatic changes on the snow cover, it is necessary to conduct a comprehensive analysis, involving additional data and new features such as models of atmospheric precipitation, thermal characteristics of the snow cover, albedo, mass and energy balance, and others. It is also important to use advanced analytical methods to identify less obvious changes and trends, which will allow for more substantiated conclusions about the dynamics and state of snow cover in the future.
