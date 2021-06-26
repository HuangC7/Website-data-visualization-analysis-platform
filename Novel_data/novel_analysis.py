
import json

import pandas as pd
import matplotlib.pyplot as plt
# 设置输出结果列对齐


pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)

# 读取排名，种类，书名，作者，月票数量这4列数据，使用默认索引
df = pd.read_csv(r'result.csv', usecols=['排名','种类','书名','作者','月票数量'])
# 输出前10行
print(df[:10], end='\n\n')

# 分析统计每一种类的月票数量   ---> echarts柱状图
df_1 = df.groupby(by='种类')['月票数量'].sum()
df_1_json = df_1.to_dict()

# for i in df_1_json:
#     print(df_1_json[i])
with open('data1.json', 'w', encoding='utf-8-sig') as file:
        file.write(json.dumps(df_1_json, indent=2, ensure_ascii=False))

print(df.groupby(by='种类')['月票数量'].sum())
# 分析统计月票数在5000-10000,10000-15000,15000-20000,以及大于20000的个数   ---> echarts饼状图
df_2 = pd.value_counts(pd.cut(df['月票数量'], bins = [5000, 10000, 15000, 20000, 100000000], labels = ['5000-10000', '10000-15000', '15000-20000', '大于20000']))
df_2_json = df_2.to_dict()
with open('data2.json', 'w', encoding='utf-8-sig') as file:
        file.write(json.dumps(df_2_json, indent=2, ensure_ascii=False))

print(pd.value_counts(pd.cut(df['月票数量'], bins = [5000, 10000, 15000, 20000, 100000000], labels = ['5000-10000', '10000-15000', '15000-20000', '大于20000'])))

# 分析统计每个种类的个数    ---> echarts折线图
df_3 = df['种类'].value_counts()
df_3_json = df_3.to_dict()
with open('data3.json', 'w', encoding='utf-8-sig') as file:
        file.write(json.dumps(df_3_json, indent=2, ensure_ascii=False))
print(df['种类'].value_counts())


df1 = df[:100]       # 一月
df2 = df[100:200]    # 二月
df3 = df[200:300]    # 三月

# 分析统计每一个月的月票数量总数   ---> echarts饼状图

df_4_1 = pd.DataFrame(df1['月票数量'].sum(), index=['一月'],columns=['月票总数'])
df_4_2 = pd.DataFrame(df2['月票数量'].sum(), index=['二月'],columns=['月票总数'])
df_4_3 = pd.DataFrame(df3['月票数量'].sum(), index=['三月'],columns=['月票总数'])
df_4 = pd.concat([df_4_1, df_4_2, df_4_3], axis=0, ignore_index=False)

df_4_json = df_4.to_dict()
with open('data4.json', 'w', encoding='utf-8-sig') as file:
        file.write(json.dumps(df_4_json, indent=2, ensure_ascii=False))


print(df1['月票数量'].sum())
print(df2['月票数量'].sum())
print(df3['月票数量'].sum())
# 分析统计每个月的都市种类的数量   ---> echarts饼状图
df_5_1 = pd.DataFrame(df1[df1['种类'] == '都市']['种类'].value_counts().tolist(), index=['一月'], columns=['种类个数'])
df_5_2 = pd.DataFrame(df2[df2['种类'] == '都市']['种类'].value_counts().tolist(), index=['二月'], columns=['种类个数'])
df_5_3 = pd.DataFrame(df3[df3['种类'] == '都市']['种类'].value_counts().tolist(), index=['三月'], columns=['种类个数'])
df_5 = pd.concat([df_5_1, df_5_2, df_5_3], axis=0, ignore_index=False)

df_5_json = df_5.to_dict()
with open('data5.json', 'w', encoding='utf-8-sig') as file:
        file.write(json.dumps(df_5_json, indent=2, ensure_ascii=False))
# print(df_5)
# # print(df_5_json)

print(df1[df1['种类'] == '都市']['种类'].value_counts().tolist())
print(df2[df2['种类'] == '都市']['种类'].value_counts().tolist())
print(df3[df3['种类'] == '都市']['种类'].value_counts().tolist())

