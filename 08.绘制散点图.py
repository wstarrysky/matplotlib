#技术要点plt.scatter（）
from matplotlib import pyplot as plt
import matplotlib
import random
font = {'family': 'simsun',
        'weight': 'bold',
        'size': '12'}
matplotlib.rc('font', **font)

def rand_int(start, end, number):
    list = [0]*number    # 初始化指定列表长度，必须要含有0
    for i in range(number):
        list[i]=random.randint(start, end)
    return list

if __name__ == '__main__':
    y_3=rand_int(10,25,31)
    y_10=rand_int(10,25,31)
    x_3=range(1,32)
    x_10 = range(51, 82)
#输入信息
    plt.scatter(x_3,y_3,label="3月份")
    plt.scatter(x_10,y_10,label="10月份")
#调整x轴的刻度
    _x=list(x_3)+list(x_10)
    _xticks_labels=[f"3月{i}日"for i in x_3]
    _xticks_labels += [f"10月{i-50}日" for i in x_10]
    plt.xticks(_x,_xticks_labels,rotation=90)
    plt.yticks(range(min(min(y_3,y_10)), max(max(y_10,y_3))+ 1))
#绘制网格
    #plt.grid()
#添加图例
    plt.legend(loc='best')
#添加描述信息
    plt.xlabel("时间")
    plt.ylabel("温度")
    plt.title("标题")
#展示
    plt.show()