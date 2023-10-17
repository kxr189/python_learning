#数据的导入
#三种方式
#csv特征：，分隔 文件头：字段属性
from csv import reader
import numpy as np
# filename = 'pima_data.csv'
# with open(filename, 'rt') as raw_data:
#     readers = reader(raw_data, delimiter=',')
#     x = list(readers)
#     data = np.array(x).astype('float')
#     print(data.shape)

#Pandas导入
# from pandas import read_csv
# filename = 'pima_data.csv'
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# data = read_csv(filename, names=names)
# print(data.shape)

#numpy导入
# from numpy import loadtxt
# filename = 'pima_data.csv'
# with open(filename, 'rt') as raw_data:
#     data = loadtxt(raw_data, delimiter=',')
#     print(data.shape)
#查看数据
from pandas import read_csv
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)

#head = data.head(10)
# print(head)

#数据的维度
# print(data.shape)
#数据的属性和类型
# print(data.dtypes)
#描述性统计
#print(data.describe())
#数据的分布
#print(data.groupby('class').size())
#数据的相关性：皮尔逊相关系数
#print(data.corr(method='pearson'))
#数据的分布分析：高斯分布
print(data.skew())




