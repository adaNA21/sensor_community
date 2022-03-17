import datetime
# Sensors id
pm_sensor_id = 70241
temp_sensor_id = 70242

# Sensors names
pm_sensor_name = f'pms5003_sensor_{pm_sensor_id}'
temp_sensor_name = f'bme280_sensor_{temp_sensor_id}'

# Date when the settings was installed
installation_date = datetime.datetime.strptime('2022-02-08', '%Y-%m-%d')
