import pandas as pd


df1 = pd.read_csv('first_run_100.csv')
df2 = pd.read_csv('first_run_100-200.csv')
df3 = pd.read_csv('first_run200-300.csv')
df4 = pd.read_csv('first_run300-rest.csv')
df = pd.DataFrame()

Name1 = df1['Name'].to_list()
Name2 = df2['Name'].to_list()
Name3 = df3['Name'].to_list()
Name4 = df4['Name'].to_list()

a1 = df1['P_1'].to_list()
a2 = df2['P_1'].to_list()
a3 = df3['P_1'].to_list()
a4 = df4['P_1'].to_list()

a_1 = df1['PV_1'].to_list()
a_2 = df2['PV_1'].to_list()
a_3 = df3['PV_1'].to_list()
a_4 = df4['PV_1'].to_list()

b1 = df1['P_2'].to_list()
b2 = df2['P_2'].to_list()
b3 = df3['P_2'].to_list()
b4 = df4['P_2'].to_list()

b_1 = df1['PV_2'].to_list()
b_2 = df2['PV_2'].to_list()
b_3 = df3['PV_2'].to_list()
b_4 = df4['PV_2'].to_list()

c1 = df1['P_3'].to_list()
c2 = df2['P_3'].to_list()
c3 = df3['P_3'].to_list()
c4 = df4['P_3'].to_list()

c_1 = df1['PV_3'].to_list()
c_2 = df2['PV_3'].to_list()
c_3 = df3['PV_3'].to_list()
c_4 = df4['PV_3'].to_list()

d1 = df1['P_4'].to_list()
d2 = df2['P_4'].to_list()
d3 = df3['P_4'].to_list()
d4 = df4['P_4'].to_list()

d_1 = df1['PV_4'].to_list()
d_2 = df2['PV_4'].to_list()
d_3 = df3['PV_4'].to_list()
d_4 = df4['PV_4'].to_list()

e1 = df1['P_5'].to_list()
e2 = df2['P_5'].to_list()
e3 = df3['P_5'].to_list()
e4 = df4['P_5'].to_list()

e_1 = df1['PV_5'].to_list()
e_2 = df2['PV_5'].to_list()
e_3 = df3['PV_5'].to_list()
e_4 = df4['PV_5'].to_list()

f1 = df1['P_6'].to_list()
f2 = df2['P_6'].to_list()
f3 = df3['P_6'].to_list()
f4 = df4['P_6'].to_list()

f_1 = df1['PV_6'].to_list()
f_2 = df2['PV_6'].to_list()
f_3 = df3['PV_6'].to_list()
f_4 = df4['PV_6'].to_list()

g1 = df1['P_7'].to_list()
g2 = df2['P_7'].to_list()
g3 = df3['P_7'].to_list()
g4 = df4['P_7'].to_list()

g_1 = df1['PV_7'].to_list()
g_2 = df2['PV_7'].to_list()
g_3 = df3['PV_7'].to_list()
g_4 = df4['PV_7'].to_list()

h1 = df1['P_8'].to_list()
h2 = df2['P_8'].to_list()
h3 = df3['P_8'].to_list()
h4 = df4['P_8'].to_list()

h_1 = df1['PV_8'].to_list()
h_2 = df2['PV_8'].to_list()
h_3 = df3['PV_8'].to_list()
h_4 = df4['PV_8'].to_list()

i1 = df1['P_9'].to_list()
i2 = df2['P_9'].to_list()
i3 = df3['P_9'].to_list()
i4 = df4['P_9'].to_list()

i_1 = df1['PV_9'].to_list()
i_2 = df2['PV_9'].to_list()
i_3 = df3['PV_9'].to_list()
i_4 = df4['PV_9'].to_list()

j1 = df1['P_10'].to_list()
j2 = df2['P_10'].to_list()
j3 = df3['P_10'].to_list()
j4 = df4['P_10'].to_list()

j_1 = df1['PV_10'].to_list()
j_2 = df2['PV_10'].to_list()
j_3 = df3['PV_10'].to_list()
j_4 = df4['PV_10'].to_list()

k1 = df1['P_11'].to_list()
k2 = df2['P_11'].to_list()
k3 = df3['P_11'].to_list()
k4 = df4['P_11'].to_list()

