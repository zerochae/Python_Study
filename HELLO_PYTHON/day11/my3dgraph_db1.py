import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d


from daoStock import StockDao

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

se = StockDao()

name = se.nameSelect()

for i,j in enumerate(name) :
    xs = np.zeros(8) + i
    ys = [0,1,2,3,4 ,5,6,7]
    zs = se.select100(j)
    ax.plot(xs,ys,zs)

plt.show()



