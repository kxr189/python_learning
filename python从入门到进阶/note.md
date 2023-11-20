---
title: python从入门到进阶（一）—— python语言基础入门
tags: [编程语言学习,python]
categories: [python,编程语言学习]
---

python从入门到进阶。
python简洁高效、应用场景丰富。

<!-- more -->

{% pullquote mindmap mindmap-md %}

- python从入门到进阶
  - python语言基础入门
  - python语言高阶加强
  - 大数据分析PySpark
    {% endpullquote %}

# 第一章

## 01 初始python

&ensp;&ensp;&ensp;&ensp;为什么选择python？
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;优雅、易学、开发效率高

## 02 什么是编程语言

&ensp;&ensp;&ensp;&ensp;语言：进行沟通交流的表达方式

&ensp;&ensp;&ensp;&ensp;编程语言是用于人类与计算机交流的一种语言，通过编写编程语言的代码，去指挥计算机工作。它无法直接与计算机沟通，需要翻译工具（解释器或编译器）将代码翻译为二进制，从而实现和计算机的顺畅沟通。

## 03 python环境安装（Windows）

&ensp;&ensp;&ensp;&ensp;下载python：python.org

## 04 python环境安装（MacOS）

略

## 05 python环境安装（Linux）

略

## 06 第一个python程序-Hello World

win+R --> cmd --> python
出现三个">>>"后就可以输入python代码了
双引号和括号都得是英文输入法下的符号。

```python
print("hello,world")
print("你好世界")
```

## 07 python解释器

    基本原理：计算机只认识二进制0和1.

python解释器是一个计算机程序，用来翻译python代码，并提交给计算机执行。
所以，它的功能就两个：翻译代码、提交给计算机执行。、

在命令窗口内直接敲代码只能执行一行，若要执行多行可以新建.py文件，再在命令窗口下输入：

```
C:\Users\22773>python C:\Users\22773\Desktop\pythonlearning\编程基础学习\test.py
hello world
```

## 08 PyCharm开发工具的安装

略

## 09 PyCharm的基础使用

1、修改pycharm的主题：

> 齿轮->主题

2、修改默认字体的大小

> 设置-编辑器-字体

3、设置快捷键快速设置字体大小

> 设置-按键映射

4、常用快捷键

> ctrl+d 复制当前行代码
> shift+alt+上/下 将当行代码上移或下移
> ctrl+shift+f10 运行当前代码文件
> shift+f6 重命名

# 第二章 基础语法

## 01 字面量

> 概念：在代码中，被**写下来的固定的值**，称之为**字面量**。

常用的值类型：
python中常用的

<table>
    <tr>
        <th>班级</th><th>课程</th><th>平均分</th>
    </tr>
    <tr>
        <td rowspan="3">1班</td><td>语文</td><td>95</td>
    </tr>
    <tr>
        <td>数学</td><td>96</td>
    </tr>
    <tr>
        <td>英语</td><td>92</td>
    </tr>
</table>

## 02 注释

> 注释的作用:在程序代码中对程序代码进行解释说明的文字

> 单行注释：#开头

```python
# 我是注释
```

> 多行注释：用一对三个双引号引起来的内容

```python
"""我是注释
我可以换行
"""
```

## 03 变量

> 什么是变量？
> 
> > 在程序运行时，能存储计算结果或者能表示值的抽象概念。

> 变量的定义格式：变量名称 = 值

```python
# 定义一个变量，用来记录钱包余额
money = 50
# 利用print语句打印出来
print("钱包还有：",money)
# 买了一个冰淇淋，花费10元
money = money - 10
print("钱包余额：",money,"元")
# 每隔一小时输出钱包的余额
print("现在是下午1点，钱包余额剩余：",money)
print("现在是下午2点，钱包余额剩余：",money)
print("现在是下午3点，钱包余额剩余：",money)
print("现在是下午4点，钱包余额剩余：",money)
```

## 04 数据类型

### 1、type()语句

使用方式：
1、在print语句中直接输出类型信息，代码示例如下：

```python
print(type(1.314))
print(type(1314))
print(type("我爱作者"))
"""
输出如下：
<class 'float'>
<class 'int'>
<class 'str'>
"""
```

2、用变量存储type()的结果（返回值）

```python
float_type = type(1.314)
int_type = type(1314)
string_type = type("我爱作者")
print(float_type)
print(int_type)
print(string_type)
"""
输出如下：
<class 'float'>
<class 'int'>
<class 'str'>
"""
```

3、type()语句还可以查看变量中存储的数据类型

```python
name = "柯锡荣"
name_type = type(name)
print(name_type)
"""
输出如下：
<class 'str'>
"""
```

<font color=#FF000 ><font size=5 >**type()查看的是变量存储的数据的类型，变量无类型，但是它存储的数据有**</font></font>

## 05 数据类型的转换

> 为什么要转换类型？
> 
> > - 从文件中读取的数字，默认是字符串，需要转换为数字类型
> > - 后续学习的input语句，默认是字符串，若需要数字也需要转换
> > - 将数字转换成字符串用以写到外部系统
> > - 等等

常见的转换语句：

<table>
    <tr>
        <th>语句（函数）</th><th>说明</th>
    </tr>
    <tr>
        <th>int(x)</th><th>将x转换为一个整数</th>
    </tr>
    <tr>
        <th>float(x)</th><th>将x转换为一个浮点数</th>
    </tr>
    <tr>
        <th>str(x)</th><th>将对象x转换为字符串</th>
    </tr>
</table>
这三个语句都是带有结果的（返回值），可以用print()语句输出，或者用变量存储。

代码示例：

```python
# 将数字类型转化为字符串
num_str = str(11)
print(type(num_str),num_str)
# 输出结果：<class 'str'> 11
float_str = str(13.14)
print(type(float_str),float_str)
# 输出结果：<class 'str'> 13.14
# 将字符串转化为数字
num = int("11")
print(type(num),num)
num2 = float("13.14")
print(type(num2),num2)
# 输出结果：
# <class 'int'> 11
# <class 'float'> 13.14

# 万物皆可以转换为字符串，而字符串不是都可以转换为数字

# 整数转换为浮点数
float_num = float(11)
print(type(float_num),float_num)
# 输出结果：<class 'float'> 11.0
# 浮点数转换为整数
int_num = int(11.6)
print(type(int_num),int_num)
# 输出结果：<class 'int'> 11
# 小数转换为整数会丢失精度
```

- **小数转换为整数会丢失精度**
- **万物皆可以转换为字符串，而字符串不是都可以转换为数字**

## 06 标识符

### 1、标识符的命名规则

> 什么是标识符？
> 
> > 用户在编程中所使用的一系列名字，用于给变量、类、方法等命名。

标识符命名规则： 

- 内容限定：命名只允许出现英文、中文、数字和下划线。
  - 不推荐使用中文
  - 数字不可以开头
- 大小写敏感
  - 同样适用于关键字
- 不可使用关键字
  - 关键字在python中都有特定的用途，不可以使用为标识符

代码示例：

```python
# 规则1：内容限定：中英文、数字、下划线_
# 1_name = "张三" 会报错
# name_! = "张三" 也会报错
name_ = "张三"
name_1 = "李四"

# 规则2：大小写敏感
Itheima = "黑马"
itheima = "666"
print(Itheima,itheima)
# 运行结果：
# 黑马 666

# 规则3：不能使用关键字
# class = 1 会报错
# def = 1 会报错
Class = 1
print(Class)
# 运行结果：1
```

### 2、标识符的命名规范

不同标识符（变量、类、方法）有不同的规范，目前先学习变量的命名规范。

变量的命名规范：

- 见名知意（明了、简洁）
- 下划线命名法：多个单词组合变量名，用下划线做分隔
- 英文字母全小写

## 07 运算符

### 1、算术运算符

令a-10,b=20，解释各运算符

<table>
    <tr>
        <th>运算符</th><th>描述</th><th>实例</th>
    </tr>
    <tr>
        <th>+</th><th>加</th><th>a+b=30</th>
    </tr>
    <tr>
        <th>-</th><th>减</th><th>a-b=-10</th>
    </tr>
    <tr>
        <th>*</th><th>乘</th><th>a*b=200</th>
    </tr>
    <tr>
        <th>/</th><th>除</th><th>b/a=2</th>
    </tr>
    <tr>
        <th>//</th><th>取整除</th><th>返回商的整数部分，9//2输出结果为4，9.0//2.0=4.0</th>
    </tr>
    <tr>
        <th>%</th><th>取余</th><th>返回除法的余数，b%a的结果为0</th>
    </tr>
    <tr>
        <th>**</th><th>指数</th><th>a**B为10的20次方，输出结果为100000000000000000000</th>
    </tr>
</table>

示例代码：

```python
# 算术（数学）运算符
print("1+1=",1+1)
print("2-1=",2-1)
print("3*3=",3*3)
print("4/2=",4/2)
print("11//2=",11//2)
print("9%2=",9%2)
print("2**2=",2**2)
# 结果：
# 1+1= 2
# 2-1= 1
# 3*3= 9
# 4/2= 2.0
# 11//2= 5
# 9%2= 1
# 2**2= 4
```

### 2、赋值运算符

<table>
    <tr>
        <th>运算符</th><th>描述</th><th>实例</th>
    </tr>
    <tr>
        <th>=</th><th>赋值运算符</th><th>将等号右边的值 赋给 左边的变量</th>
    </tr>
</table>

此外还有复合赋值运算符：

<table>
    <tr>
        <th>运算符</th><th>描述</th><th>实例</th>
    </tr>
    <tr>
        <th>+=</th><th>加法赋值运算符</th><th>c+=a 等价于 c=c+a</th>
    </tr>
    <tr>
        <th>-=</th><th>减法赋值运算符</th><th>c-=a 等价于 c=c-a</th>
    </tr>
    <tr>
        <th>*=</th><th>乘法赋值运算符</th><th>c*=a 等价于 c=c*a</th>
    </tr>
    <tr>
        <th>/=</th><th>除法赋值运算符</th><th>c/=a 等价于 c=c/a</th>
    </tr>
    <tr>
        <th>//=</th><th>取整除赋值运算符</th><th>c//=a 等价于 c=c//a</th>
    </tr>
    <tr>
        <th>%=</th><th>取模赋值运算符</th><th>c%=a 等价于 c=c%a</th>
    </tr>
    <tr>
        <th>**=</th><th>幂赋值运算符</th><th>c**=a 等价于 c=c**a</th>
    </tr>
</table>

## 08 字符串拓展

### 1、字符串的三种定义方式

- 单引号定义法：name='hello'
- 双引号定义法：name="hello"
- 三引号定义法：name="""hello"""
- 三引号定义法和多行注释一样，同样支持**换行**操作；使用变量接收它，就是字符串，不用就是注释。

代码示例“

```python
# 单引号定义法：
name1='hello'
# 双引号定义法：
name2="hello"
# 三引号定义法：
name3="""he
llo"""
print(type(name1),name1)
print(type(name2),name2)
print(type(name3),name3)
"""运行结果：
<class 'str'> hello
<class 'str'> hello
<class 'str'> he
llo
"""
```

