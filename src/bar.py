# Module
import copy
import pandas as pd                
import matplotlib as mpl           
import matplotlib.pyplot as plt

# Class
class Bar_G :
    # Constructor
    def __init__(self, df) :
        self.df = copy.deepcopy(df)
        self.target = ['총계', '성인 승차 인원', '청소년 승차 인원', '어린이 승차 인원']

    # Recommend Bar Top 10 SELECT
    def bar_rcmd(self, select) :
        df_rcmd = self.df.sort_values(by = self.target[select], ascending = False)
        df_rcmd = df_rcmd.iloc[0:10]
        df_rcmd = df_rcmd.loc[:, ['정류소명', self.target[select]]].set_index('정류소명')
        bar = df_rcmd.plot(kind = 'bar', figsize = (10, 7), legend = True, fontsize = 15)
        bar.set_title(self.target[select] + '기준 승차 데이터 TOP 10', fontsize = 20)
        bar.set_xlabel('버스 정류장명', fontsize = 15)
        bar.set_ylabel('승차인원(수)', fontsize = 15)
        bar.legend([self.target[select]], fontsize = 15)
        plt.show()
    
    # Decommend Bar Bottom 10 SELECT
    def bar_dcmd(self, select) :
        df_dcmd = self.df.sort_values(by = self.target[select], ascending = True)
        df_dcmd = df_dcmd.iloc[0:10]
        df_dcmd = df_dcmd.loc[:, ['정류소명', self.target[select]]].set_index('정류소명')
        bar = df_dcmd.plot(kind = 'bar', figsize = (10, 7), legend = True, fontsize = 15)
        bar.set_title(self.target[select] + '기준 승차 데이터 TOP 10', fontsize = 20)
        bar.set_xlabel('버스 정류장명', fontsize = 15)
        bar.set_ylabel('승차인원(수)', fontsize = 15)
        bar.legend([self.target[select]], fontsize = 15)
        plt.show()