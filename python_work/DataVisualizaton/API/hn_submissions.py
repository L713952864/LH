import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter
# 网址里是topstorty的ID
URL = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(URL)
print("Status code:", r.status_code)

submission_ids = r.json()
submission_dicts = []
# 对于前30的每一个ID
for submission_id in submission_ids[0:30]:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json'
    req = requests.get(url)
    submission_dicts.append(req.json())

"""
for submission_dict in submission_dicts:
    print('\nTitle: ', submission_dict['title'])
    print('Discussion LinK: ', submission_dict['url'])
    print('Comment: ', submission_dict['descendants'])
"""

titles = [submission_dict['title'] for submission_dict in submission_dicts]
plot_dicts = []
for submission_dict in submission_dicts:
    if submission_dict['descendants'] != 0 and dict.get(submission_dict, 'url'):
        plot_dict = {'value': submission_dict['descendants'],
                     # 'label': submission_dict['kids'],  # submission_dict['kids']是一个列表
                     'xlink': submission_dict['url'],
                     }

    elif not dict.get(submission_dict, 'url'):
        plot_dict = {'value': submission_dict['descendants'],
                     # 'label': 'None',
                     'xlink': 'No url',
                     }
    plot_dicts.append(plot_dict)

# 定制图标外观（改进）
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14  # 副标签
my_config.major_label_font_size = 18  # 主标签
my_config.truncate_label = 15  # 将较长的项目名缩短为15个字符
my_config.show_y_guides = False
my_config.width = 1000
# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Commented Stories on Hacker News'
chart.x_labels = titles

chart.add('', plot_dicts)
chart.render_to_file('hn_submissions.svg')