- 字符串的引号嵌套：
  - 单引号定义法可以内含双引号
  - 双引号定义法可以内含单引号
  - 可以使用转义字符（\）来将引号解除效用，变成普通字符串

```python
# 字符串内包含双引号
name = 'hello""'
print(name)
# 字符串内包含单引号
name1 = "hello''"
print(name1)
# 使用(\)
name2 = "hello\'\'"
print(name2)
"""输出结果：
hello""
hello''
hello''
"""
```

### 2、字符串的拼接


<font color=#FF0000 ><font size=3 >**如果有多个字符串字面量，可以通过+号拼接为一个字符串**</font></font>


```python
# I love myself
print("I"+" "+"love"+" "+"myself")
```

还可以变量与变量、变量与字面量之间进行拼接

```python
# I love myself
name = "myself"
name1 = "I"
print(name1+" "+"love"+" "+name)
```

**注意**：用+号进行拼接的只能是字符串。

### 3、字符串格式化

首先给出一段代码：

```python
# I love myself
name = "myself"
message = "I love %s" % name
print(message)
```

其中：**%s**中，%表示占位，s表示将变量变成字符串放入占位的地方

其他类型的变量也可以，代码示例：

```python
# I love myself , 520
name = "myself"
num = 520
message = "I love %s , %s" % (name,num)
print(message)
```

python支持非常多的数据类型占位，最常用的三类如下：

| 格式符号 | 转化              |
|:----:|:---------------:|
| %s   | 将内容转化为字符串放入占位位置 |
| %d   | 将内容转化为整数放入占位位置  |
| %f   | 将内容转化为浮点型放入占位位置 |

代码示例；

```python
# I love 20 13.140000
name = "I"
zhenshu = 20
fudianshu = 13.14
message = "%s love %d %f" % (name,zhenshu,fudianshu)
print(message)
```

### 4、格式化的精度控制

- 数字精度控制：可以用辅助符号”m.n“来控制数据的宽度和精度，m控制宽度，n控制精度，会进行四舍五入（被修约的数为5时，需要看前一位的数字，若是奇数则进位，若是偶数则将5省掉）
  
  ```python
  num1 = 11
  num2 = 11.11
  print("num1 = %5d" % num1)
  print("num2 = %.1f" % num2)
  """结果：
  num1 =    11
  num2 = 11.1
  """
  ```

### 5、字符串格式化的方式2

- 快速写法：f"内容{变量}"
- 特点：不限制数据类型，不做精度控制

代码示例：

```python
name = "I"
year = 2002
height = 171.5
print(f"{name} am born in {year} , and my height is {height}")
# I am born in 2002 , and my height is 171.5
```

### 6、对表达式进行格式化

- 什么是表达式？表达式是指一条具有明确执行结果的代码语句。
- 如：1+1、%*2
- 变量定义也是 name = "mike"

代码示例：

```python
print("1 * 1的结果是：%d" % (1*1))
print(f"1 * 2的结果是：{1*2}")
print("字符串在python中的类型名是：%s" % type('字符串'))
"""输出结果：
1 * 1的结果是：1
1 * 2的结果是：2
字符串在python中的类型名是：<class 'str'>
"""
```

练习题：股价计算小程序

```python
name = "传智播客"
stock_price = 19.99
stock_code = '003032'
stock_price_daily_growth_factor = 1.2
growth_days = 7

print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%s，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,stock_price * stock_price_daily_growth_factor ** growth_days))
```

## 09 数据输入(input()语句的使用)

- input语句可以从键盘中获取键盘输入

代码示例：

```python
print("请告诉我你是谁?")
name = input()
print("你是%s" % name)
"""结果：
请告诉我你是谁?
nidie
你是nidie
"""
```

其他编写方式：

```python
name = input("请告诉我你是谁?")
print("你是%s" % name)
"""结果：
请告诉我你是谁?
nidie
你是nidie
"""
```

input语句中不论键盘输入什么，都看作字符串。
需要其他数据类型时请用数据类型转换指令。

# 第三章 Python判断语句

## 01 布尔类型和比较运算符

- 布尔类型：只有两个结果
  - 是、真
  - 否、假
- 布尔类型不仅可以自行定义，也可以通过比较得到

```python
# 定义变量存储bool类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}，类型是：{type(bool_2)}")
# 比较运算符的使用 == , != , > , < , >= , <=
num1 = 10
num2 = 10
print(f"10 == 10 的结果是：{num2 == num1}")
num1 = 11
num2 = 10
print(f"11 != 10 的结果是：{num2 != num1}")
name1 = "a"
name2 = "b"
print(f"name1 == name2 的结果是：{name1 == name2}")
```

## 02 if语句的基本格式

格式：
if 要判断的条件：
&ensp;&ensp;&ensp;&ensp;条件成立时要做的事情
代码示例：

```python
age = int(input("你几岁？"))
if age >= 18:
    print("你老了")
```

**注意**：判断语句的结果必须是bool类型，此外，不要忘记冒号

## 03 if else 语句

代码示例：

```python
age = int(input("你几岁？"))
if age >= 18:
    print("你老了")
else:
    print("还可以")
```

## 04 if elif else 语句

多条件判断
代码示例：

```python
age = int(input("你几岁？"))
if age < 18:
    print("young")
elif age > 90:
    print("old")
else:
    print("good")
```

**注意**：判断是互斥的且有顺序的，满足了就执行，后面的条件就不再进行判断

## 05 判断语句的嵌套

嵌套的关键点在于<font color=#FF000 ><font size=4 >空格缩进</font></font>
代码示例：

```python
age = int(input("你几岁？"))
if age < 18:
    print("young")
else:
    if age > 20:
        print("young1")
    else:
        print("young2")
```

## 06 实战案例

> 使用逻辑判断语句，完成猜数字的案例代码编写
> 案例要求：随机产生一个数字0-10，通过三次判断来猜出数字，猜错会进行大小提示。

```python
import random
num = random.randint(1, 10)
num_guess = int(input("请输入你所猜到的数字："))
if num_guess == num:
    print("恭喜，你一次就猜中了！")
else:
    if num_guess > num:
        print("数字猜大了！")
    elif num_guess < num:
        print("数字猜小了")
    num_guess = int(input("请输入你所猜到的数字："))
    if num_guess == num:
        print("恭喜，你第二次就猜中了！")
    else:
        if num_guess > num:
            print("数字猜大了！")
        elif num_guess < num:
            print("数字猜小了")
        num_guess = int(input("请输入你所猜到的数字："))
        if num_guess == num:
            print("恭喜，你最后一次猜中了！")
        else:
            print("很遗憾，三次机会已用完！")
```

# 第四章 Python循环语句

## 01 while循环的基础语法

结构：

```python
# while 条件:
#     条件满足时，做的事情1
#     条件满足时，做的事情2
#     条件满足时，做的事情3
#     ......
```

代码示例：

```python
i = 100
while i >= 0:
    print(i)
    i = i - 1
```

注意：while循环的条件需要得到bool类型，此外，循环要设置终止条件。
练习：求1-100的和

```python
i = 1
s = 0
while i <= 100:
    s = s + i
    i = i + 1
print("1+2+3+...+100=",s) # 5050
```

## 02 while循环的基础案例

练习：设置1-100的随机整数，通过while循环，配合input语句，判断数字是否等于所猜数字，机会无限，猜完数字后提示次数。

```python
import random
num = random.randint(1,100)
i = 1
guess_num = int(input("输入你猜的数字："))
while guess_num != num:
    if guess_num > num:
        print("你猜的数字大了！")
    else:
        print("你猜的数字小了！")
    i = i + 1
    guess_num = int(input("再次输入你猜的数字："))
print("恭喜你猜对了，一共猜了 %s 次" % i)
```

## 03 while循环的嵌套应用

代码示例：

```python
i = 1
while i <= 100:
    print(f"今天是第{i}天")
    j = 1
    while j <= 10:
        print(f"送给她的第{j}朵玫瑰")
        j += 1
    i = i + 1
```

注意：基于空格缩进来控制层次。

## 04 while循环的嵌套案例

> 知识点补充：
> 
> > 默认print语句输出内容会自动换行，若要不换行，则在print语句中加入end=''就可以了
> > 代码示例：

```python
# hello world
print("hello ", end='')
print("world", end='')
```

> > 制表符：\t，效果等同于键盘上按下Tab健，可以使多行字符串对齐。
> > 代码示例：

```python
# 如果字符差距超过两个则需要两个\t
print("he\t\tworld")
print("hello\tworld")
print("hellolo\tworld")
"""结果：
he        world
hello    world
hellolo    world
"""
```

练习案例：通过while循环输出9*9乘法表
代码示例：

```python
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j}\t",end='')
        j += 1
    i += 1
    print() # print输出空内容就是换行
# 1*1=1    
# 1*2=2    2*2=4    
# 1*3=3    2*3=6    3*3=9    
# 1*4=4    2*4=8    3*4=12    4*4=16    
# 1*5=5    2*5=10    3*5=15    4*5=20    5*5=25    
# 1*6=6    2*6=12    3*6=18    4*6=24    5*6=30    6*6=36    
# 1*7=7    2*7=14    3*7=21    4*7=28    5*7=35    6*7=42    7*7=49    
# 1*8=8    2*8=16    3*8=24    4*8=32    5*8=40    6*8=48    7*8=56    8*8=64    
# 1*9=9    2*9=18    3*9=27    4*9=36    5*9=45    6*9=54    7*9=63    8*9=72    9*9=81    
```

## 05 for循环的基础语法

### 1、基础语法

结构：

```python
# for 临时变量 in 待处理数据集:
#     循环满足条件时执行的代码
```

代码示例：

```python
name = "itheima"
for x in name:
    # 将name的内容挨个取出
    print(x)
```

for循环也被称之为：**遍历循环**
注意：同while循环不一样，for循环无法定义循环条件，只能被动地读取数据处理。

> 练习：统计“itheima is a brand of itcast“中有多少个a

```python
name = "itheima is a brand of itcast"
i = 0
for x in name:
    if x == 'a':
        i = i + 1
print(f"{i}个a")
```

### 2、range语句

```python
# for 临时变量 in 待处理数据集:
#     循环满足条件时执行的代码
```

在for语句的结构中，**待处理数据集**严格来说，称之为：<font color=#FF000 ><font size=4 >序列类型</font></font>

> 序列类型：其内容可以一个个依次取出的一种类型，包括：

- 字符串
- 列表
- 元组
- 等

for循环语句本质上是便利序列类型。

<font color=#FF000 ><font size=4 >range语句：用于获得一个简单的数字序列。</font></font>

> 语法一：
> 
> > range(num)
> > 获取一个从0开始，到num结束的数字序列，不包含num本身。如：range(5)取出的数据是：[0,1,2,3,4]

> 语法二：
> 
> > range(num1,num2)
> > 获取一个从num1开始，到num结束的数字序列，不包含num2本身。

> 语法三：
> 
> > range(num1,num2,step)
> > 获取一个从num1开始，到num2结束的数字序列，不包含num2本身；step为步长。

代码示例：

```python
for x in range(10):
    print(x) # 0 1 2 3 4 5 6 7 8 9

for y in range(2,4):
    print(y) # 2 3

for z in range(3,6,2):
    print(z) # 3 5
```

