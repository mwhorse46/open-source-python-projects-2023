import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()
# left = 0
# right = 20



def animate(i):
    left = 0
    right = 20

    data = pd.read_csv('data.csv')
    x = data['Time']
    y1 = data['lane_1']
    y2 = data['lane_2']
    y3 = data['lane_3']
    y4 = data['lane_4']

    plt.cla()

    plt.plot(x, y1, label='Lane 1')
    plt.plot(x, y2, label='Lane 2')
    plt.plot(x, y3, label='Lane 3')
    plt.plot(x, y4, label='Lane 4')

    plt.legend(loc='upper left')
    plt.tight_layout()
    


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
