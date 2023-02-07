# module
import pandas as pd
import matplotlib as mpl
from bar import Bar_G
from map import Visualize_map
from matplotlib import pyplot

# Main Code

# < 프로그램 안내 >
print('< 버스 정류소 인원 데이터 분석 프로그램 >')
print('---------------------------------------------------------------------------')
print('본 AI 프로그램은 버스 정류소 이용객을 기준으로 유동인구를 파악합니다.')
print('파악된 유동인구를 바탕으로 사용자가 입점하고자하는 시설을 분석합니다.')
print('분석된 데이터를 통해 입점 추천지와 비추천지를 알려줍니다.')
print('---------------------------------------------------------------------------\n')

# < 사용자 데이터 입력 >
print('< 사용자 데이터 입력 >')
print('---------------------------------------------------------------------------')
print('입점 시설의 명칭과 주요 이용 연령층을 입력하세요.')
name = input('입점 시설의 이름을 입력하세요 : ')
print('입점 시설의 주요 이용 연령층을 입력하세요.')
target = int(input('0. 전체  | 1. 성인 | 2. 청소년 | 3. 어린이 : '))
print('---------------------------------------------------------------------------\n')

# < 버스정류소 데이터 불러오기 >
bus_stop_data = pd.read_csv('bus_stop_data.csv')
dfo = pd.DataFrame(bus_stop_data)

# < 막대 그래프를 통한 분석 결과 시각화 >
# ---------------------------------------------------------------------------
print('< 막대 그래프 시각화 >')
print('---------------------------------------------------------------------------')
# Font
pyplot.rc('font', family = 'Malgun Gothic')
mpl.rcParams['axes.unicode_minus'] = False

# Z. Bar
bar_target = Bar_G(dfo)

# A. Target 기준 상위 10개
print('# 타겟 연령층의 상위 10개 정류소 그래프입니다.')
bar_target.bar_rcmd(target)
print('---------------------------------------------------------------------------\n')
# ---------------------------------------------------------------------------

# < Map을 통한 분석 결과 시각화 >
print('< Map을 통한 시각화 >')
# ---------------------------------------------------------------------------
print('---------------------------------------------------------------------------')

# A. 전체 데이터를 시각화 (총계 기준)
print('1. 총계 기준 전 버스 정류소 이용객 현황 지도입니다.')
map_all = Visualize_map(dfo)
map_all.mapping_range(0, 0, 2000, 'green')
map_all.mapping_show('map_all')

# B. Target의 전체 분포 현황
target_str = ['전체', '성인', '청소년', '어린이']
print('2.', target_str[target], '이용객 비율별 정류장 표시 지도입니다.')
map_target_all = Visualize_map(dfo)
map_target_all.mapping_target(target, 'purple')
map_target_all.mapping_show('map_target_all')

# B. 입점 추천 위치 시각화 (상위 5% 하위 5%)
print('3. 타겟 연령층 상위 5%(Blue) | 타겟 연령층 하위 5%(Red)입니다.')
map_target_cmd = Visualize_map(dfo)
map_target_cmd.mapping_rcmd(target, 100, 'blue')
map_target_cmd.mapping_dcmd(target, 1900, 'red')
map_target_cmd.mapping_show('map_target_cmd')
print('---------------------------------------------------------------------------\n')
# ---------------------------------------------------------------------------

# < 결론 도출 >
# ---------------------------------------------------------------------------
print('< 시설 입점지를 추천합니다. >')
print('---------------------------------------------------------------------------')
target_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
map_seven = Visualize_map(dfo)
for i in range(7):
    map_seven.mapping_dis(target, i, target_color[i], target_str[target], map_seven.map_rate(target, i))
map_seven.mapping_show('map_seven')
print('---------------------------------------------------------------------------')
# ---------------------------------------------------------------------------