### 3、变量作用域

在for循环中，临时变量只在for循环内生效，但实际上在for循环外也能使用，但规范上不推荐。

## 06 for循环的嵌套应用

代码示例：

```python
i = 1
for i in range(1,101):
    print(f"今天是第{i}天，坚持")
    for j in range(1,3):
        print(f"今天读了{j}本书")
```

练习：使用for循环绘制9*9乘法表

```python
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t",end='')
    print() # 换行
```

## 07 循环中断：break和continue

### 1、continue关键字

作用：中断本次循环，直接进入下一次循环；可用于for和while循环。
注意：continue只能影响所在层的循环。
代码示例：

```python
# 不会出现3
for i in range(1,6):
    print("1")
    for j in range(1,2):
        print("2")
        continue
        print("3")
    print("4")
```

### 2、break关键字

作用：直接结束循环；可用于for和while循环。
注意：是直接结束当前当层循环。

## 08 综合案例

练习案例：发工资
某公司，账户余额有1W元，给20名员工发工资。
员工编号1-20，从编号1开始，依次领取工资，每人可以领取1000元；领取工资时，财务判断员工的绩效（1-10，随机生成），如果低于5则不发工资；如果工资发完后则结束发工资。

```python
import random
money = 10000
sum = 20
for i in range(1,21):
    jixiao = random.randint(1,10)
    if jixiao < 5:
        print(f"员工{i}，绩效分{jixiao}，低于5，不发工资，账户余额{money}")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}，绩效分{jixiao}，高于5，发放工资1000元，账户余额{money}")
    else:
        print("工资发完了，下个月再领取吧。")
        break
```

# 第五章 python函数

## 01 函数介绍

> 函数:是组织好的，**可重复使用**的，用来实现特定功能的代码段。

> 使用函数的好处：可供随时重复使用；提高代码的复用性，减少重复代码，提高开发效率。

实际案例：

```python
str1 = "aaa"
str2 = "aaaa"

# 定义函数统计字符串长度
def my_len(str):
    count = 0
    for i in str:
        count += 1
    print(f"length_{str} = {count}")

my_len(str1)
my_len(str2)

# length_aaa = 3
# length_aaaa = 4
```

## 02 函数的定义

函数的定义语法如下：

```python
# 函数的定义：
# def 函数名(传入参数):
#     函数体
#     return 返回值
```

代码示例：

```python
# 定义函数
def say_hi():
    print("hi")
# 函数的调用
say_hi()
```

注意：函数要先定义后调用；传入参数可以省略。

## 03 函数的参数

传入参数的功能：在函数进行计算的时候，接受外部调用时提供的数据。
代码示例：

```python
def add(x, y):
    result = x + y
    print(f"{x}+{y}={result}")

while(True):
    x = int(input("输入x："))
    y = int(input("输入y："))
    add(x, y)
```

> 在函数定义中，提供的x和y称之为<font color=#FF000 ><font size=3 >**形参**</font></font>，表示参数声明要使用两个参数。

> 在函数调用中，提供的实际数字x和y称之为<font color=#FF000 ><font size=3 >**实参**</font></font>，表示函数执行时用到的真正参数值。

传入参数的数量是不受限制的。

## 04 函数的返回值

> 什么是返回值？
> 
> > 返回值就是程序中函数完成事情后，最后给调用者的一个结果。

代码示例：

```python
def add(x, y):
    result = x + y
    return result

while(True):
    x = int(input("输入x："))
    y = int(input("输入y："))
    result = add(x, y)
    print(f"{x}+{y}={result}")
```

注意：函数体遇到return关键字后面的就不会再执行了，表示函数已经结束了。

> none类型：无返回值的函数实际上是返回了none这个字面量。

代码示例：

```python
def add(x, y):
    result = x + y

result = add(1,1)
print("无返回值的函数返回值类型是",type(result))
# 无返回值的函数返回值类型是 <class 'NoneType'>
```

> none的使用价值：
> 
> > 可用于if判断上，none = false \
> > 可用于声明无初始值的变量

```python
# none 用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None

result = check_age(16)

if not result:
    # 进入if表示result是None值 也就是Fslse
    print("未成年，不可以进入")
```

## 05 函数说明文档

函数是纯代码语言，可以给函数添加说明文档，辅助理解函数的作用。\
按三下双引号加回车会自动写好格式。\
推荐写法如下：

```python
def add(x, y):
    """
    add函数可以接受两个参数，实现两数相加的功能
    :param x: 数1
    :param y: 数2
    :return: 两数相加的结果
    """
    result = x + y
    return result
# 悬停在函数上方会弹出说明文档
result = add(1,2)
```

## 06 函数的嵌套调用

> 什么是函数的嵌套：就是一个函数里面调用另外一个函数。

## 07 变量的作用域

> 变量的作用域：
> 
> > 指的是变量的作用范围。分为局部变量和全局变量。

> 局部变量：
> 
> > 定义在函数体内部的变量，即只在函数体内部生效。

> 局部变量的作用：
> 
> > 在函数体内部临时保存数据，函数调用完成后立刻销毁局部变量。

代码示例：

```python
# 演示局部变量
def test_a():
    num = 100
    print(num)

test_a()
# print(num) 会报错，
# 出了函数，局部变量就无法使用了。
```

> 全局变量：
> 
> > 在函数体内部、外部都可以生效的变量。

代码示例：

```python
# 演示全局变量
num = 100
def test_a():
    print(num)

test_a()
# print(num) 不会报错，
# 出了函数，全局变量还是能够使用了。
```

> global关键字

```python
# 演示全局变量
num = 100
def test_a():
    num = 200 # 这个num和函数外的num没有任何关系
    # 里面的num是局部变量，函数外部的num是全局变量
    print(num)

test_a() # 200
print(num) # 100
```

使用global关键字就可以在函数内部修改全局变量了。

代码示例：

```python
# 演示全局变量
num = 100
def test_a():
    global num
    num = 200
    print(num)

test_a() # 200
print(num) # 200
```

## 08 综合案例

<img src="\img\python从入门到进阶（一）\python-函数入门案例图1.jpg" alt="黑马ATM" title="黑马ATM">

代码示例：
{% spoiler "点击显/隐内容" %}

```python
# 定义全局变量
money = 5000000
name = None
# 客户姓名输入
name = input("请输入您的姓名：")
# 查询查询函数
def query(show_header):
    if show_header:
        print("----------查询余额----------")
    print(f"{name}，您好，当前的余额为{money}元")

# 存款函数
def saving(num):
    global money
    money += num
    print("----------存款----------")
    print(f"{name}，您好，您存款{num}元成功。")
    query(False)

# 取款函数
def get_money(num):
    global money
    print("----------取款----------")
    if money >= num:
        money -= num
        print(f"{name}，您好，您取款{num}元成功。")
        query(False)
    else:
        print(f"{name}，您好，您的余额不足，余{money}元。")

# 主菜单效果
def main():
    print("----------主菜单----------")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return  input("请输入你的选择：")

while True:
    choice = main()
    if choice == "1":
        query(True)
        continue
    elif choice == "2":
        num = int(input("请输入存款数额："))
        saving(num)
        continue
    elif choice == "3":
        num = int(input("请输入取款数额："))
        get_money(num)
        continue
    else:
        print("程序退出。")
        break
```

{% endspoiler %}

# 第六章 Python数据容器

## 01 数据容器入门

> 数据容器是什么？
> 
> > 一种可以容纳多份数据的数据类型，容纳的每一份数据称之为一个元素；每一个元素可以是任意类型的数据，如字符串、数字、bool等

> 为什么要学习数据容器？
> 
> > 可用于存储大量数据，不用分成很多变量保存数据。

数据容器根据特点的不同，如：

- 是否支持重复元素
- 是否可以修改
- 是否有序等
  分为5类：列表list、元组tuple、字符串str、集合set、字典dict

## 02 数据容器：list（列表）

### 1、列表的定义

- 列表的定义语法：
  
  ```python
  # 字面量
  # [元素1,元素2,元素3,......]
  # 
  # 定义变量
  # 变量名称 = [元素1,元素2,元素3,......]
  # 
  # 定义空列表
  # 变量名称 = []
  # 变量名称 = list()
  ```
- 注意事项：列表可以一次性存储多个数据，且<font color=#FF000 ><font size=3 >**可以为不同数据类型，支持嵌套。**</font></font>

代码示例：

```python
name_list = ['I', 'love', 'kxr']
print(name_list)
print(type(name_list))

name_list1 = ['I', 1, 1.1]
print(name_list1)
print(type(name_list1))

name_list2 = ['I', 1, [1, 2, 3]]
print(name_list2)
print(type(name_list2))
```

### 2、列表的索引

- 列表的下标索引：
  
代码示例：
  
```python
name_list = ['I', 'love', 'kxr']
print(name_list)
print(type(name_list))

# 下标索引

print(name_list[0])
print(name_list[1])
print(name_list[2])

```
- 列表还可以进行反向索引：最后一个元素标记为-1，倒数第二个标记位-2，依次往前递减

代码示例：
```python
name_list = ['I', 'love', 'kxr']
print(name_list)
print(type(name_list))

# 下标的反向索引
print(name_list[-3])
print(name_list[-2])
print(name_list[-1])
```

- 嵌套列表的下标索引

代码示例： 
```python
name_list = ['I', 'love', [1, 2, 3]]
print(name_list)
print(type(name_list))

# 下标索引

print(name_list[2][0])
print(name_list[2][1])
print(name_list[2][2])

# ['I', 'love', [1, 2, 3]]

# <class 'list'>

# 1

# 2

# 3

```
### 3、列表的常用操作（方法）
- 插入元素
- 删除元素
- 清空列表
- 修改元素
- 统计元素个数
- 等等
以上功能都称之为：<font color=#FF000 ><font size=4 >**列表的方法**</font></font>

#### 查询的功能（方法）
查找某元素的下标，如果找不到，就报错ValueError
语法：列表.index(元素)
代码示例：
```python
name_list = ['I', 'love', [1, 2, 3]]
# 查找下标索引
index = name_list.index([1,2,3])
print(index) # 2
# 如果元素不存在会报错
# index = name_list,index(1)
```

#### 修改功能（方法）

修改特定位置的元素值
语法：列表[下标] = 值
注意：正反下标均可以。
代码示例：

```python
name_list = ['I', 'love', [1, 2, 3]]
# 修改功能
name_list[1] = "O"
print(name_list) # ['I', 'O', [1, 2, 3]]
```

#### 插入元素

语法：列表.insert(下标，元素)，在指定的下标位置，插入指定的元素
代码示例：

```python
name_list = ['I', 'love', [1, 2, 3]]
# 插入元素
name_list.insert(1,2)
print(name_list) # ['I', 2, 'love', [1, 2, 3]]
```

#### 追加元素

语法：列表.append(元素)，将指定元素追加到列表的尾部。
代码示例：

```python
name_list = ['I', 'love', [1, 2, 3]]
# 追加元素
name_list.append(2)
print(name_list) # ['I','love', [1, 2, 3], 2]
```

