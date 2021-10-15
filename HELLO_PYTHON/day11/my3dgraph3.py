import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

from daoStock import StockDao

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

se = StockDao()

ax.plot([0, 0, 0], [0, 1, 2], [0, 1, 0], 'r')
ax.plot([1, 1, 1], [0, 1, 2], [0, -1, 0], 'b')
ax.plot([2, 2, 2], [0, 1, 2], [0, 0, 0], 'g')
ax.plot([3, 3, 3], [0, 1, 2], [0, 0, 0], 'black')
ax.plot([4, 4, 4], [0, 1, 2], [0, 0, 0], 'purple')

list = se.select("삼성전자")

print(list)

plt.show()
