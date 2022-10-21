import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
    # Построение случайного блуждания.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Нанесение точек на диаграмму.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth = 10)
    # Удаление осей.
    ax.get_xaxis().set_visible(False)

    ax.get_yaxis().set_visible(False)

    plt.show()

    break