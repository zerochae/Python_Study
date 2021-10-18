import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

from daostock2 import StockDao2



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

se = StockDao2()

name = se.selectName()


for i,j in enumerate(name) :

    if i == len(name)-1 : break

    zs = se.selectPrice(name[i])
    xs = np.zeros(len(zs))
    ys = list(range(0,len(zs)))
    ax.plot(xs,ys,zs)

plt.show()

