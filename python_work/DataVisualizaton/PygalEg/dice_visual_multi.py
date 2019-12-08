import pygal
from PygalEg.die import Die

die_1 = Die()
die_2 = Die()
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# 分析频次
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]


# 可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = list(range(1, max_result))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual_multi.svg')