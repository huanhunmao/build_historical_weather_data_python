import  pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('practice_data/wines.csv',)

# 拿到 points=100 的数量
# 通过标签来访问和修改数据 单个标签：df.loc['行标签', '列标签']
print(len(df.loc[df['points'] == 100])) # 19

# 找到价格最高的 酒 名称
# 将只有一个元素的 Series 转换为该元素的实际值
print(df.loc[df['price'] == df['price'].max()]['name'].squeeze()) # Glamorosa Sensible

# 本来范围是 0-100， 缩小范围的方式 就是 / 20  变成 0-5
df['rate'] = df['points'] / 20
print(df['rate'])

# 价格低于 100 的直方图 📊
# df.loc[df['price'] < 100]['price'].hist()
# plt.show()

# 另外一个图展示 价格和评分关系，可以帮助分析 评分是否和价格正相关
# kind='scatter' 表示要绘制散点图
df.plot(x='price', y='points', figsize=(15,3), kind='scatter')
plt.show()