还可以追加一批元素：
语法：列表.extend(其他数据容器)，将其他数据容器的内容取出，依次追加到列表尾部。
代码示例：

```python
name_list = ['I', 'love', [1, 2, 3]]
# 追加元素
name_list.extend([1,2,3])
print(name_list) # ['I','love', [1, 2, 3], 1, 2, 3]
```

注意：append和extend都可以追加一批元素，但append是将这批追加的元素作为整体追加到列表尾部。
代码示例：

```python
name_list = ['I', 'love', [1, 2, 3]]
name_list1 = ['I', 'love', [1, 2, 3]]
# 追加元素
name_list.extend([1,2,3])
print(name_list) # ['I','love', [1, 2, 3], 1, 2, 3]
name_list1.append([1,2,3])
print(name_list1) # ['I','love', [1, 2, 3], [1, 2, 3]]
```

#### 清空列表

- 语法1：del列表[下标]
- 语法2：列表.pop(下标) 将元素取出并返回
  代码示例：
  
  ```python
  name_list = ['I', 'love', [1, 2, 3]]
  name_list1 = ['I', 'love', [1, 2, 3]]
  # 删除元素
  del name_list[2]
  print(name_list)
  result = name_list1.pop(2)
  print(name_list1,result)
  # ['I', 'love']
  # ['I', 'love'] [1, 2, 3]
  ```
- 删除某个元素在列表中的第一个匹配项
  语法：列表.remove(元素)
  代码示例：
  
  ```python
  name_list = ['I', 'love', 'I',[1, 2, 3]]
  # 删除元素
  name_list.remove('I')
  print(name_list) # ['love', 'I', [1, 2, 3]]
  ```

#### 清空列表

语法：列表.clear()
代码示例：

```python
name_list = ['I', 'love', 'I',[1, 2, 3]]
# 清空列表
name_list.clear()
print(name_list) # []
```

#### 统计元素数量

语法：列表.count(元素)
代码示例：

```python
name_list = [1,1,1,1,2,3,3,4,4,4,]
# 统计元素数目
num = name_list.count(2)
print(num) # 1
```

#### 统计列表元素总数

语法：len(列表)
代码示例：

```python
name_list = [1,1,1,1,2,3,3,4,4,4,]
# 统计数目
num = len(name_list)
print(num) # 10
```

案例练习：

<img src="\img\python从入门到进阶（一）\python-列表课后练习.jpg" alt="常用功能练习" title="常用功能练习">

代码示例：

```python
# 定义这个列表并用变量接收
name_list = [21,25,21,23,22,20]
# 追加数字31到列表尾部
name_list.append(31)
# 追加一个新列表[29,33,30]到列表尾部
name_list.extend([29,33,30])
# 取出第一个元素
first = name_list.pop(0)
print(f"第一个元素是{first}")
# 取出最后一个元素
end = name_list.pop(-1)
print(f"最后一个元素是{end}")
# 查找元素31在列表中的下标位置
location = name_list.index(31)
print(f"31在列表中的位置为{location}")
# 第一个元素是21
# 最后一个元素是30
# 31在列表中的位置为5
```

## 03 list（列表）的遍历

### 1、while循环

循环条件用下标来控制。

代码示例：

```python
def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    my_list = ["I", "love", "myself"]
    i = 0
    while i < len(my_list):
        print(my_list[i])
        i += 1

list_while_func()
```

### 2、for循环

代码示例：

```python
def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return: None
    """
    my_list = ["I", "love", "myself"]
    i = 0
    for i in my_list:
        print(i)

list_for_func()
```

## 04 数据容器：tuple（元组）

### 1、元组的定义格式

- 元组定义：定义元组使用**小括号**，且使用逗号隔开各个数据，数据可以是不同的数据类型。

- 定义格式如下：
  
  ```python
  # 定义元组字面量
  # (元素,元素,元素,元素......)
  # 定义元组变量
  # 变量名称 = (元素,元素,元素,元素......)
  # 定义空元组
  # 变量名称 = ()
  # 变量名称 = tuple()
  ```

代码示例：

```python
# 定义元组变量
# 变量名称 = (元素,元素,元素,元素......)
t1 = (1, "hello", True)
# 定义空元组
# 变量名称 = ()
# 变量名称 = tuple()
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}，内容是：{t1}")
print(f"t2的类型是：{type(t2)}，内容是：{t2}")
print(f"t3的类型是：{type(t3)}，内容是：{t3}")
# t1的类型是：<class 'tuple'>，内容是：(1, 'hello', True)
# t2的类型是：<class 'tuple'>，内容是：()
# t3的类型是：<class 'tuple'>，内容是：()
```

- 注意：元组只有一个数据时，这个数据后面需要添加括号

代码示例：

```python
t1 = (1, )
t2 = (1)
print(f"type_t1 = {type(t1)}, content_t1 = {t1}")
print(f"type_t2 = {type(t2)}, content_t2 = {t2}")
# type_t1 = <class 'tuple'>, content_t1 = (1,)
# type_t2 = <class 'int'>, content_t2 = 1
```

可以发现t2不是元组

- 元组同样支持嵌套
- 元组的索引也是通过下标来索引，用中括号

代码示例：

```python
t1 = ((1, 2, 3), (4, 5, 6))
print(t1[0][0]) # 1
```

### 2、元组的特点

列表是可以修改的，而**元组一旦定义就不可以修改**。

当我们只需要在程序内封装数据，又不希望封装的数据被篡改，那么元组就非常合适了。

### 3、元组的常见操作

#### 查询功能

语法：元组.index(元素)

代码示例：

```python
t1 = (1, 2, 3, 4, 5, 6)
location = t1.index(5)
print("元素5的位置是",location) # 元素5的位置是 4
```

#### 统计元素个数

语法：元组.count(元素)

代码示例：

```python
t1 = (1, 2, 3, 4, 5, 6, 5)
print(t1.count(5))
# 2
```

#### 统计元素总数

语法：len(元组)

代码示例：

```python
t1 = (1, 2, 3, 4, 5, 6, 5)
print(len(t1))
# 7
```

#### 元组的遍历while

代码示例：

```python
t1 = (1, 2, 3, 4, 5, 6, 5)
i = 0
while i < len(t1):
    print(t1[i])
    i += 1
```

#### 元组的遍历for

代码示例：

```python
t1 = (1, 2, 3, 4, 5, 6, 5)
for i in t1:
    print(i)
```

#### 元组嵌套列表

元组里面嵌套一个列表是可以修改列表中的元素的。

代码示例：

```python
t1 = (1, 2, 3, [4, 5, 6, 5])
t1[3][3] = 7
print(t1) # (1, 2, 3, [4, 5, 6, 7])
```

## 05 数据容器：str（字符串）

### 1、字符串的定义

- 字符串是字符的容器，可以容纳任意数量的字符。
- 字符串的下标索引同列表、元组一样
  - 从前到后，下标从0开始
  - 从后到前，下标从-1开始
- 字符串同样是不可修改的数据容器

代码示例：

```python
str1 = "aabbccdd"
print(str1[2]) # b
print(str1[-1]) # d
```

### 2、字符串的操作

- 查找特定字符串的下标索引值

语法：字符串.index(字符串)

代码示例：

```python
str1 = "aabbccdd"
print(str1.index("bbcc")) # 2
```

- 字符串的替换

语法：字符串.replace(字符串1,字符串2)

**注意**：这不是修改字符串本身，而是得到一个新字符串。

代码示例：

```python
str1 = "aabbccdd"
print(str1.replace("bbcc","ccdd")) # aaccdddd
```

- 字符串的分割

语法：字符串.split(分隔符字符串)

功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中。

**注意**：字符串本身不变，而是得到一个列表对象。

代码示例：

```python
str1 = "aa bb cc dd"
print(str1.split(" ")) # ['aa', 'bb', 'cc', 'dd']
```

- 字符串的规整操作
  - 语法：字符串.strip()，不含参数，去前后空格
  - 语法：字符串.strip(字符串)，去前后指定字符串（按照单个字符进行移除）

代码示例：

```python
str1 = "  aa bb cc dd  "
str2 = "121aa bb cc dd111"
print(str1.strip()) # aa bb cc dd
print(str2.strip("12")) # aa bb cc dd
```

- 统计字符串中某字符串出现的次数

代码示例：

```python
str1 = "aaabbbaaabbb"
print(str1.count("aa")) # 2
```

- 统计字符串的长度

代码示例：

```python
str1 = "aaabbbaaabbb"
print(len(str1)) # 12
```

- 字符串的遍历：while和for

## 06 数据容器（序列）的切片

### 1、什么是序列

- 序列是指：内容连续、有序，可使用下标索引的一类数据容器。
- 列表、元组、字符串均可以视为序列。

### 2、序列的切片操作

- 切片：从一个序列中取出一个子序列。
- 语法：序列[起始下标:结束下标:步长]
  - 起始下标表示从何处开始，留空则表示从头开始
  - 结束下标（不含）表示何处结束，留空则表示截取到结尾
  - 步长表示依次取元素的间隔，步长为1表示一个个取元素，步长2表示每隔一个取一个元素......
  - 步长为负数时，表示反向取元素，下标也要反向标记
- 此操作不会影响序列本身，而是会得到一个新序列

代码示例：

```python
# 对序列进行切片，从1开始，4结束，步长1
my_list = [0, 1, 2, 3, 4, 5, 6]
print(my_list[1:4:1]) # [1, 2, 3]

# 对元组进行切片，从头开始，到最后结束，步长1
my_touple = (0, 1, 2, 3, 4, 5, 6)
print(my_touple[::]) # (0, 1, 2, 3, 4, 5, 6)

# 对字符串进行切片，从头开始，到最后结束，步长2
my_str = "01234567"
print(my_str[::2]) # 0246

# 对字符串进行切片，从最后开始，到头结束，步长-1
my_str1 = "01234567"
print(my_str1[::-1]) # 76543210 等同于序列反转

# 对序列进行切片，从3开始，1结束，步长-1
my_list1 = [0, 1, 2, 3, 4, 5, 6]
print(my_list1[-4:-6:-1]) # [3, 2]
print(my_list1[3:1:-1]) # [3, 2]

# 对元组进行切片，从最后开始，到头结束，步长-2
my_touple1 = (0, 1, 2, 3, 4, 5, 6)
print(my_touple1[::-2]) # (6, 4, 2, 0)
```

## 07 数据容器：set（集合）

### 1、集合的定义格式

- 为什么要使用集合呢？
  - 列表可以修改，支持重复元素且有序
  - 元组、字符串不可修改，支持重复元素且有序
  - 而集合不支持元素重复，内部无序

基本语法：

```python
定义集合字面量
# {元素1,元素2,元素3,...}
# 定义集合变量
# {元素1,元素2,元素3,...}
# 定义空集合
# 变量名 = set()
```

代码示例：

```python
# 定义集合变量
my_set = {"I love", "myself", "myself"}
# 定义空集合
my_set_empty = set()

print(f"my_set的内容是：{my_set}，类型是{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，类型是{type(my_set_empty)}")

# my_set的内容是：{'I love' ,'myself'}，类型是<class 'set'>
# my_set_empty的内容是：set()，类型是<class 'set'>
```

### 2、集合的特点

