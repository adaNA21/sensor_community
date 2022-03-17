import datetime

# Sensors id
pm_sensor_id = 70241
weather_sensor_id = 70242

# Sensors names
pm_sensor_name = f'pms5003_sensor_{pm_sensor_id}'
meteo_sensor_name = f'bme280_sensor_{weather_sensor_id}'
dic_sensors = {'PM': pm_sensor_name, 'METEO': meteo_sensor_name}

# Date when the setting was installed
installation_date = datetime.datetime.strptime('2022-02-08', '%Y-%m-%d')

# Url were sensor community data are stored
initial_url = "https://archive.sensor.community/"