k_1 = df1['PV_11'].to_list()
k_2 = df2['PV_11'].to_list()
k_3 = df3['PV_11'].to_list()
k_4 = df4['PV_11'].to_list()

l1 = df1['P_12'].to_list()
l2 = df2['P_12'].to_list()
l3 = df3['P_12'].to_list()
l4 = df4['P_12'].to_list()

l_1 = df1['PV_12'].to_list()
l_2 = df2['PV_12'].to_list()
l_3 = df3['PV_12'].to_list()
l_4 = df4['PV_12'].to_list()

m1 = df1['P_13'].to_list()
m2 = df2['P_13'].to_list()
m3 = df3['P_13'].to_list()
m4 = df4['P_13'].to_list()

m_1 = df1['PV_13'].to_list()
m_2 = df2['PV_13'].to_list()
m_3 = df3['PV_13'].to_list()
m_4 = df4['PV_13'].to_list()

n1 = df1['P_14'].to_list()
n2 = df2['P_14'].to_list()
n3 = df3['P_14'].to_list()
n4 = df4['P_14'].to_list()

n_1 = df1['PV_14'].to_list()
n_2 = df2['PV_14'].to_list()
n_3 = df3['PV_14'].to_list()
n_4 = df4['PV_14'].to_list()

Name_1 = Name1 + Name2 + Name3 + Name4
P_1  = a1 + a2 + a3 + a4
PV_1 = a_1 + a_2 + a_3 + a_4
P_2  = b1 + b2 + b3 + b4
PV_2 = b_1 + b_2 + b_3 + b_4
P_3  = c1 + c2 + c3 + c4
PV_3 = c_1 + c_2 + c_3 + c_4
P_4  = d1 + d2 + d3 + d4
PV_4 = d_1 + d_2 + d_3 + d_4
P_5  = e1 + e2 + e3 + e4
PV_5 = e_1 + e_2 + e_3 + e_4
P_6  = f1 + f2 + f3 + f4
PV_6 = f_1 + f_2 + f_3 + f_4
P_7  = g1 + g2 + g3 + g4
PV_7 = g_1 + g_2 + g_3 + g_4
P_8  = h1 + h2 + h3 + h4
PV_8 = h_1 + h_2 + h_3 + h_4
P_9  = i1 + i2 + i3 + i4
PV_9 = i_1 + i_2 + i_3 + i_4
P_10  = j1 + j2 + j3 + j4
PV_10 = j_1 + j_2 + j_3 + j_4
P_11  = k1 + k2 + k3 + k4
PV_11 = k_1 + k_2 + k_3 + k_4
P_12  = l1 + l2 + l3 + l4
PV_12 = l_1 + l_2 + l_3 + l_4
P_13  = m1 + m2 + m3 + m4
PV_13 = m_1 + m_2 + m_3 + m_4
P_14  = n1 + n2 + n3 + n4
PV_14 = n_1 + n_2 + n_3 + n_4

Name = []
l =len(Name_1)
for i in range(l):
    length = len(Name_1)
    Name.append(Name_1[i][1:])

df['Name']= Name
df['P_']  = P_1
df['PV_1'] = PV_1
df['P_2']  = P_2
df['PV_2'] = PV_2
df['P_3']  = P_3
df['PV_3'] = PV_3
df['P_4']  = P_4
df['PV_4'] = PV_4
df['P_5']  = P_5
df['PV_5'] = PV_5
df['P_6']  = P_6
df['PV_6'] = PV_6
df['P_7']  = P_7
df['PV_7'] = PV_7
df['P_8']  = P_8
df['PV_8'] = PV_8
df['P_9']  = P_9
df['PV_9'] = PV_9
df['P_10']  = P_10
df['PV_10'] = PV_10
df['P_11']  = P_11
df['PV_11'] = PV_11
df['P_12']  = P_12
df['PV_12'] = PV_12
df['P_13']  = P_13
df['PV_13'] = PV_13
df['P_14']  = P_14
df['PV_14'] = PV_14

df.to_excel('Builders_Database.xlsx',sheet_name='Sheet1',index=False)
print('Done')

