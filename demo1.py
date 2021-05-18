import matplotlib.pyplot as plt

# 人生苦短，我用Python , java , android , kotlin ,
#  2021年5月18日21:37:44
# B站 up : 幻雨之秋
# 跳转页 ： https://hyzqacg.github.io

# 刚装上的python默认是不带 matplotlib.pyplot 这个库的，所以需要到 cmd 或者 Terminal 里面运行以下代码，下载这个库
# pip import matplotlib
# 下载速度慢，或下载不到，用这条
# pip import matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple


# 折线图
# 讲两组数组数据，放入
plt.plot([1,2,3,4],[1,4,9,16])
# 显示数据
plt.show()


# 柱状图
# 数据a
a = ['测试1', '测试2', '测试3', '测试4']
# 数据b
b = [1, 2, 3, 4]

# 字体设置
font = {
    'family': 'simhei',
    'weight': 'bold',
    'size': '12'
}

# maptplotlib.rc('font', **font)

#显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']

#这两行需要手动设置
plt.rcParams['axes.unicode_minus']=False

# 合并数据
plt.bar(a, b)

# 显示数据
plt.show()

