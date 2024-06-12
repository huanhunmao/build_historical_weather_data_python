import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_small/TG_STAID000001.txt', skiprows=20, parse_dates=['    DATE'])

# show rows
# print(df[10:20])

# show columns
# print(df.columns) # Index(['STAID', ' SOUID', '    DATE', '   TG', ' Q_TG'], dtype='object')
# print(df[['    DATE',' Q_TG']])
#             DATE  Q_TG
# 0     1860-01-01     0

# 求 均值
# print(df['   TG'].mean()) # -991.1500649011311 这个数字错的 因为没观测的数据记为 -9999

# 过滤掉 -9999 错误的值
# print(df.loc[df['   TG'] != -9999])

# 拿到 TG 平均值
# print(df.loc[df['   TG'] != -9999]['   TG'].mean() / 10) # 6.360787526128467

# 拿最大值
# print(df.loc[df['   TG'] != -9999]['   TG'].max() / 10) # 26.2

# 拿最小值
# print(df.loc[df['   TG'] != -9999]['   TG'].min() / 10) # -28.8

# 直方图
# df['   TG'].hist() 这个是错误的 因为没有过滤掉 -9999
df.loc[df['   TG'] != -9999]['   TG'].hist()
plt.show()  # 确保绘图展示出来

