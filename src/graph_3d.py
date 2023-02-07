# Module
import numpy as np
import pandas as pd
import copy
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Class
class Visualize_3D :
    # Constructor
    def __init__(self, df) :
        self.df = df
        self.t = list(np.array(df['총계'].tolist()))
        self.x = list(np.array(df['성인 승차 인원'].tolist()))
        self.y = list(np.array(df['청소년 승차 인원'].tolist()))
        self.z = list(np.array(df['어린이 승차 인원'].tolist()))

    # All Data 3d Graph
    def graph_3d_all(self) :
        self.graph_show(self.x, self.y, self.z)

    # Range Data 3d Graph
    def graph_3d_range(self, maxI, minI) :
        t_temp = copy.deepcopy(self.t)
        x_temp = copy.deepcopy(self.x)
        y_temp = copy.deepcopy(self.y)
        z_temp = copy.deepcopy(self.z)

        if maxI != 1 :
            r = 0
            while (r < maxI - 1) :
                maximum = t_temp.index(max(t_temp))
                del t_temp[maximum]
                del x_temp[maximum]
                del y_temp[maximum]
                del z_temp[maximum]
                r += 1

        if minI != 2000 :
            r = 0
            while(r < 2000 - minI) :
                minimum = t_temp.index(min(t_temp))
                del t_temp[minimum]
                del x_temp[minimum]
                del y_temp[minimum]
                del z_temp[minimum]
                r += 1

        self.graph_show(x_temp, y_temp, z_temp)

    # Show Data 3d Graph
    def graph_show(self, x, y, z) :
        fig = plt.figure(figsize = (10, 10))
        ax = fig.gca(projection = '3d')
        ax.scatter(x, y, z, marker = 'o', s = 15, c = 'darkgreen')
        ax.set_xlabel('Adult')
        ax.set_ylabel('Teenager')
        ax.set_zlabel('Child')
        plt.show()
        

bus_stop_data = pd.read_csv('Project/bus_stop_data.csv')
dfo = pd.DataFrame(bus_stop_data)
v = Visualize_3D(dfo)
v.graph_3d_range(300, 400)