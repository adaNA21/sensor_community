####################################################################################################################
# Program to download air quality data relative to my sensor.
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

# Import packages and modules
from modules import Modules

# Initialise functions
download_data = Modules.DownloadData()

# Download PM data
df_pm = download_data.download_data('pm')

# Download Meteorological data
df_meteo = download_data.download_data('meteo')

print('Download completed!')
