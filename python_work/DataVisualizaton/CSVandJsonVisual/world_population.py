import json
import pygal
import pygal_maps_world.maps
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
from CSVandJsonVisual.country_codes import get_country_code

# 把数据加载到列表中
filename = 'data_json.json'
with open(filename) as f:
    pop_data = json.load(f)
# 创建一个包含人口数量的字典：key-code value-population
cc_populations = {}
cnt = 0
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            print("___" + country_name)
            cnt += 1
print(cnt)
# 根据人口数量分组
cc_pops_1, cc_pops_2, cc_pops_3, cc_pops_4 = {}, {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10**6:
        cc_pops_1[cc] = pop
    elif pop < 10**7:
        cc_pops_2[cc] = pop
    elif pop < 10**9:
        cc_pops_3[cc] = pop
    else:
        cc_pops_4[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3), len(cc_pops_4))

# 创建实例并设置样式
# 参数为十六进制的RGB颜色，详细百度：hex color chooser(十六进制颜色选择器）
wm_style = RS('#336699', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)


wm.title = 'World Population in 2010, by Country'
wm.add('0-1m', cc_pops_1)
wm.add('1m-10m', cc_pops_2)
wm.add('10m-1bn', cc_pops_3)
wm.add('>1bn', cc_pops_4)


wm.render_to_file('world_population.svg')


