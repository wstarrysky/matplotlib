# 1.设置图片大小
# 2.保存到本地
# 3.描述信息，比如x轴和y轴表示什么，这个图表示什么
# 4.调整x和y的刻度
# 5.线条的样式，颜色、透明度之类的
# 6.标记处特殊的点（比如告诉别人最高点和最低点在哪里）
# 7.给图片添加一个水印（防伪，防盗使用）
from matplotlib import pyplot as plt

# 设置图片大小
fig = plt.figure(figsize=(15, 8), dpi=80)
# figure图形图标的意思，在这里指的就是我们画的图
# figsize是一个元组，表示图片的宽和高，宽20，高8；dpi指的是每英寸上像素点的个数

x = range(2, 26, 2)  # 从2到26，步长为2
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]  # 对应的y值

# 绘图
plt.plot(x, y)  # 传入x和y的值

# 设置x轴的刻度
# plt.xticks(x)#这样子就把所有x的值都标记上去了
# plt.xticks(range(2,25))#这样子的x轴刻度值就是一了
# 如果还要更密集一点，考虑做一个列表
xtick = [i / 2 for i in range(2, 49)]
plt.xticks(xtick[::3])  # 取列表的步长以简略
# y轴也是一样有着yticks这样的一个管理y轴刻度的值
plt.yticks(range(min(y), max(y) + 1))
# 保存图片
plt.savefig("sig_size.png")
plt.show()  # 展示坐标图
