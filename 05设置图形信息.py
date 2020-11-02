# 如果列表a表示10点到12点的每一分钟的气温，如何绘制折线图观察每分钟气温的变化情况？


# 使用xticks，使得x轴显示字符串
from matplotlib import pyplot as  plt
import random
import matplotlib

# windows和linux设置字体的方式
font = {'family': 'simsun',
        'weight': 'bold',
        'size': '14'}
matplotlib.rc("font", **font)

a = range(120)  # y值
b = [random.randint(20, 35) for i in range(120)]  # x值

plt.figure(figsize=(15, 8), dpi=80)

# 绘图
plt.plot(a, b)  # 传入数据

# 绘制坐标轴尺寸
_x = a[::3]
_xsticks = ["10点{}分".format(i) for i in range(60)]
_xsticks += ["11点{}分".format(i) for i in range(60)]
# format(),一个格式化字符，用{}和：来代替%符号

# 取步长，数字和字符串一一对应
plt.xticks(_x[::3], _xsticks[::3], rotation=45)  # rotation  旋转的角度参数
plt.yticks(b)

#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位℃")
plt.title("10点到12点每分钟温度变化的情况")

plt.show()
plt.close()
