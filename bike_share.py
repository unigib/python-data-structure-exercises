# This program analyses a small bike-share service's trip records from
# bike_share.json. Each trip stores station IDs, while station details are
# kept in a separate dictionary.
#
# When the program is run, it should display a report about the trips.

import json
from pathlib import Path

data_file = Path(__file__).with_name('bike_share.json')
with data_file.open(encoding='utf-8') as file:
    data = json.load(file)

stations = data['stations']
trips = data['trips']

print('There are {} stations and {} trips'.format(len(stations), len(trips)))


# TODO: Write code to answer the following questions:
# * Which station was the most popular starting point?
# * Which station was the most popular destination?
# * What was the average trip duration?
# * Were member or casual riders responsible for more trips?
# * Which hour of the day had the most trips start?

# TODO (extra):
# * Display a report with trip counts and average duration for each rider type.
# * For each station, calculate the net flow: arrivals minus departures.
# * Find the busiest calendar day and report its number of trips.