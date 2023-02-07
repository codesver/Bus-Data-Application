import pandas as pd
import numpy as np
import copy

def isEnglishOrKorean(input_s):
    k_count = 0
    e_count = 0
    for c in input_s:
        if ord('가') <= ord(c) <= ord('힣'):
            k_count+=1
        elif ord('a') <= ord(c.lower()) <= ord('z'):
            e_count+=1
    return k_count + e_count

file = open('Study/Input.txt', 'r', encoding = 'utf8')
a = file.read().split()

dataCSV = pd.read_csv('Study/Output.csv')
dfa = pd.DataFrame(dataCSV)
df = copy.deepcopy(dfa)
listN = list(np.array(df['정류소번호'].tolist()))

for i in range(len(listN)) :
    listN[i] = str(listN[i])
listLat = []
listLong = []
temp = 0

for i in range(2000, 2316) :
    for j in range(3, len(a)) :
        if (a[j] == listN[i]) & (isEnglishOrKorean(a[j - 1]) == 0) & (isEnglishOrKorean(a[j - 2]) == 0) & (isEnglishOrKorean(a[j - 3]) > 0) :
            listLong.append(float(a[j - 1]))
            temp = 1
            break
    if  temp == 0:
        listLong.append(0)
    temp = 0

print(listLong)