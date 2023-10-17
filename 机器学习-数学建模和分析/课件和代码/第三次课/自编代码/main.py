# 基本数据类型
# python有六种数据类型
# 1、字符串 单双引号都可以
data = 'Hello,Math'
# 打印第0个字母
print(data[0])
# 打印第1、2、3、4个字母
print(data[1:5])
# 打印字符串的长度
print(len(data))
# 打印字符串
print(data)

# 2、数值
value = 521
print(value)
value_2 = 102
print(value_2)

# 3、bool类型
true = True
false = False
print(true)
print(false)

# 复杂数据类型
# 元组：只读，即abc不能变了，就是不能重新赋值
abc = (1,2,3)
print(abc)
print(abc[1])
# 列表
de = [1,2,3]
print(de)
# 列表可以增加项
de.append(4)
print(de)
print(de[3])
# 更新列表
de[2] = 5
print(de)
for i in de:
    print(i)
# 字典：可变容器模型key:value，可以储存任意类型的对象
mydict = {'a':6.18,'b':'str','c':True}
print('A value: %.2f' %mydict['a'])
# 增加
mydict['a'] = 523
print('A value: %d' %mydict['a'])
print('keys: %s' %mydict.keys())
print('value: %s' %mydict.values())
for key in mydict:
    print(mydict[key])

# 变量赋值
a, b, c = 1, 'hello', True
print(a,b,c)
print(a)
print(b)
print(c)

# 空值
empty = None
b_empty = empty
print(empty)
print(b_empty)

# 控制语句
# 有三类：条件控制语句、循环语句、条件循环语句
# 1、条件控制语句
val = 1
if val == 1:
    print('This is true')
elif value > 20:
    print('It is bigger than 20')
else:
    print('This is false')
# 2、循环语句
# range(5)随机生成5个数0~4
for i in range(5):
    print(i)
# 3、条件循环语句
i = 0
while i<5:
    print(i)
    i = i+1

# 函数：可重复利用的代码
# 定义函数
def mysum(x,y):
    return x+y
result = mysum(x=1,y=2)
print(result)


# numpy速成
# 创建数组
import numpy as np
myarray = np.array([1,2,3])
print(myarray)
print(myarray.shape)

myarray = np.array([[1,2,3],[2,3,4],[3,4,5]])
print(myarray)
print(myarray.shape)

# 访问数据
print('第一行数据:%s' %myarray[0])
# 最后一行数据
print('最后一行数据:%s' %myarray[-1])
print('第三列数据：%s' %myarray[:,2])