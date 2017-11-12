from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
	"""根据制定的国家，返回该国家的二字国别码"""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	if country_name == "Yemen, Rep.":
		return 'ye'
	# 没找到时返回None
	return None

# print(get_country_code("Andorra"))