集合不支持元素重复，内部无序

### 3、集合的常见操作

#### 修改

- 添加新元素
  - 语法：集合.add(元素)。将指定元素添加到集合内。
  - 结果：集合本身被修改，添加了新元素

代码示例：

```python
# 定义集合变量
my_set = {"I love", "myself", "myself"}
my_set.add("python")
print(my_set) # {'python', 'myself', 'I love'}
```

- 移除元素
  - 语法：集合.remove(元素)。将指定元素从集合中移除。
  - 结果：集合本身被修改，移除了元素

代码示例：

```python
# 定义集合变量
my_set = {"I love", "myself", "myself", 'python'}
my_set.remove("python")
print(my_set) # {'myself', 'I love'}
```

- 从集合中随机取出元素
  - 语法：集合.pop()，从集合中随机取出元素。
  - 结果：集合本身被修改，移除了元素，返回值是元素

代码示例：

```python
# 定义集合变量
# 定义集合变量
my_set = {"I love", "myself", "myself", 'python'}
element = my_set.pop()
print(element) # I love
print(my_set) # {'I love', 'myself'}
```

- 清空集合
  - 语法：集合.clear()
  - 结果：集合清空

代码示例：

```python
# 定义集合变量
my_set = {"I love", "myself", "myself", 'python'}
my_set.clear()
print(my_set) # set()
```

- 取两个集合的差集
  - 语法：集合1.difference(集合2)，取出集合1和集合2的差集（集合1有而集合2没有的）
  - 结果：得到1个新集合，集合1和集合2不变。

代码示例：

```python
# 定义集合变量
my_set1 = {"I love", "myself", "myself", 'python'}
my_set2 = {"I love",  'python'}
print(my_set1.difference(my_set2)) # {'myself'}
print(my_set1) # {'myself', 'I love', 'python'}
print(my_set2) # {'I love', 'python'}
```

- 消除两个集合的差集
  - 语法：集合1.difference_update(集合2)，在集合1中，删除和集合2相同的内容
  - 结果：集合1被修改，集合2不变

代码示例：

```python
# 定义集合变量
my_set1 = {"I love", "myself", "myself", 'python'}
my_set2 = {"I love",  'python'}
my_set1.difference_update(my_set2)
print(my_set1) # {'myself'}
print(my_set2) # {'I love', 'python'}
```

- 合并两个集合
  - 语法：集合1.union(集合2)
  - 结果：得到1个新集合，集合1和集合2不变

代码示例：

```python
# 定义集合变量
my_set1 = {"I love", "myself"}
my_set2 = {"I love",  'python'}
print(my_set1.union(my_set2)) # {'myself', 'I love', 'python'}
print(my_set1) # {'myself', 'I love'}
print(my_set2) # {'I love', 'python'}
```

- 统计集合元素数量
  - 语法：len(集合)

代码示例：

```python
# 定义集合变量
my_set1 = {"I love", "myself", "myself"}
print(len(my_set1)) # 2
```

#### 集合的遍历

集合不支持下标索引，所以不能使用while循环，但是可以用for循环。

代码示例：

```python
# 定义集合变量
my_set1 = {"I love", "myself", "myself"}
for x in my_set1:
    print(x)
    # I love
    # myself
```

## 08 数据容器：dict（字典、映射）

### 1、字典的定义

python中的字典可以通过key找到其所属的value值。

- 字典的定义使用发括号，字典中存储的元素是一对一对的。

语法如下：

```python
# 定义字典字面量
# {key:value,key:value,...}
# # 定义字典变量
# my_dict = {key:value,key:value,...}
# # 定义空字典
# my_dict = {}
# my_dict = dict()
```

代码示例：

```python
my_dict = {"王力宏":99,"我自己":100}
my_dict1 = dict()
my_dict2 = {}
print(f"my_dict的内容是：{my_dict},数据类型是：{type(my_dict)}")
print(f"my_dict1的内容是：{my_dict1},数据类型是：{type(my_dict1)}")
print(f"my_dict2的内容是：{my_dict1},数据类型是：{type(my_dict2)}")
# my_dict的内容是：{'王力宏': 99, '我自己': 100},数据类型是：<class 'dict'>
# my_dict1的内容是：{},数据类型是：<class 'dict'>
# my_dict2的内容是：{},数据类型是：<class 'dict'>
```

注意：字典中的key值是不可以重复的,重复添加会覆盖掉原有的数据。

- 字典数据的获取：
  - 字典同集合一样，不可以通过下标索引，但是可以通过key值找到对应的value值

代码示例：

```python
my_dict = {"王力宏":99,"我自己":100}
print(my_dict["王力宏"]) # 99
print(my_dict["我自己"]) # 100
```

- 字典的嵌套：key和value可以是任意类型数据（key不能为字典）

代码示例：

```python
stu_score_dict = {
    "王理红":{
        "语文":60,
        "数学":60,
        "英语":30
    },
    "周接论":{
        "语文":60,
        "数学":60,
        "英语":60
    },
    "我自己":{
        "语文":100,
        "数学":100,
        "英语":100
    }
}
score = stu_score_dict["我自己"]["语文"]
print(f"我自己的语文成绩是{score}") # 我自己的语文成绩是100
```

### 2、字典的相关操作

#### 新增元素何更新元素

代码示例：

```python
stu_score = {
    "周": 100,
    "王": 90,
    "李": 80
}
# 新增元素
stu_score["A"] = 60
# 修改元素
stu_score["周"] = 50
print(stu_score) # {'周': 50, '王': 90, '李': 80, 'A': 60}
```

#### 删除元素

- 语法：字典.pop(key)
- 结果：获得指定key的value，同时字典被修改，指定key的数据被删除

代码示例：

```python
stu_score = {
    "周": 100,
    "王": 90,
    "李": 80
}

print(stu_score.pop("周"))
print(stu_score) # {'王': 90, '李': 80, 'A': 60}
```

#### 清空字典

- 语法：字典.clear()

代码示例：

```python
stu_score = {
    "周": 100,
    "王": 90,
    "李": 80
}
stu_score.clear()
print(stu_score) # {}
```

#### 获取全部的key

- 语法：字典.keys()
- 结果：得到字典中全部的key

代码示例：

```python
stu_score = {
    "周": 100,
    "王": 90,
    "李": 80
}

print(stu_score.keys()) # dict_keys(['周', '王', '李'])
```

#### 遍历字典

依次通过key值遍历字典

代码示例：

```python
stu_score = {
    "周": 100,
    "王": 90,
    "李": 80
}
# 方式1：通过获取到全部key进行遍历
for key in stu_score.keys():
    print(stu_score[key])
    # 100
    # 90
    # 80
# 方式2：直接对字典进行for循环，每一次循环直接得到key
for key in stu_score:
    print(stu_score[key])
    # 100
    # 90
    # 80
```

#### 统计字典元素数目

代码示例：

```python
stu_score = {
    "周": 100,
    "王": 90,
    "李": 80
}
print(len(stu_score)) # 3
```

## 09 五类数据容器的对比总结

数据容器可以从以下视角进行简单分类：

- 是否支持下标索引
  - 支持：列表、元组、字符串 ——序列类型
  - 不支持：集合、字典 ——非序列类型
- 是否支持重复元素：
  - 支持：列表、元组、字符串 ——序列类型
  - 不支持：集合、字典 ——非序列类型
- 是否支持修改：
  - 支持：列表、集合、字典
  - 不支持：元组、字符串

<img src="\img\python从入门到进阶（一）\数据容器对比.jpg" alt="数据容器对比" title="数据容器对比">

## 10 数据容器的通用操作

### 1、遍历

- 五类数据容器都支持for循环遍历
- 列表、元组、字符串支持while循环遍历，集合和字典不支持while循环遍历，因为他们无法下标索引

### 2、数据容器的通用统计功能

- len(容器)
- max(容器)
- min(容器)

### 3、容器的通用转换操作

- list(容器)
- tuple(容器)
- str(容器)
- set(容器)

代码示例：
{% spoiler "点击显/隐内容" %}

```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_str = "aa"
my_set = {1, 2, 3}
my_dict = {"a": 1, "c": 2}
# 容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")
# 列表转列表的结果是：[1, 2, 3]
# 元组转列表的结果是：[1, 2, 3]
# 字符串转列表的结果是：['a', 'a']
# 集合转列表的结果是：[1, 2, 3]
# 字典转列表的结果是：['a', 'c']

# 容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}")
# 列表转元组的结果是：(1, 2, 3)
# 元组转元组的结果是：(1, 2, 3)
# 字符串转元组的结果是：('a', 'a')
# 集合转元组的结果是：(1, 2, 3)
# 字典转元组的结果是：('a', 'c')

# 容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串的结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}")
# 注意：以下都是字符串，带双引号的
# 列表转字符串的结果是：[1, 2, 3]
# 元组转字符串的结果是：(1, 2, 3)
# 字符串转字符串的结果是：aa
# 集合转字符串的结果是：{1, 2, 3}
# 字典转字符串的结果是：{'a': 1, 'c': 2}

# 容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是：{set(my_str)}")
print(f"集合转集合的结果是：{set(my_set)}")
print(f"字典转集合的结果是：{set(my_dict)}")
# 列表转集合的结果是：{1, 2, 3}
# 元组转集合的结果是：{1, 2, 3}
# 字符串转集合的结果是：{'a'}
# 集合转集合的结果是：{1, 2, 3}
# 字典转集合的结果是：{'a', 'c'}
```

{% endspoiler %}

### 4、容器通用排序功能

- 语法：sorted(容器,[reverse=True])
- 排序的结果是列表

代码示例：

```python
my_list = [3, 1, 2, 4, 2, 5]
my_tuple = (3, 1, 2, 4, 2, 5)
my_str = "ccssasasaaa"
my_set = {3, 1, 2, 4, 2, 5}
my_dict = {"c": 1, "a": 2}
print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")

# 列表对象的排序结果：[1, 2, 2, 3, 4, 5]
# 元组对象的排序结果：[1, 2, 2, 3, 4, 5]
# 字符串对象的排序结果：['a', 'a', 'a', 'a', 'a', 'c', 'c', 's', 's', 's', 's']
# 集合对象的排序结果：[1, 2, 3, 4, 5]
# 字典对象的排序结果：['a', 'c']
```

## 11 拓展：字符串大小的比较

字符串是按位比较，只要有一位大，那么整体就大。

# 第七章 Python函数进阶

## 01 函数多返回值

语法：return 返回值1,返回值2,返回值3,..

返回值类型不受限制。

代码示例：

```python
def test_return():
    return 1,2,3

x, y, z = test_return()
print(x, y, z) # 1 2 3
```

## 02 函数多种传参方式

函数传入参数种类：位置、关键字、不定长、缺省参数

### 位置参数

- 定义：调用函数时，根据函数定义的参数位置来传递参数。
- 注意：传递的参数和定义的参数的顺序和个数要一致。

### 关键字参数

- 定义：参数调用是通过“键=值”形式传递参数。
- 作用：可以让函数更加清晰】容易使用，同时也清除了参数的顺序需求。
- 注意：函数调用时，如果有位置参数，位置参数必须在关键字参数前面，但关键字参数不存在先后顺序。

