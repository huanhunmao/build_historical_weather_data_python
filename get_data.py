import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
# df.loc[df['   TG'] != -9999]['   TG'].hist()
# plt.show()  # 确保绘图展示出来

# 查某个 日期的 TG 值
# print(df.loc[df['    DATE'] == '1860-04-02']['   TG']) # index + TG 92    52
# print(df.loc[df['    DATE'] == '1860-04-02']['   TG'].squeeze() / 10) # 5.2 拿到温度值

# 寻找 温度最大值 日期
# print(df.loc[df['   TG'] == df['   TG'].max()]) # 3150      1   35381 1868-08-16    262      0
# print(df.loc[df['   TG'] == df['   TG'].max()]['    DATE']) # 3150   1868-08-16
# print(df.loc[df['   TG'] == df['   TG'].max()]['    DATE'].squeeze()) # 1868-08-16 00:00:00 拿到日期


# 更简单的方式 获得 TG 类似坐标 index + '   TG'
# print(df)
# print(df.loc[3, '   TG']) # 37 能直接拿到 TG 值

# 将 -9999 值替换为 NaN
df['TG0'] = df['   TG'].mask(df['   TG'] == -9999, np.nan)
# 计算出 更方便的 TG
df['TG'] = df['TG0'] / 10
# print(df)

# 转为 摄氏度
df['CTG'] = df['TG'] * (9/5) + 32
print(df)

# 再次画出图
# df['CTG'].hist()
# plt.show()

# 展示 所有日期 温度变化
# df.plot(x = '    DATE', y = 'TG', figsize = (15,3))
# plt.show()

# 展示特定 一段的 温度变化
df[100:1000].plot(x = '    DATE', y = 'TG', figsize = (15,3))
plt.show()