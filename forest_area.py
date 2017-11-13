import csv
import pygal
from pygal.style import RotateStyle

from country_codes import get_country_code

filepath = "API_AG.LND.FRST.K2_DS2_en_csv_v2.csv"
with open(filepath, mode='r', encoding='gb18030', errors='ignore') as temp:
	frst = csv.reader(temp)
	temp1 = next(frst)
	temp1 = next(frst)
	temp1 = next(frst)
	temp1 = next(frst)
	numbers = {}
	for row in frst:
		country = row[0]
		code = get_country_code(country)
		number = row[-1]
		if code:
			numbers[code] = number
	style_forest = RotateStyle(color="#40de5a")
	show_number = pygal.maps.world.World(style=style_forest)
	show_number.title = "Forest"
	show_number.add("forest_lastest", numbers)
	show_number.render_to_file("Forest.svg")