代码示例:

```python
def user_info(name, age, gender):
    print(f"你的名字是{name}，年龄是{age}，性别是{gender}")

# 关键字传参
user_info(name="小明", age=11, gender="男")
# 不按固定顺序
user_info(age=11, gender="男", name="小明")
# 和位置参数混用
user_info("小明", gender="男", age=11)

# 你的名字是小明，年龄是11，性别是男
# 你的名字是小明，年龄是11，性别是男
# 你的名字是小明，年龄是11，性别是男
```

### 不定长参数

- 定义：不定长参数也叫可变参数，用于不确定调用的时候会传递多少个参数的场景。
- 不定长参数的类型：
  - 位置传递
    - 传进的所有参数会被变量收集合并为一个元组，这就是位置传递
  - 关键字传递
    - 参数是“键=值”的形式，所有参数合并为一个字典

位置传递——代码示例：

```python
def user_info(*arg):
    print(arg)

user_info('Tom')
user_info('Tom', 18)
# ('Tom',)
# ('Tom', 18)
```
注意：传进的所有参数都会被arg变量手机，它会根据传进参数的位置合并成一个元组，args是元组类型，这就是位置传递。

关键字传递——代码示例：

```python
def user_info(**kwargs):
    print(kwargs)

user_info(Tom=11, Jam=110)
# {'Tom': 11, 'Jam': 110}
```
注意：参数是“键=值”形式，所有的“键=值”的形式都会被kwargs接受，组成字典。

### 缺省参数

- 定义：缺省参数也叫做默认参数，用于定义函数，为参数提供默认值，调用函数时可以不传该默认参数的值。
- 注意：所有位置参数必须出现在默认参数之前，包括函数的定义和调用。
- 注意：函数调用时，如果为缺省参数传值则修改默认参数值，否则使用这个默认值。
- 默认参数必须放在最后。

代码示例：

```python
def user_info(name, age, gender = "男"):
    print(f"你的名字是{name}，年龄是{age}，性别是{gender}")

user_info("小明", 11, gender="女") # 你的名字是小明，年龄是11，性别是女
user_info(age=11, name="小明") # 你的名字是小明，年龄是11，性别是男
```

## 03 匿名函数

### 函数作为参数传递

函数本身也可作为参数传入到另一个函数中，这是一种**计算逻辑的传递**，而非数据的传递；任何逻辑都可以自行定义并作为函数传入。

代码示例：

```python
def test_func(compute):
    redult = compute(1, 2)
    print(f"compute参数的类型是{type(compute)}")
    print(f"计算结果是{redult}")

def compute(num1, num2):
    return num1 + num2

test_func(compute)

# compute参数的类型是<class 'function'>
# 计算结果是3
```

### lambda匿名函数

lambda关键字可以定义匿名函数（无名称），匿名函数只可以使用一次。

还需要注意的是，匿名函数的函数体只能写一行代码。

代码示例：

```python
def test_func(compute):
    redult = compute(1, 2)
    print(f"compute参数的类型是{type(compute)}")
    print(f"计算结果是{redult}")

test_func(lambda x, y: x+y)

# compute参数的类型是<class 'function'>
# 计算结果是3
```

# 第八章 Python文件操作

## 01 文件的编码

- 编码技术：将内容翻译成二进制，以及将二进制翻译回可识别内容。
- 计算机中有许多可用编码：UTF-8、GBK、Big5等，不同的编码将内容翻译成二进制也是不同的。
- 查看文件编码可以利用window自带的软件“记事本”，用记事本打开后在右下角就可以看到编码类型。
- UTF-8目前是全球通用的编码。

## 02 文件的读取

- 一般来说，文件可分为文本文件、视频文件、音频文件、图像文件、可执行文件等多种类别。

- 文件操作主要包括打开、关闭、读、写等操作

- 打开文件
  
  - open(name,mode,encoding)函数
  - name：要打开的文件名的字符串（可以包含文件所在的具体路径）
  - mode：设置打开文件的模式：只读、写入、追加等
  - encoding：编码格式（推荐UTF-8）**（只能用关键字参数指定）**

代码示例：

```python
# 打开文件
f = open('python.txt', 'r', encoding='UTF-8') # 不在当前文件的目录下要D:/文件名
print(type(f)) # <class '_io.TextIOWrapper'>
```

- 注意事项：此时的”f“是open函数的文件对象，对象是python中一种特殊的数据类型，拥有属性和方法，可以使用对象.属性或者对象.方法对其进行访问。

- mode常用的三种基础访问模式

| 模式  | 描述                                                         |
| --- | ---------------------------------------------------------- |
| r   | 以只读的方式打开文件，文件的指针会放在文件开头，这是默认的模式                            |
| w   | 打开一个文件只用于写入。如果文件已经存在，则打开文件并从头开始编辑，原有的内容会被删除；如果文件不存在，则创建新文件 |
| a   | 打开一个文件用于追加。如果文件已经存在，新的内容会被写入到已有的内容之后；如果文件不存在，则创建新的文件进行写入   |

- 读操作相关方法
  - 文件对象.read(num)
    - num表示要从文件中读取的数据的长度（单位是字符），如果没有传入num，则表示读取文件中所有的数据；**返回的是字符串**。
  - 文本对象.readlines()
    - 可以按照行的方式将文件中的内容进行一次性读取，**返回的是一个列表**。其中每一行的数据为一个元素。

代码示例：

```python
# 打开文件
f = open('python.txt', 'r', encoding='UTF-8') # 不在当前文件的目录下要D:/文件名
print(type(f)) # <class '_io.TextIOWrapper'>
# 读取操作
print(f"读取10个字节的结果：{f.read(10)}") # 读取10个字节的结果：1234567890
# 注意此时文件指针的位置为第一组1234567890
# 因此，下一次读取在第一组1234567890之后
print(f"read方法读取全部内容的结果是：{f.read()}")
print("-----------------------------------------------------------")
# read方法读取全部内容的结果是：1234567890
# 1234567890
lines = f.readlines()
print(f"读取文件的全部行，结果为：{lines}，类型为{type(lines)}")
# 读取文件的全部行，结果为：[]，类型为<class 'list'>
# 内容为空，因为已经被读取完了
```

- 文件对象.readline()
  - 一次读取一行内容，**返回的是字符串**

代码示例：

```python
# 打开文件
f = open('python.txt', 'r', encoding='UTF-8') # 不在当前文件的目录下要D:/文件名
line1 = f.readline()
line2 = f.readline()
print(f"第一行数据是{line1}") # 第一行数据是12345678901234567890
print(f"第二行数据是{line2}") # 第二行数据是1234567890
```

- for循环读取文件行

代码示例：

```python
f = open('python.txt', 'r', encoding='UTF-8') # 不在当前文件的目录下要D:/文件名
for line in f:
    print(f"每一行数据为：{line}")
```

- 文件的关闭
  - 文件对象.close()
  - 如果不关闭文件，那这个文件将一直被python文件所占用

代码示例：

```python
f = open('python.txt', 'r', encoding='UTF-8') # 不在当前文件的目录下要D:/文件名
f.close()
```

- with open语法

代码示例：

```python
with open("python.txt", "r") as f:
    print(f.readlines()) # ['12345678901234567890\n', '1234567890']
# 通过该操作可以自动关闭文件
```

## 03 文件的写入

- 写入操作的三个步骤：
  - 1、open()打开文件
  - 2、write()写入内容
  - 3、flush()内容刷新

只调用write的时候内容并未真正写入到文件中，而是存储在缓冲区中，需要调用flush，内容才会真正写入文件。

代码示例：

```python
f = open("python.txt", "w")
f.write("helloworld")
f.flush()
f.close()
# 此时文件中只有helloworld，不会有其他内容，因为“w”模式会将文件内容全部清空
```

- w模式会在第一次写入数据的时候清空文件原有内容。
- 注意：其实close()是内置flush功能的。

## 04 文件的追加

代码示例：

```python
f = open("text.txt", "a")
f.write("\nhelloworld111")
f.flush()
f.close()
```

## 05 文件操作综合案例

<img src="\img\python从入门到进阶（一）\文件操作综合案例.jpg" alt="文件操作综合案例" title="文件操作综合案例">
<img src="\img\python从入门到进阶（一）\文件操作综合案例1.jpg" alt="文件操作综合案例" title="文件操作综合案例">
代码示例：
```python
f = open("text.txt", "r", encoding="UTF-8")
g = open("text.txt.bak", "w", encoding="UTF-8")
for line in f:
    line = line.strip("\n")
    words = line.split(",")
    if words.count("测试") == 0:
        g.write(line)
        g.write("\n")
f.close()
g.close()
```

# 第九章 Python异常、模块与包

## 01 了解异常

- 什么是异常？
- 当检测到一个错误时，Python解释器就无法继续执行了，反而会出现了一些错误的指示，这就是所谓的**异常**，也就额是BUG

## 02 异常的捕获方法

- 异常处理(捕获异常)：在力所能及的范围内，对可能出现的bug进行提前准备、提前处理。
- 捕获异常的作用在于：提前假设某处会出现异常，做好提前准备，当真的出现异常的时候，可以有后续手段。

基本语法：

```python
try:
    可能发生错误的代码
except:
    如果出现错误执行的代码
```

快速入门，代码示例：

```python
try:
    f = open("linux.txt", 'r')
except:
    f = open('linux.txt', 'w')
```

- 捕获指定异常

基本语法：

```python
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')
```

以上代码指定捕获NameError异常。

```python
try:
    1/0
except NameError as e:
    print('name变量名称未定义错误')
```

而在以上代码中，1/0并不属于NameError异常，因此不会被捕获，编译时直接报错。

```python
try:
    name
except NameError as e:
    print('name变量名称未定义错误')
    print(e) # e存储的是异常信息
```

as后面的变量用于存储异常信息。

- 捕获多个异常
  - 当捕获多个异常时，可以把要补货的异常类型的名字放到except之后，并使用元组的方式进行书写。

代码示例：

```python
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('ZeroDivision错误...')
```

- 捕获所有异常(和第一种方法效果一致)

代码示例：

```python
try:
    print(1/0)
except Exception as e:
    print('出现异常了')
```

- 异常else：else表示的是如果没有异常要执行的代码。

```python
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('没有异常时执行的代码')
```

- 异常的finally：无论是否异常都要执行的代码

```python
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('没有异常时执行的代码')
finally:
    print('无论异不异常都要执行的代码')
```

## 03 异常的传递

异常是具有传递性的。

代码示例：

```python
def fun1():
    print("fun1开始执行")
    num = 1/0
    print("fun1结束执行")

def fun2():
    print("fun2开始执行")
    fun1()
    print("fun2结束执行")

def main():
    try:
        fun2()
    except Exception as e:
        print(f"出现异常了，异常信息是{e}")

main()

# fun2开始执行
# fun1开始执行
# 出现异常了，异常信息是division by zero
```

## 04 Python模块

### 模块的导入

- Python模块是一个Python文件，以.py结尾，
- 模块能定义函数，类和变量，模块中也包含了可执行的代码。
- 模块的作用：python中有很多不同的模块，每一个模块都可以帮助我们快速实现一些功能，一个模块就是一个工具包。

