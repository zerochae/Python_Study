import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

from daoStock import StockDao

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

se = StockDao()


xs = [0,0,0,0,0 ,0,0,0]
ys = [0,1,2,3,4 ,5,6,7]
# zs = [70300,70300,70300,70300,70300,70300,70300,70300]
zs = se.select("삼성전자")

ax.plot(xs,ys,zs,'black')

plt.show()



