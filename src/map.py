# Module
import folium
import copy
import math
import webbrowser
import pandas as pd
from pandas import DataFrame

# 전역 함수
def distance(x, y, x1, y1):
    d = math.sqrt((((x - x1) * 10000) ** 2) + (((y - y1) * 10000) ** 2))
    return d

# Class
class Visualize_map :
    # Constructor
    def __init__(self, df) :
        self.df = copy.deepcopy(df)
        self.map_osm = folium.Map(location = [35.16177000, 126.87969568], zoom_start = 13)
        self.target = ['총계', '성인 승차 인원', '청소년 승차 인원', '어린이 승차 인원']
        self.divide_rcmd = [50000, 50000, 10000,1000]
        self.divide_dcmd = [100, 100, 10, 1]
    
    # Target Map
    def mapping_target(self, select, colorM) :
        df_temp = self.df.sort_values(by = self.target[select], ascending = False)
        for item in df_temp.index:
            lat = df_temp.loc[item, '위도']
            long = df_temp.loc[item, '경도']
            folium.CircleMarker([lat, long],
                            radius = df_temp.loc[item, self.target[select]] / self.divide_rcmd[select],
                            popup = df_temp.loc[item, '정류소명'],
                            color = colorM,
                            fill = True).add_to(self.map_osm)
        
    # Recommend Map 0 ~ index
    def mapping_rcmd(self, select, index, colorM) :
        df_temp = self.df.sort_values(by = self.target[select], ascending = False)
        df_temp = df_temp[0 : index]
        for item in df_temp.index:
            lat = df_temp.loc[item, '위도']
            long = df_temp.loc[item, '경도']
            folium.CircleMarker([lat, long],
                            radius = df_temp.loc[item, self.target[select]] / self.divide_rcmd[select],
                            popup = df_temp.loc[item, '정류소명'],
                            color = colorM,
                            fill = True).add_to(self.map_osm)
    
    # Decommend Map index ~ 2000
    def mapping_dcmd(self, select, index, colorM) :
        df_temp = self.df.sort_values(by = self.target[select], ascending = False)
        df_temp = df_temp[index : 2000]
        for item in df_temp.index:
            lat = df_temp.loc[item, '위도']
            long = df_temp.loc[item, '경도']
            folium.CircleMarker([lat, long],
                            radius = df_temp.loc[item, self.target[select]] / self.divide_dcmd[select],
                            popup = df_temp.loc[item, '정류소명'],
                            color = colorM,
                            fill = True).add_to(self.map_osm)

    # Range Map indexA ~ indexB
    def mapping_range(self, select, indexA, indexB, colorM) :
        df_temp = self.df.sort_values(by = self.target[select], ascending = False)
        df_temp = df_temp[indexA : indexB]
        for item in df_temp.index:
            lat = df_temp.loc[item, '위도']
            long = df_temp.loc[item, '경도']
            folium.CircleMarker([lat, long],
                            radius = df_temp.loc[item, self.target[select]] / self.divide_rcmd[select],
                            popup = df_temp.loc[item, '정류소명'],
                            color = colorM,
                            fill = True).add_to(self.map_osm)

    # 주요 정류소의 연령층 이용 비율 함수
    def map_rate(self, select, index):
        df_temp = self.df.sort_values(by = self.target[select], ascending = False)
        df_temp = df_temp.reset_index()
        del df_temp["index"] 
        p = (df_temp.loc[index, self.target[select]]*100)/ df_temp.loc[0:len(df_temp.index), self.target[select]].sum(axis = 0)
        return p

    # 주요 정류소의 인접 정류소 병합 함수
    def mapping_dis(self, select, index, colorM, name, rate):
        df_temp = self.df.sort_values(by = self.target[select], ascending = False)
        df_temp = df_temp.reset_index()
        del df_temp["index"] 
        df_tempd= DataFrame({'정류소번호':[], '정류소명':[], '총계':[], '성인 승차 인원':[], '청소년 승차 인원':[], '어린이 승차 인원':[], '위도':[], '경도':[]})
        df_tempd.loc[df_tempd.shape[0]] = [df_temp.loc[index, '정류소번호'], df_temp.loc[index, '정류소명'], df_temp.loc[index, '총계'], df_temp.loc[index, '성인 승차 인원'], df_temp.loc[index, '청소년 승차 인원'], df_temp.loc[index, '어린이 승차 인원'], df_temp.loc[index, '위도'], df_temp.loc[index, '경도']]
        i=0
        j=0
        for i in range(1800):
            if (distance(df_temp.loc[index, '위도'], df_temp.loc[index, '경도'], df_temp.loc[i+1, '위도'], df_temp.loc[i+1, '경도']) < 100):
                df_tempd.loc[df_tempd.shape[j]] = [df_temp.loc[i+1, '정류소번호'], df_temp.loc[i+1, '정류소명'], df_temp.loc[i+1, '총계'], df_temp.loc[i+1, '성인 승차 인원'], df_temp.loc[i+1, '청소년 승차 인원'], df_temp.loc[i+1, '어린이 승차 인원'], df_temp.loc[i+1, '위도'], df_temp.loc[i+1, '경도']]
                j+1
        for item in df_tempd.index:
            lat = df_tempd.loc[item, '위도']
            long = df_tempd.loc[item, '경도']
            folium.CircleMarker([lat, long],
                            radius = df_tempd.loc[item, self.target[select]] / (self.divide_rcmd[select]),  # -item
                            popup = df_tempd.loc[item, '정류소명'],
                            color = colorM,
                            fill = True).add_to(self.map_osm)
        print("TOP", index+1, " :", df_temp.loc[index, "정류소명"])
        print(name + "의 버스 이용객 중 해당 정류소를 이용하는", name + "의 비율은 %3.2f%% 입니다." %rate)
        print("주변 정류장 :", df_tempd.loc[2, "정류소명"], df_tempd.loc[3, "정류소명"], df_tempd.loc[4, "정류소명"], ">>", colorM, "\n")
    
    # Show
    def mapping_show(self, name) :
        self.map_osm.save(name + '.html')
        webbrowser.open_new_tab(name +'.html')