####################################################################################################################
# Program containing the classes and functions necessary to download air quality data relative to my sensor.
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
import pandas as pd
from tqdm import tqdm
from dateutil.relativedelta import relativedelta
from modules import dic_sensors, installation_date, initial_url


class DownloadData:

    def __init__(self):
        self.initial_url = initial_url
        self.installation_date = installation_date
        self.dic_sensors = dic_sensors

    def download_data(self, index):

        if str.lower(index) == 'pm' or str.lower(index) == 'meteo':
            try:
                df_data_all = pd.read_csv(f'data/{str.upper(index)}_data.csv', index_col=0, parse_dates=True)
                latest_date = df_data_all.index.max() + relativedelta(days=1)
            except FileNotFoundError:
                df_data_all = pd.DataFrame()
                latest_date = self.installation_date

            date_interval = (datetime.datetime.now() - latest_date).days

            for i in tqdm(range(date_interval)):
                date_format = f'{latest_date.year}-{"{:02d}".format(latest_date.month)}-' \
                              f'{"{:02d}".format(latest_date.day)}'

                data_url = f'{self.initial_url}{date_format}/{date_format}_{self.dic_sensors[str.upper(index)]}.csv'
                try:
                    df_data = pd.read_csv(data_url, sep=';')
                    df_data = df_data.set_index(pd.to_datetime(df_data['timestamp'])).drop('timestamp', axis=1)
                    df_data_all = pd.concat([df_data_all, df_data])
                    latest_date += relativedelta(days=1)
                except Exception as x:
                    if x.code == 404:
                        latest_date += relativedelta(days=1)
                        print(f'Data for {date_format} not available')
                        continue
                    else:
                        raise

            df_data_all.to_csv(f'data/{str.upper(index)}_data.csv')
            return df_data_all
        else:
            return f"ERROR: {index} value not valid!"