代码示例：
```python
# 模块的导入语法
[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
# 常见组合
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名
```

- 按住ctrl点击模块则可以看到模块代码

- 案例：导入time模块

代码示例（不同导入方式）：
```python
# 使用import导入time模块，使用该模块的全部功能
import time # 导入python内置的time模块，time.py这个文件
print("你好")
time.sleep(5) # . 确定层级关系
print("我好")
```

```python
# 导入时间模块中的sleep方法
from time import sleep # 导入python内置的time模块中的sleep方法
print("你好")
sleep(5) # 这样直接使用sleep函数
print("我好")
```

```python
# 使用*导入time模块的全部功能
from time import *
print("你好")
sleep(5) # 这样直接使用sleep函数
print("我好")
```

```python
# 使用as定义别名
from time import sleep as tt
import time as t
print("你好")
t.sleep(5)
tt(5)
print("我好")
```

### 自定义模块
代码示例：
```python
# my_module1.py
def test(a, b):
    return a+b

# test.py
import my_module1
print(my_module1.test(1, 2)) # 3
```

- 注意：当导入多个模块的时候，且模块内有同名的功能，当调用这个同名功能时，调用到的是后面导入的模块的功能。
<br>
---
- __main__变量的使用
    - 在定义的模块中需要做模块功能测试时可以使用main变量进行测试，在使用模块的时候不会运行该测试代码。

代码示例：
```python
# my_module1.py
def test(a, b):
    return a+b

if __name__ == '__main__':
    print(test(1, 2))
# 在模块中
# 3

# test.py
import my_module1
# 不会输出3
```
这样就满足了在模块的代码文件中可以运行测试函数，又满足了我们在外部导入时不会允许模块中的测试代码。

- __all__变量
    - 当模块文件中有all变量的时候，当使用from xxx import * 导入时只能导入这个列表中的元素。

代码示例：
```python
# my_module1.py
__all__ = ['test_A']

def test_A(a, b):
    return a+b

def test_B(a, b):
    return a-b

# test.py
from my_module1 import *
print(test_A(1, 2))
# print(test_B(1, 3)) 会报错
# 若还是要使用test_B则需要手动导入
# from my_module1 import test_B
```

## 05 Python包
### 自定义包
- python的包就是一个文件夹，在该文件夹下包含了一个__init__.py文件，该文件夹可用于包含多个模块文件；从逻辑上看，包的本质依然是模块。
- 有__init__.py文件就是python包，没有就是普通的文件夹
- 包的作用：当我们的模块文件越来越多时，包可以帮助我们管理这些模块，
- 步骤如下：
    - 1、新建'my_package'，包内部会自动创建__init__.py文件，这个文件控制着包的导入行为
    - 2、新建包内模块

### 导入包
- 方式一：import 包名.模块名<br>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;包名.模块名.目标

代码示例：
```python
# my_module1.py
def info_print1():
    print("我是模块1的功能代码")

# my_module2.py
def info_print2():
    print("我是模块2的功能代码")

# test.py
import my_package.my_module1
import my_package.my_module2

my_package.my_module1.info_print1()
my_package.my_module2.info_print2()
```

- 方式二：from 包名 import 模块名

代码示例：
```python
# test.py
from my_package import my_module1
from my_package import my_module2

my_module1.info_print1()
my_module2.info_print2()
```

- 方式三：from 包名.模块名 import 函数名

代码示例：
```python
# test.py
from my_package.my_module1 import info_print1
from my_package.my_module2 import info_print2

info_print1()
info_print2()
```

- 方式四：
- 在'__init__.py'中添加'__all__ = []'，控制允许导入的模块列表
- from 包名 import *
- **注意：all只能用来控制import * .**

代码示例：
```python
# test.py
from my_package import *

my_module1.info_print1()
# my_module2.info_print2() 用不了

# __init__.py
__all__ = ['my_module1']
```

### 安装第三方包
在python程序的生态中，有许多第三方包（非python官方），可以极大帮助我们提高开发效率。

在命令提示符中输入pip install 包名，称即可通过网络快速安装第三方包

使用国内网站进行安装：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称

可以直接在pycharm中安装包

1、点击右下角-解释器设置
<img src="\img\python从入门到进阶（一）\pycharm安装第三方包1.png" alt="pycharm安装第三方包1" title="pycharm安装第三方包1">
2、点击加号，搜索包并安装
<img src="\img\python从入门到进阶（一）\pycharm安装第三方包2.png" alt="pycharm安装第三方包2" title="pycharm安装第三方包2">
3、如果安装速度较慢，可以把该选项勾上，写入-i https://pypi.tuna.tsinghua.edu.cn/simple
<img src="\img\python从入门到进阶（一）\pycharm安装第三方包3.png" alt="pycharm安装第三方包3" title="pycharm安装第三方包3">

## 06 Python异常-模块-包-综合案例讲解

<img src="\img\python从入门到进阶（一）\第九章综合案例.jpg" alt="第九章综合案例" title="第九章综合案例">

代码示例：
{% spoiler "点击显/隐内容" %}
```python
# bill.txt文件中原有的内容为 1+1=2
"""
字符串相关工具模块
str_utils.py
"""
def str_reverse(s):
    """
    将字符串完成反转
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s, x, y):
    """
    按照给的的下标完成给定字符串的切片操作
    :param s: 即将切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下表
    :return: 切片完成的字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("123456"))
    print(substr("123456", 1, 3))
# 654321
# 23

"""
文件处理相关工具模块
file_util.py
"""
def print_file_info(file_name):
    """
    将给定路径的文件内容输出到控制台
    :param file_name: 文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print("文件的内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常，原因时：{e}")
    else:
        if f:
            f.close()

def append_to_file(file_name, data):
    """
    将指定的数据追加到指定的文件中
    :param file_name: 指定的文件
    :param data: 指定的数据
    :return: None
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write("\n")
    f.write(data)
    f.close()

if __name__ == '__main__':
    print_file_info("bill.txt")
    append_to_file("bill.txt", '10086')

# test.py
import my_utils.str_utils
from my_utils import file_utils

print(my_utils.str_utils.str_reverse("黑马程序员"))
print(my_utils.str_utils.substr("itheima", 0, 4))
# 员序程马黑
# ithe
file_utils.print_file_info("bill.txt")
file_utils.append_to_file("bill.txt", "2+2=4")
file_utils.print_file_info("bill.txt")
# 文件的内容如下：
# 1+1=2
# 文件的内容如下：
# 1+1=2
# 2+2=4
```

{% endspoiler %}

# 第十章 python基础综合案例
## 01 案例介绍
<img src="\img\python从入门到进阶（一）\第十章综合案例开发图1.jpg" alt="第十章综合案例开发图1" title="第十章综合案例开发图1">
<img src="\img\python从入门到进阶（一）\第十章综合案例开发图2.jpg" alt="第十章综合案例开发图2" title="第十章综合案例开发图2">
<img src="\img\python从入门到进阶（一）\第十章综合案例开发图3.jpg" alt="第十章综合案例开发图3" title="第十章综合案例开发图3">

## 02 json数据格式
### 什么是json
- JSON是一种轻量级的数据交互格式，可以按照JSON指定的格式去组织和封装数据
- JSON本质上是一个带有特定格式的字符串
- 主要功能：JSON就是一种在各个编程语言中流通的数据格式，负责**不同编程语言中的数据传递和交互**，类似于
    - 国际通用语言——英语
    - 中国56个名族不同地区通用语言——普通话
- <font color=#FF000 ><font size=3 >**简言之，JSON就是用于不同编程语言中的数据中转的一种数据格式**</font></font>

### 使用json进行数据转化
- json数据的格式可以是字典，也可以是内嵌字典的列表。

```python
# json的数据格式可以是
{"name":"admin","age":18}
# json的数据格式还可以是
[{"name":"admin","age":18}, {"name":"kxr","age":18}]
```

所谓的json就是把python中的字典转化为字符串，或者把内嵌字典的列表转化为字符串。

- python数据与json数据的相互转化
    - json字符串只能内单引号外双引号

代码示例：
```python
# 使用内置python模块json
import json
# 准备列表
data1 = [{"name":"小儿", "age":11},{"name":"大二","age":12}]
# 转化为json
json_str = json.dumps(data1, ensure_ascii=False) # 不写中文就不用写第二个参数
# 内容以及变量类型打印
print(type(json_str))
print(json_str)
# <class 'str'>
# [{"name": "小儿", "age": 11}, {"name": "大二", "age": 12}]

# 准备字典
data2 = {"name":"kxr", "age":12}
# 转化为json
json_dict = json.dumps(data2)
# 内容以及变量类型打印
print(type(json_dict))
print(json_dict)
# <class 'str'>
# {"name": "kxr", "age": 12}

# 将json字符串转换为python列表
s = '[{"name": "小儿", "age": 11}, {"name": "大二", "age": 12}]'
python_list = json.loads(s)
print(type(python_list))
print(python_list)
# <class 'list'>
# [{'name': '小儿', 'age': 11}, {'name': '大二', 'age': 12}]
# 转换为python字典同理
# 转换为python字典同理
```

## 03 pyecharts模块介绍
- 如果要做出数据可视化效果图，可以借助pyecharts模块来完成。
- pyecharts是由百度团队开发的，因此有着中文文档可供查询
    - 官方网站“pyecharts.org”
    - 官方示例“gallery.pyecharts.org”

- 安装pyecharts第三方包：“pip install pyecharts”

## 04 pyecharts快速入门
### 构建基础折线图
代码示例：
```python
# 导入line功能构建折线图对象
from pyecharts.charts import Line
# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
line.add_yaxis("GDP", [30,20,10])
# 通过render代码，将代码生成为图像
line.render()
```
折线图如下：
<img src="\img\python从入门到进阶（一）\10-折线图.png" alt="10-折线图" title="10-折线图">

### 使用全局配置项设置属性
- pyecharts模块中有很多配置选项，常用的有两个类别的选项
    - 全局配置选项
    - 系列配置选项

- set_global_opts方法
    - 这里的全局配置选项可以通过该方法进行配置，相应的选项和功能如下：
    - TitleOpts：标题配置项
    - LegendOpts：图例配置项
    - ToolboxOpts：工具箱配置项
    - VisualMapOpts：视觉映射配置项
    - TooltipOpts：提示框配置项
    - DataZoomOpts：区域缩放配置项

代码示例：
```python
# 导入line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
line.add_yaxis("GDP", [30,20,10])
# 设置全局配置项
line.set_global_opts(
    # 居中显示，距离底部有1%的距离
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    # 控制图例，选择是否展示
    legend_opts=LegendOpts(is_show=True),
    # 工具箱，选择是否展示
    toolbox_opts=ToolboxOpts(is_show=True),
    # 视觉映射，选择是否展示
    visualmap_opts=VisualMapOpts(is_show=True)
)
# 通过render代码，将代码生成为图像
line.render()

```
折线图如下：
<img src="\img\python从入门到进阶（一）\10-GDP展示.png" alt="10-GDP展示" title="10-GDP展示">

- <font color=#FF000 ><font size=5 >**在官网中可以找到其他全局配置项。**</font></font>

