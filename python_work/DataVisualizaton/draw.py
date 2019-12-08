import matplotlib.pyplot as plt


def look_better(x_axis, y_axis):
    plt.title("Cube Numbers", fontsize=20)
    plt.xlabel("X", fontsize=12)
    plt.ylabel("Y", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.axis([0, x_axis, 0, y_axis])


def plot_1():
    x_values = list(range(1, 6))
    y_values = [i**3 for i in range(1, 6)]
    plt.plot(x_values, y_values, color='b', linestyle='--',
             label='data', linewidth=1)
    plt.scatter(x_values, y_values, c=(0, 0.4, 0.8), edgecolors='none', s=40)
    plt.show()


def plot_2():
    x_values = list(range(0, 5000))
    y_values = [i**3 for i in range(0, 5000)]
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,
                edgecolors='none', s=3)
    plt.savefig('Cube_plot.png', bbox_inches='tight')
    plt.show()


look_better(10, 150)
plot_1()
look_better(5000, 5000**3)
plot_2()