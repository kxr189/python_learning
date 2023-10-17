#基本数据类型
#python 6种数据类型
#字符串
# data = 'Hello, Math!'
# print(data[0])
# print(data[1:5])
# print(len(data))
# print(data)

#数值
# value = 521
# print(value)
# value_2 = 1.2
# print(value_2)

#布尔类型
# true = True
# false = False
# print(true)
# print(false)

#变量赋值
# a, b, c = 1, 'hello', True
# print(a, b, c)
# print(a)
# print(b)
# print(c)

#空值
# a = None
# b = a
# print(a)
# print(b)

#控制语句  三类：条件控制语句、循环语句、条件循环
#条件控制语句
# value = 1
# if value == 1:
#     print('This is true')
# elif value>20:
#     print('is is bigger than 20?')
# else:
#     print('This is false')

#循环语句
# for i in range(5):
#     print(i)

#条件循环
# i = 0
# while i<5:
#     print(i)
#     i = i+1

#复杂数据类型
#元组:只读，元组的元素不能重新赋值
# a = (1,2,3)
# print(a)
# print(a[1])

#列表
# a = [1, 2, 3]
# print(a)
# #add
# a.append(4)
# print(a)
# print(a[3])
# #更新列表项
# a[2] = 5
# print(a)
# for i in a:
#     print(i)

#字典：可变容器模型 key:value
# mydict = {'a':6.18, 'b':'str', 'c':True}
# print('A value: %.2f' %mydict['a'])
# #add
# mydict['a'] = 523
# print('A value: %d' %mydict['a'])
# print('keys: %s' %mydict.keys())
# print('value: %s' %mydict.values())
# for key in mydict:
#     print(mydict[key])


#函数：可重复利用的 def（）return
#定义函数
# def mysum(x, y):
#     return x+y
# result = mysum(x=1, y=2)
# print(result)

#Numpy速成
#创建数组
import numpy as np
# myarray = np.array([1,2,3])
# print(myarray)
# print(myarray.shape)
#
# myarray = np.array([[1,2,3], [2,3,4], [3,4,5]])
# print(myarray)
# print(myarray.shape)
#
# #访问数据
# print('第一行数据：%s' % myarray[0])
# print('最后一行： %s' %myarray[-1])
# print('整列(3列)的数据： %s' %myarray[:, 2])

#pandas速成
#series:一维数组：list
import pandas as pd
# myarray = np.array([1,2,3])
# index = ['a', 'b', 'c']
# myseries = pd.Series(myarray, index=index)
# print(myseries)
# print('series的第一个元素：')
# print(myseries[0])
# print('series的c index的元素：')
# print(myseries['c'])
#Dataframe:可以指定行和列的二维数组
myarray = np.array([[1,2,3], [2,3,4], [3,4,5]])#类型：（x, y）
rowindex = ['row1', 'row2', 'row3']
colname = ['col1', 'col2', 'col3']
mydataframe = pd.DataFrame(data=myarray, index=rowindex, columns=colname)
print(mydataframe)
print('访问col3的数据')
print(mydataframe['col3'])




























