import pandas as pd
import math
df = pd.read_excel('Builders_Database.xlsx')

a1 = df['P_1'].to_list()
a2 = df['P_2'].to_list()
a3 = df['P_3'].to_list()
a4 = df['P_4'].to_list()
a5 = df['P_5'].to_list()
a6 = df['P_6'].to_list()
a7 = df['P_7'].to_list()
a8 = df['P_8'].to_list()
a9 = df['P_9'].to_list()
a10 = df['P_10'].to_list()
a11 = df['P_11'].to_list()
a12 = df['P_12'].to_list()
a13 = df['P_13'].to_list()
a14 = df['P_14'].to_list()

all = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14
list_set = set(all)
distinct = list(list_set)

distinct_headers = list(filter(lambda x: not isinstance(x, float) or not math.isnan(x), distinct))

print(distinct_headers)
print(len(distinct_headers))