import pandas as pd

df = pd.read_csv('first_run.csv')
sf = pd.DataFrame()
a = df['links'].to_list()
l = len(a)

b = []
y=0

for i in range(l):
    if a[i][0]=='h':
        b.append(a[i])
        y+=1
        print(a[i])
        print(y)

print(b)
sf['links'] = b
sf.to_excel('RERA_Builders_Database.xlsx',sheet_name='Buider_Links',index=False)
print('Done')