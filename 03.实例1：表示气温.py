#如果列表a表示10点到12点的每一分钟的气温，如何绘制折线图观察每分钟气温的变化情况？

from matplotlib import pyplot as  plt
import  random
import  cv2

a=range(120) #y值
b=[random.randint(20,35) for i in range(120)]#x值

plt.figure(figsize=(15,10),dpi=80)

#绘图
plt.plot(a,b)#传入数据

#绘制坐标轴尺寸
plt.xticks(range(121)[::5])
plt.yticks(b)

plt.show()
plt.close()