####################################################################################################################
# Code to define fix parameters for the data download
# Copyright (C) 2022 Andrea Di Antonio
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
####################################################################################################################


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
