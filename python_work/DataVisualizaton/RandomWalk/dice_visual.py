import matplotlib.pyplot as plt
from PygalEg.die import Die

die = Die()
results = [die.roll() for roll_num in range(1000)]
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

plt.title("Result in Matplotlib", fontsize=15)
plt.xlabel("Result")
plt.ylabel("Frequency of Result")

x_values = list(range(1, die.num_sides + 1))
print(x_values)
print(frequencies)
plt.scatter(x_values, frequencies, c=(0, 0, 0.3),
            edgecolors='none', s=50)
plt.plot(x_values, frequencies, color='b', linestyle='--', linewidth=1)
plt.show()