import pygal
from PygalEg.die import Die

die = Die()
results = [die.roll() for roll_num in range(1000)]

# 分析频次
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]


# 可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(1, 7))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')