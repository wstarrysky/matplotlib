from matplotlib import pyplot as plt
import matplotlib
import random
font = {'family': 'simsun',
        'weight': 'bold',
        'size': '14'}
matplotlib.rc('font', **font)


def rand_int(start, end, number):
    list = [0]*number    # 初始化指定列表长度，必须要含有0
    for i in range(number):
        list[i]=random.randint(start, end)
    return list


y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 4, 3, 3, 1, 1, 2, 1]
y_2 = rand_int(0,6,20)
age = range(11, 31)
# x,y
x= age
# 设置图形大小
plt.figure(figsize=(15, 8), dpi=80)
# 传入数据
plt.plot(x, y_1,label="自己")    # label一定是要结合plt.legend()使用的
plt.plot(x, y_2,label="同桌")
# 刻画坐标轴
_xsticks = ["{}岁".format(i) for i in range(11, 31)]
# 很关键，灵性
_ysticks = ["{}/个".format(y_1[i]) for i in range(len(y_1))]
# f-string   一种新的表示方法  ****很重要，尽量还是使用这种方法表示吧  其实{}就是一个被替换的地方，而对于format（）而言，
# 括号内的其实就是{}里的表达式，这样子就很好理解了
# _ysticks = [f"{a[i]}/个" for i in range(len(a))]#其实这里是做了n个标签，只不过这n个标签一一对应相应的x值 ，然后相同的标签
# 的值就互相重叠了，在图上的表示效果显得只有几个而已,也是有些地方黑有些地方浅的原因
plt.xticks(x, _xsticks)
plt.yticks(y_1, _ysticks)

# 绘制网格
plt.grid(alpha=0.4)  # alpha代表透明度，0完全透明  1就是完全不透明

# 描述坐标轴
plt.xlabel("年龄")
plt.ylabel("个数")
plt.title("走势图")

# 添加图例
plt.legend(loc='best')
plt.show()