## 05 数据处理、创建折线图
通过json模块对数据进行处理。

代码示例：
{% spoiler "点击显/隐内容" %}
```python
"""
演示可视化需求1：折线图开发
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts
# 处理数据 依次是美国、日本、印度
f_us = open("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
f_jp = open("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/折线图数据/日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()
f_id = open("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/折线图数据/印度.txt", "r", encoding="UTF-8")
id_data = f_id.read()
# 去掉不符合JSON规范的开头和结尾
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
jp_data = jp_data[:-2]
id_data = id_data.replace("jsonp_1629350745930_63180(", "")
id_data = id_data[:-2]
# JOSN转Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
id_dict = json.loads(id_data)
# 取出trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
id_trend_data = id_dict['data'][0]['trend']
# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
id_x_data = id_trend_data['updateDate'][:314]
# 获取确诊数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
id_y_data = id_trend_data['list'][0]['data'][:314]
# 生成图表
line = Line() # 构建折线图对象
line.add_xaxis(us_x_data) # x轴是共用的
line.add_yaxis("美国确诊人数",us_y_data, label_opts=LabelOpts(is_show=False)) # 添加美国y轴数据
line.add_yaxis("日本确诊人数",jp_y_data, label_opts=LabelOpts(is_show=False)) # 日本
line.add_yaxis("印度确诊人数",id_y_data, label_opts=LabelOpts(is_show=False)) # 印度
# 设置全局配置项
line.set_global_opts(
    # 居中显示，距离底部有1%的距离
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)
line.render() # 使用render方法生成图表
# 关闭文件
f_us.close()
f_jp.close()
f_id.close()
```
{% endspoiler %}

折线图如下：
<img src="\img\python从入门到进阶（一）\10-确诊人数折线图.png" alt="10-确诊人数折线图" title="10-确诊人数折线图">

# 第十一章 python基础综合案例——数据可视化——地图可视化
## 01 基础地图使用
使用pyecharts进行地图构建。

代码示例：
{% spoiler "点击显/隐内容" %}
```python
"""
演示地图可视化的基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()
# 准备数据 使用列表存储，列表中是元组
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499),
]
# 添加数据
map.add("测试地图", data, "china") # 名称、数据、地图类型
# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts( # 设置地图视觉指示器
        is_show=True, 
        is_piecewise=True, # 开启手动校准范围
        pieces=[ # 手动指定分段 3段
            {"min":1, "max":9, "label":"1-9人", "color":"#CCFFFF"},
            {"min":10, "max":99, "label":"10-99人", "color":"#FFFF99"},
            {"min":99, "max":499, "label":"99-499人", "color":"#FF9966"},
            {"min":499, "max":999, "label":"499-999人", "color":"#FF6666"},
            {"min":1000, "max":9999, "label":"1000-9999人", "color":"#CC3333"},
            {"min":10000, "label":"10000以上", "color":"#990033"}
        ]
    )
)
# 绘图
map.render()
```
{% endspoiler %}

地图示例：
<img src="\img\python从入门到进阶（一）\11-可视化地图1.png" alt="可视化地图1" title="可视化地图1">

## 02 疫情地图——国内疫情地图
代码示例：
{% spoiler "点击显/隐内容" %}
```python
"""
演示全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取数据文件
f = open("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()
# 取到各省份数据
# 将json转换为Python字典
data_dict = json.loads(data)
# 从字典中取出省份数据
province_data_list = data_dict["areaTree"][0]["children"]
# 从省份数据取到省份名称和数据组装成元组，再将所有省份封装到列表内
data_list = [] # 绘图时用到的数据列表
for province_data in province_data_list:
    province_name = province_data["name"] # 省份名称
    province_confirm = province_data["total"]["confirm"] # 确诊人数
    if province_name == '新疆维吾尔自治区' or province_name == '内蒙古自治区' or province_name == '宁夏回族自治区' \
            or province_name == '西藏自治区' or province_name == '广西壮族自治区' or province_name == '北京市' \
            or province_name == '天津市' or province_name == '上海市' or province_name == '重庆市':
        data_list.append((province_name, province_confirm))
    else:
        data_list.append((province_name+'省', province_confirm))
# 创建地图对象
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list, "china")
# 添加全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True, # 是否显示
        is_piecewise=True, # 是否分段
        pieces=[
            {"min":1, "max":99, "label":"1-99人确诊", "color":"#CCFFFF"},
            {"min":100, "max":999, "label":"100-999人确诊", "color":"#FFFF99"},
            {"min":1000, "max":4999, "label":"1000-9999人确诊", "color":"#FF9966"},
            {"min":5000, "max":9999, "label":"5000-9999人确诊", "color":"#FF6666"},
            {"min":10000, "max":99999, "label":"10000-99999人确诊", "color":"#CC3333"},
            {"min":100000, "label":"超过100000人确诊", "color":"#990033"}
        ]
    )
)
# 绘图
map.render("全国疫情地图.html")
```
{% endspoiler %}

地图示例：
<img src="\img\python从入门到进阶（一）\11-可视化地图2.png" alt="可视化地图2" title="可视化地图2">

## 03 疫情地图——省级疫情地图
代码示例：
{% spoiler "点击显/隐内容" %}
```python
"""
演示河南省疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取数据文件
f = open("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()
# 取到各省份数据
# 将json转换为Python字典
data_dict = json.loads(data)
# 从字典中取出河南省各个城市的数据
cities_data = data_dict["areaTree"][0]["children"][3]["children"]
# 从数据取到各个城市名称和数据组装成元组，再将所有数据封装到列表内
data_list = [] # 绘图时用到的数据列表
for city_data in cities_data:
    city_name = city_data["name"]  # 城市名称
    city_confirm = city_data["total"]["confirm"] # 确诊人数
    data_list.append((city_name+ "市", city_confirm))
# 手动添加济源市的数据
data_list.append(("济源市", 5))
# 创建地图对象
map = Map()
# 添加数据
map.add("河南省疫情分布", data_list, "河南")
# 添加全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True, # 是否显示
        is_piecewise=True, # 是否分段
        pieces=[
            {"min":1, "max":99, "label":"1-99人确诊", "color":"#CCFFFF"},
            {"min":100, "max":999, "label":"100-999人确诊", "color":"#FFFF99"},
            {"min":1000, "max":4999, "label":"1000-9999人确诊", "color":"#FF9966"},
            {"min":5000, "max":9999, "label":"5000-9999人确诊", "color":"#FF6666"},
            {"min":10000, "max":99999, "label":"10000-99999人确诊", "color":"#CC3333"},
            {"min":100000, "label":"超过100000人确诊", "color":"#990033"}
        ]
    )
)
# 绘图
map.render("河南省疫情地图.html")
```
{% endspoiler %}

地图示例：
<img src="\img\python从入门到进阶（一）\11-可视化地图3.png" alt="可视化地图3" title="可视化地图3">

# 第十二章 python基础综合案例——数据可视化——动态柱状图
## 01 基础柱状图构建
通过Bar构建基础柱状图

代码示例：
```python
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts # 导包以对坐标轴进行更多配置
# 使用Bar构建基础柱状图
bar = Bar()
# 添加数据
bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right")) # 使数据位于右侧，该功能非必须
# 反转xy轴
bar.reversal_axis()
# 绘图
bar.render("基础柱状图.html")
```

地图示例：
<img src="\img\python从入门到进阶（一）\12-柱状图图1.png" alt="12-柱状图1" title="12-柱状图1">

## 02 基础时间柱状图
- 使用TimeLine()创建时间线


代码示例：
```python
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
# 给时间线设置主题 导相关包
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right")) # 使数据位于右侧，该功能非必须
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 30, 20], label_opts=LabelOpts(position="right")) # 使数据位于右侧，该功能非必须
bar2.reversal_axis()

# 创建时间线对象
timeline = Timeline({"theme":ThemeType.LIGHT}) # 设置主题
# timeline对象添加bar柱状图
timeline.add(bar1, "2021年GDP")
timeline.add(bar2, "2022年GDP")
# 设置自动播放
timeline.add_schema(
    play_interval=1000, # 自动播放的时间间隔，单位：毫秒
    is_timeline_show=True, # 是否在自动播放的时候展示时间线
    is_auto_play=True, # 是否自动播放
    is_loop_play=True # 是否循环自动播放
)
# 通过时间线绘图
timeline.render("基础柱状图.html")
```

地图示例：
<img src="\img\python从入门到进阶（一）\12-柱状图图2.png" alt="12-柱状图2" title="12-柱状图2">

## 03 GDP动态柱状图绘制
### 列表的sort方法
> 列表的sort方法
>>在前面学习的sorted函数可以对数据容器进行排序；但是，在本案例中需要对列表进行排序并指定排序规则，sorted函数是无法完成的，为此需要补充学习列表的sort方法。

- 列表.sort(key=选择排序依据的函数，reverse=True|False)
    - 参数key，是要求传入一个函数。表示1将列表中的每一个元素都传入函数中，返回排序的依据
    - 参数reverse，是否反转排序结果，True表示降序，False表示升序。

代码示例：
```python
# 准备列表
my_list = [["a",33],["b",55],["c",11]]
# 排序函数
def choose_sort_key(element):
    return element[1]
my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)
# [['b', 55], ['a', 33], ['c', 11]]
```
还可以使用匿名函数
```python
# 准备列表
my_list = [["a",33],["b",55],["c",11]]

my_list.sort(key=lambda element:element[1], reverse=True)
print(my_list)
# [['b', 55], ['a', 33], ['c', 11]]
```

### 绘制动态柱状图
代码示例：
{% spoiler "点击显/隐内容" %}
```python
"""
GDP动态柱状图开发
"""
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 读取数据
f = open("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换为字典存储
# {年份：[[国家，GDP],[],...],[],[],...}
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])  # 年份
    country = line.split(",")[1]    # 国家
    gdp = float(line.split(",")[2]) # GDP数据
    # 判断字典中是否有指定的key使用异常捕获
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country,gdp])
# 排序年份
sorted_year = sorted(data_dict.keys()) # 获取所有key值并排序

timeline = Timeline({"theme":ThemeType.LIGHT})

for year in sorted_year:
    # 列表排序
    data_dict[year].sort(key=lambda element:element[1],reverse=True)
    # 取出前八个国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for contry_gdp in year_data:
        x_data.append(contry_gdp[0]) # x轴添加国家
        y_data.append(contry_gdp[1]/100000000) # y轴添加GDP数据
    x_data.reverse()
    y_data.reverse()
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP()亿", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    # 设置每一年图标的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前八GDP数据")
    )
    timeline.add(bar, str(year))
# 设置自动播放
timeline.add_schema(
    play_interval=1000, # 自动播放的时间间隔，单位：毫秒
    is_timeline_show=True, # 是否在自动播放的时候展示时间线
    is_auto_play=True, # 是否自动播放
    is_loop_play=True # 是否循环自动播放
)
timeline.render("1960-2019年全球GDP国家前八名.html")
```
{% endspoiler %}

动态柱状图示例：
<img src="\img\python从入门到进阶（一）\12-柱状图图3.png" alt="12-柱状图3" title="12-柱状图3">