# python从入门到进阶

python从入门到进阶。
python简洁高效、应用场景丰富。

<!-- more -->

```mermaid
graph LR
python从入门到进阶--> python语言基础入门
python从入门到进阶--> python语言高阶加强
python从入门到进阶--> 大数据分析PySpark
```

```mermaid
graph LR
python从入门到进阶--> python语言基础入门
python从入门到进阶--> python语言高阶加强
python从入门到进阶--> 大数据分析PySpark
```
# 第一章 你好python
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
python中常用的有**6**种值（数据）类型
<table>
    <tr>
        <th>类型</th><th>描述</th><th>说明</th>
    </tr>
    <tr>
        <td rowspan="4">数字number</td><td>整数int</td><td>如：10，-10</td>
    </tr>
    <tr>
        <td>浮点数float</td><td>如：13.14</td>
    </tr>
    <tr>
        <td>复数complex</td><td>如：4+3j</td>
    </tr>
    <tr>
        <th>布尔bool</th><th>true 和 false</th>
    </tr>
    <tr>
        <th>字符串string</th><th>描述文本的一种数据类型（需要加上双引号或者单引号）</th><th>字符串由任意数量的字符组成</th>
    </tr>
    <tr>
        <th>列表list</th><th>有序的可变序列</th><th>python中使用最频繁的数据类型，可有序记录一堆数据</th>
    </tr>
    <tr>
        <th>元组tuple</th><th>有序的不可变序列</th><th>可有序记录一堆不可变的python数据集合</th>
    </tr>
    <tr>
        <th>集合set</th><th>无序不重复集合</th><th>可无序记录一堆不重复的python数据集合</th>
    </tr>
    <tr>
        <th>字典dictionary</th><th>无序key-value集合</th><th>可无序记录一堆key-value型的python数据集合</th>
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
>> 在程序运行时，能存储计算结果或者能表示值的抽象概念。

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
>>- 从文件中读取的数字，默认是字符串，需要转换为数字类型
>>- 后续学习的input语句，默认是字符串，若需要数字也需要转换
>>- 将数字转换成字符串用以写到外部系统
>>- 等等

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
>> 用户在编程中所使用的一系列名字，用于给变量、类、方法等命名。

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
如果有多个字符串字面量，可以通过+号拼接为一个字符串
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

|格式符号|转化|
|:--:|:--:|
|%s|将内容转化为字符串放入占位位置|
|%d|将内容转化为整数放入占位位置|
|%f|将内容转化为浮点型放入占位位置|

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