# Sensor community repo

## Scope

This repository contains the code to download and plot the data relative to my air quality sensor, part of the [Lufdaten](https://maps.sensor.community/#2/0.0/0.0) project. 

## Requirements

To run the analysis contained in this repository, it is strongly recommended to install [Anaconda](https://www.anaconda.com/products/individual). This repo contains a `conda environment` file that will install all the necessary packages.  

### Activate anaconda environment
Firstly, open the Anaconda prompt and navigate to where the `sensor_community` folder is stored on your local machine using the command\
\
`cd path/to/folder`\
\
Then create and activate the anaconda environment for the project, called `SensorCommunity`, by running the following commands\
\
`conda env create -f environment.yml` \
`conda activate SensorCommunity`

## Run the code

To download the data and store them in the `data` folder, run the following command within your Anaconda terminal: 

`python download_data.py`

To produce plots and analyses with the data, run the `Sensor_community_plot` Jupyter Notebook. 

# Warning

Between 19th March 2022 and 19th April 2022, the sensor was removed for maintenance. 
Between 26th May 2022 and 17th July 2022, the sensor was again removed for maintenance. 
Therefore, no data is available for this time window.
