---
title: python-numpy从入门到实践
tags: [深度学习,机器学习,计算机视觉,python,numpy]
categories: [深度学习,深度学习入门,深度学习理论入门,计算机视觉]
---

简介：numpy是Python语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供了大量的数学函数库。

<!-- more -->

# 一、初识numpy
## 1、numpy简介
>简介：numpy是Python语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供了大量的数学函数库。

>作用：numpy是一个运行速度非常快的数学库，主要用于数组运算。

>包含：
- 一个强大的N维数组对象ndarray
- 广播功能函数
- 整合C/C++/Fortran代码的工具
- 线性代数、傅里叶变换、随机数生成等功能

>优势：比直接使用Python代码编写更加便捷高效，numpy中数组的存储效率和输入输出性能远远优于Python中等价的基本数据结构，其能够提升性能食欲数组中的元素成比例的；numpy比纯Python代码高效得多。

>应用：Numpy常与Scipy（Scientific Python）和Matplotlib（绘图库）一起使用，这种组合广泛用于替代MATLAB，是一个强大的科学计算环境，有助于通过Python学习数据科学或者机器学习。

## 2、Ndarray对象简介
>介绍：ndarray对象是用于存放同**类型元素**的**多维**数组，每个元素在内存中有相同大小的存储区域。

Ndarray由不同部分组成，下面使用时再介绍。

# 二、Numpy的基本使用
## 1、Numpy数据类型
- Numpy包括以下几种数据类型：

| 数据类型  | 描述  |
| --- | ---------------------------------------------------------- |
|bool_|布尔型数据类型|
|int_|默认的整数类型（类似于c语言中的long,int32,int64）|
|intc|与d的int类型一样，一般是int32或者int64|
|intp|用于索引的整数类型|
|int8|字节（-128~127）|
|int16|整数（-32768~32767）|
|int32|整数（-2147483648~2147483647）|
|int64|整数（-9223372036854775808~9223372036854775807）|
|uint8|无符号整数（0~255）|
|uint16|无符号整数（0~65535）|
|uint32|无符号整数（0~4294967295）|
|uint64|无符号整数（0~18446744073709551615）|
|float_|float64类型的简写|
|float16|半精度浮点数，包括：1个符号位，5个指数位，10个尾数位|
|float32|半精度浮点数，包括：1个符号位，8个指数位，23个尾数位|
|float64|半精度浮点数，包括：1个符号位，11个指数位，52个尾数位|
|complex_|complex128的简写，即128位复数|
|complex64|复数，表示双32位浮点数（实数部分和虚数部分）|
|complex128|复数，表示双64位浮点数（实数部分和虚数部分）|

- 每个内建类型都有一个唯一定义它的字符代码：

|字符代码|描述|
| --- | ---------------------------------------------------------- |
|b|布尔型|
|i|有符号整型|
|u|无符号整型|
|f|浮点型|
|c|复数浮点型|
|m|timedelta时间间隔|
|M|datetime日期时间|
|O|Python对象|
|S、a|byte-字符串|
|U|Unicode|
|V|原始数据void|

- 数据类型对象(dtype)
    - 数据类型对象是用来描述与数组对应的内存区域如何使用，这依赖以下几个方面：
        - 数据的类型
        - 数据的大小
        - 数据的字节顺序
            - 大端法或小端法（通过对数据类型预先设定“<”或者“>”来决定的，“<”意味着小端法，最小值存储在最小的地址，即低位组放在最前面；">"意味着大端法，最重要的字节存储在最小的地址，即高位组放在最前面）
        - 在结构化类型的情况下，字段的名称、每个字段的数据类型和每个字段的内存快的部分
        - 如果数据类型是子数组，它的形状和数据类型

- 创建数据类型对象
    - 原型：numpy.dtype(object, align, copy)
        - object：要转换的数据类型对象
        - align：如果为true，填充字段位类似c的结构体
        - copy：复制dtype对象，如果为false，则是对内置数据类型对象的引用

代码示例：
```python
import numpy as np # 重命名为np
dt = np.dtype(np.int32)
print(dt)
print(type(dt))
# int32
# <class 'numpy.dtypes.Int32DType'>
```
<font color=#FF0000 ><font size=3 >代码解释：如果以后要创建Ndarray对象的时候，指定类型时指定为dt，那么Ndarray对象存的就是int32类型的数据。
</font></font>

1. 使用字符代码

代码示例：
```python
import numpy as np # 重命名为np
dt = np.dtype('i4') # 有符号整型 i1,i2,i4,i8
print(dt)
print(type(dt))
# int32
# <class 'numpy.dtypes.Int32DType'>
```
>i1表示int8，i2代表int16，i4代表int32，i8代表int64

2. 字节顺序的标注

代码示例：
```python
import numpy as np # 重命名为np
dt = np.dtype('<i4') # 小端法
print(dt)
print(type(dt))
# int32
# <class 'numpy.dtypes.Int32DType'>
```

3. 结构化类型

代码示例：
```python
import numpy as np # 重命名为np
student = np.dtype([("name", "S20"),("age", "i4"),("mark", "f4")]) # 名称、数据类型 S20是32个字符的字符串
print(student)
print(type(student))
# [('name', 'S20'), ('age', '<i4'), ('mark', '<f4')] 默认小端法
# <class 'numpy.dtypes.VoidDType'>
```

## 2、创建Ndarray数组对象
> 注意：Numpy默认Ndarray所有元素的类型是相同的。
> 若传进来的列表中包含不同的类型，则统一为同一类型，优先级：str>flaot>int

### array()函数
- 原型：numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
- 作用：创建Ndarray数组对象
    - object：数组或嵌套的数列
    - dtype：数组元素的数据类型（可选）
    - copy：对象是否需要复制（可选）

## 3、Numpy数组与Python中列表的对比


## 4、Ndarray数组属性


# 三、元素操作
