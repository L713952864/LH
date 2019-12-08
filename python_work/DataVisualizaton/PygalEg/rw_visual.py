import pygal
from RandomWalk.random_walk import RandomWalk

rw = RandomWalk(100)
rw.fill_walk()
values = [rw.x_values, rw.y_values]
values_list = [i for i in zip(*values)]

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Correlation'


xy_chart.add('起始点', [values_list[0]])
xy_chart.add('A:1-30', values_list[1:31])
xy_chart.add('B:31-60', values_list[31:61])
xy_chart.add('C:61-98', values_list[61:99])
xy_chart.add('终止点', [values_list[-1]])

xy_chart.render_to_file('rw_visual.svg')

