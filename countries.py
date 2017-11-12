from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES):
	print(country_code, COUNTRIES[country_code])
print(COUNTRIES.items())
