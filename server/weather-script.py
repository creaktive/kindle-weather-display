#!/usr/bin/python2

# Kindle Weather Display
# Matthew Petroff (http://www.mpetroff.net/)
# September 2012

import urllib2
from xml.dom import minidom
import datetime
import codecs



#
# Download and parse weather data
#

# Fetch data (change lat and lon to desired location)
CODE = '727232'
weather_xml = urllib2.urlopen('http://weather.yahooapis.com/forecastrss?w=' + CODE + '&u=c').read()
dom = minidom.parseString(weather_xml)

# Parse temperatures
xml_temperatures = dom.getElementsByTagName('yweather:forecast')
dates = [None]*5
highs = [None]*5
lows = [None]*5
icons = [None]*5
i = 0
for item in xml_temperatures:
    dates[i] = item.getAttribute('date')
    highs[i] = int(item.getAttribute('high'))
    lows[i] = int(item.getAttribute('low'))
    image_url = 'icons/' + item.getAttribute('code') + '.svg'

    f = codecs.open(image_url ,'r', encoding='utf-8')
    f.readline()
    icons[i] = f.readline()
    f.close()

    i = i + 1

# Parse dates
xml_day_one = dates[0]
day_one = datetime.datetime.strptime(xml_day_one, '%d %b %Y')



#
# Preprocess SVG
#

# Open SVG to process
output = codecs.open('weather-script-preprocess.svg', 'r', encoding='utf-8').read()

# Insert icons and temperatures
output = output.replace('ICON_ONE',icons[0]).replace('ICON_TWO',icons[1]).replace('ICON_THREE',icons[2]).replace('ICON_FOUR',icons[3])
output = output.replace('HIGH_ONE',str(highs[0])).replace('HIGH_TWO',str(highs[1])).replace('HIGH_THREE',str(highs[2])).replace('HIGH_FOUR',str(highs[3]))
output = output.replace('LOW_ONE',str(lows[0])).replace('LOW_TWO',str(lows[1])).replace('LOW_THREE',str(lows[2])).replace('LOW_FOUR',str(lows[3]))

# Insert days of week
one_day = datetime.timedelta(days=1)
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
output = output.replace('DAY_THREE',days_of_week[(day_one + 2*one_day).weekday()]).replace('DAY_FOUR',days_of_week[(day_one + 3*one_day).weekday()])

# Write output
codecs.open('weather-script-output.svg', 'w', encoding='utf-8').write(output)
