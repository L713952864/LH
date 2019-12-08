import matplotlib.pyplot as plt
from RandomWalk.random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸，单位为英寸，dpi为分辨率
    plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.scatter(rw.x_values, rw.y_values, c=list(range(rw.num_points)),
                cmap = plt.cm.Blues, edgecolors='none', s=10)
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=50)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    flag = input("proceed? (y/n):")
    if flag == 'n':
        break