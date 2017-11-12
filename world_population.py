import json
import pygal
from pygal.style import RotateStyle  # 设置图表颜色
from pygal.style import LightColorizedStyle

from country_codes import get_country_code

wm_style = RotateStyle(color="#336699",base_style=LightColorizedStyle)  # 设置十六进制颜色
# wm_style1=LightColorizedStyle(background='white',foreground='a(0,255,0,0.7)')
wm = pygal.maps.world.World(style=wm_style)
wm.title = "Population"
filepath = 'population_data.json'
with open(filepath, 'r') as temp:
	populatuon = json.load(temp)
populatuon2010 = []
countries2010 = []
# 创建一个包含人口数量的字典
cc_population = {}
for index in populatuon:
	if index["Year"] == "2010":
		population_temp = index["Value"]
		populatuon2010.append(int(float(population_temp)))  # 带小数点的字符串先转换成浮点数再转换成整数
		country_code = index["Country Name"]
		code = get_country_code(country_code)
		if code:
			cc_population[code] = int(float(population_temp))
		# print(code+": "+population_temp)
		else:
			print('ERROR-' + country_code)
		countries2010.append(code)
cc_population_1, cc_population_2, cc_population_3 = {}, {}, {}
for cc, pop in cc_population.items():
	if pop < 10000000:
		cc_population_1[cc] = pop
	elif pop < 100000000:
		cc_population_2[cc] = pop
	else:
		cc_population_3[cc] = pop
print(len(cc_population_1), len(cc_population_2), len(cc_population_3))
# 人数分组
wm.add("0-10M", cc_population_1)
wm.add("10M-1BN", cc_population_2)
wm.add(">1BN", cc_population_3)
wm.render_to_file("population2010.svg")
# with open("population2010.json",'w') as temp:
# 	json.dump(populatuon2010,temp)
# print(populatuon2010)
# print(countries2010)
