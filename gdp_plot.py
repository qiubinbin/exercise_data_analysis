import json
import pygal
from pygal.style import LightColorizedStyle
from pygal.style import RotateStyle

from country_codes import get_country_code
filepath='gdp_json.json'
with open(filepath,'r') as temp:
	gdp=json.load(temp)
gdp_countries_2016={}
for index in gdp:
	if index["Year"]==2016:
		value=index["Value"]
		country=index["Country Name"]
		code=get_country_code(country)
		if code:
			gdp_countries_2016[code]=float(value)
style_temp = RotateStyle(color="#4b5cc4",base_style=LightColorizedStyle)
gdp_show=pygal.maps.world.World(style=style_temp)
gdp_show.title="GDP_2016"
gdp_show.add("GDP2016",gdp_countries_2016)
gdp_show.render_to_file("GDP_2016.svg")
