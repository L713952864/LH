import json
import pygal
import pygal_maps_world.maps
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from CSVandJsonVisual.country_codes import get_country_code

filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)

cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp = gdp_dict['Value']
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for code, gdp in cc_gdp.items():
    if gdp < 10**10:
        cc_gdp_1[code] = gdp
    elif gdp < 10**12:
        cc_gdp_2[code] = gdp
    else:
        cc_gdp_3[code] = gdp
print(len(cc_gdp_1), len(cc_gdp_2), len(cc_gdp_3))
wm_style = RS('#e49898', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World GDP in 2016, by Country'
wm.add('0-10bn', cc_gdp_1)
wm.add('10bn-1tn', cc_gdp_2)
wm.add('>1tn', cc_gdp_3)

wm.render_to_file('world_gdp.svg')
