import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# 执行API调用并存储响应
# 将响应对象存储在r中
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)


# 状态码为200表示请求成功
def get_status_code(r):
    """r是一个响应对象"""
    return r.status_code


print("Status code:", get_status_code(r))
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 研究有关仓库的信息，所有仓库在items对应的值里，也是一个一个字典
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))
names = [repo_dict['name'] for repo_dict in repo_dicts]
stars = [repo_dict['stargazers_count'] for repo_dict in repo_dicts]

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
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

# 自定义工具提示标签，根据value生成高度
plot_dicts = []
for repo_dict in repo_dicts:
    if repo_dict['description'] != None:
        plot_dict = {'value': repo_dict['stargazers_count'],
                     'label': repo_dict['description'],
                     'xlink': repo_dict['html_url'],
                    }
    else:
        plot_dict = {'value': repo_dict['stargazers_count'],
                     'label': "No information",
                     'xlink': repo_dict['html_url'],
                     }
    plot_dicts.append(plot_dict)


chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')