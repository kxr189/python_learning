---
title: 【笔记】python从入门到进阶（二）—— python语言高阶加强
tags: [编程语言学习,python]
categories: [python,编程语言学习]
---

python从入门到进阶。
python简洁高效、应用场景丰富。

<!-- more -->

# 第一章 面向对象

## 01 初始对象
使用对象组织数据：
&emsp;&emsp;在程序中是可以做到和生活中那样，设计表格、生产表格、填写表格的组织形式的。
1. 在程序中设计表格，我们称之为：<font color=#FF0000 ><font size=3 >**设计类（class）**</font></font>

代码示例：
```python
class student:
    name = None # 记录学生姓名
```
2. 在程序中打印生产表格，我们称之为：<font color=#FF0000 ><font size=3 >**创建对象**</font></font>

代码示例：
```python
# 基于类创建对象
stu_1 = student()
stu_2 = student()
```
3. 在程序中填写表格，我们称之为：<font color=#FF0000 ><font size=3 >**对象属性赋值**</font></font>

代码示例：
```python
stu_1.name = "周杰轮" # 为学生1对象赋予名称属性值
stu_2.name = "林君姐" # 为学生2对象赋予名称属性值
```

整体演示：
```python
# 1、设计一个类（类比生活中：设计一张登记表）
class Student:
    name = None         # 记录学生姓名
    gender = None       # 记录学生性别
    nationality = None  # 记录学生国籍
    native_place = None # 记录学生国籍
    age = None          # 记录学生年龄
# 2、创建一个对象（类比生活中：打印一张登记表）
Stu_1 = Student()
# 3、对象属性进行赋值（类比生活中：填写表单）
Stu_1.name = "kxr"
Stu_1.gender = "男"
Stu_1.nationality = "China"
Stu_1.native_place = "广东省"
Stu_1.age = 22
# 4、获取对象中记录的信息
print(Stu_1.name)
print(Stu_1.gender)
print(Stu_1.nationality)
print(Stu_1.native_place)
print(Stu_1.age)
# kxr
# 男
# China
# 广东省
# 22
```

## 02 类的成员方法
### 类的定义和使用语法
类的使用语法：
> class 类名称：    # class是关键字
>       类的属性    # 类的属性，即定义在类中的变量（成员变量）
>       类的行为    # 类的行为，即定义在类中的函数（成员方法）

创建类对象的语法
> 对象 = 类名称（）

那么什么是类的行为（方法）？<br>
其实就是一个函数，可以通过对象去调用这个函数。<br>
**定义在类内部的函数就叫做方法。**

### 成员方法的使用
成员方法的定义语法：<br>
&emsp;&emsp;在类中，定义成员方法和定义函数基本一致，但仍有细微区别，定义语法如下：
```python
def 方法名(self, 形参1, 形参2, ...):
    方法体
```
可以看到，在方法定义的参数列表中，有一个：self关键字，self关键字是成员方法定义的时候必须填写的。

### self关键字的作用
1. 用来表示类自身的意思
2. 当我们使用类对象调用时，self会自动被Python传入
3. 在方法内部，想要访问类的成员对象就必须使用self

注意：self关键字，尽管在参数列表中，但是传参时可以忽略它。

代码示例：
```python
class student:
    name = None

    def say_hi(self):
        print(f"大家好，我是{self.name}")
    def say_hi2(self, msg):
        print(f"大家好，我是{self.name},{msg}")

stu = student()
stu.name = "kxr"
stu.say_hi()                #大家好，我是kxr
stu.say_hi2("我是傻逼")      #大家好，我是kxr,我是傻逼

stu2 = student()
stu2.name = "wbd"
stu2.say_hi() # 大家好，我是wbd
```

## 03 类和对象
> 本节要点
>> 1. 掌握使用现实世界事物的思想
>> 2. 掌握类和对象的关系
>> 3. 理解什么是面向对象

现实世界的事物和类：
&emsp;&emsp;现实世界的事物可以归纳出两个特征：<font color=#FF0000 ><font size=3 >**属性、行为**</font></font>
&emsp;&emsp;类也有属性和行为；使用程序中的类可以完美的描述现实世界的事物。

基于类创建对象的语法：对象名 = 类名称（）

为什么非要创建对象才能使用呢？
>类只是一种程序内的“设计图纸”，需要基于图纸生产实体（对象），才能正常工作，这种套路就称之为<font color=#FF0000 ><font size=5 >**面向对象编程**</font></font>：设计类，基于类创建对象，由对象做具体的工作。

举例：
>在现实世界中，要生产一种产品，首先要有该产品的“设计图纸”，然后才能根据该图纸来生产出“实物”出来。

代码示例：
```python
# 闹钟的设计图纸
class clock:
    id = None       # 序列号
    price = None    # 零售价

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000) # 2000是频率 3000是持续时间

# 根据图纸来生产实物
clock1 = clock()
clock1.id = "001"
clock1.price = 99.99
print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
clock1.ring()
```
<font color=#FF0000 ><font size=5 >**这个程序会发出声音！！！！**</font></font>

## 04 构造方法
属性（成员变量）的赋值：
&emsp;&emsp;前面演示的代码都是依次为对象的属性赋值，略显繁琐，还有更高效的方法，可以使用**构造方法**。

- 构造方法
    - Python类可以使用：__init__()方法，称之为构造方法
    可以实现：
    - 在创建类对象（构造类）的时候，会**自动执行**
    - 在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用

代码示例：
```python
class student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("student类创建了一个类对象")

stu = student("kxr", 11, "121012002020")
print(stu.name)
print(stu.age)
print(stu.tel)
# student类创建了一个类对象
# kxr
# 11
# 121012002020
```

## 05 练习：学生信息录入
<img src="\img\python从入门到进阶（二）\学生信息录入.png" alt="学生信息录入" title="学生信息录入">

代码示例：
{% spoiler "点击显/隐内容" %}
```python
class student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

stu_info = {}

for i in range(1,11):
    print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    address = input("请输入学生地址：")
    stu_info[f"学生{i}"] = {"name":name, "age":age, "address":address}
    stu = student(name, age, address)
    print(f"学生{i}信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}】")

print("所有信息录入完毕，学生信息汇总如下：",stu_info)

# 当前录入第1位学生信息，总共需录入10位学生信息
# 请输入学生姓名：11
# 请输入学生年龄：11
# 请输入学生地址：11
# 学生1信息录入完成，信息为：【学生姓名：11，年龄：11，地址：11】
# 当前录入第2位学生信息，总共需录入10位学生信息
# 请输入学生姓名：22
# 请输入学生年龄：22
# 请输入学生地址：22
# 学生2信息录入完成，信息为：【学生姓名：22，年龄：22，地址：22】
# 当前录入第3位学生信息，总共需录入10位学生信息
# 请输入学生姓名：33
# 请输入学生年龄：33
# 请输入学生地址：33
# 学生3信息录入完成，信息为：【学生姓名：33，年龄：33，地址：33】
# 当前录入第4位学生信息，总共需录入10位学生信息
# 请输入学生姓名：44
# 请输入学生年龄：44
# 请输入学生地址：44
# 学生4信息录入完成，信息为：【学生姓名：44，年龄：44，地址：44】
# 当前录入第5位学生信息，总共需录入10位学生信息
# 请输入学生姓名：55
# 请输入学生年龄：55
# 请输入学生地址：55
# 学生5信息录入完成，信息为：【学生姓名：55，年龄：55，地址：55】
# 当前录入第6位学生信息，总共需录入10位学生信息
# 请输入学生姓名：66
# 请输入学生年龄：66
# 请输入学生地址：66
# 学生6信息录入完成，信息为：【学生姓名：66，年龄：66，地址：66】
# 当前录入第7位学生信息，总共需录入10位学生信息
# 请输入学生姓名：77
# 请输入学生年龄：77
# 请输入学生地址：77
# 学生7信息录入完成，信息为：【学生姓名：77，年龄：77，地址：77】
# 当前录入第8位学生信息，总共需录入10位学生信息
# 请输入学生姓名：88
# 请输入学生年龄：88
# 请输入学生地址：88
# 学生8信息录入完成，信息为：【学生姓名：88，年龄：88，地址：88】
# 当前录入第9位学生信息，总共需录入10位学生信息
# 请输入学生姓名：99
# 请输入学生年龄：99
# 请输入学生地址：99
# 学生9信息录入完成，信息为：【学生姓名：99，年龄：99，地址：99】
# 当前录入第10位学生信息，总共需录入10位学生信息
# 请输入学生姓名：00
# 请输入学生年龄：00
# 请输入学生地址：00
# 学生10信息录入完成，信息为：【学生姓名：00，年龄：00，地址：00】
# 所有信息录入完毕，学生信息汇总如下： {'学生1': {'name': '11', 'age': '11', 'address': '11'}, '学生2': {'name': '22', 'age': '22', 'address': '22'}, '学生3': {'name': '33', 'age': '33', 'address': '33'}, '学生4': {'name': '44', 'age': '44', 'address': '44'}, '学生5': {'name': '55', 'age': '55', 'address': '55'}, '学生6': {'name': '66', 'age': '66', 'address': '66'}, '学生7': {'name': '77', 'age': '77', 'address': '77'}, '学生8': {'name': '88', 'age': '88', 'address': '88'}, '学生9': {'name': '99', 'age': '99', 'address': '99'}, '学生10': {'name': '00', 'age': '00', 'address': '00'}}
```
{% endspoiler %}

## 06 其他内置方法
### 1、魔术方法
上文学习的__init__构造方法就是python类内置的方法之一，这些内置的类方法各自有特殊的功能，这些内置方法我们称之为魔术方法。

魔术方法非常多，主要学习以下几个常见的：

- 魔术方法
    - __init__ 构造方法
    - __str__ 字符串方法 
    - __lt__ 小于、大于符号比较
    - __le__ 小于等于、大于等于符号比较
    - __eq__ ==符号比较

#### __str__字符串方法
作用：通过该方法控制类转换为字符串的行为。

代码示例：
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student类对象：name={self.name}，age={self.age}"

student = Student("周杰轮", 11)
print(student)
print(str(student))
# Student类对象：name=周杰轮，age=11
# Student类对象：name=周杰轮，age=11
```
没有字符串方法直接输出该对象的话会输出内存地址。

#### __lt__小于符号比较方法
作用：可以实现两个对象的比较

代码示例：
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

stu1 = Student("周杰轮",12)
stu2 = Student("周杰",13)
print(stu1 < stu2) # True
print(stu1 > stu2) # False
```

#### __le__小于等于符号比较方法
作用：可以实现两个对象的比较

代码示例：
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __le__(self, other):
        return self.age <= other.age

stu1 = Student("周杰轮",12)
stu2 = Student("周杰",12)
print(stu1 <= stu2) # True
print(stu1 >= stu2) # True
```

#### __eq__比较运算符方法
作用：可以实现两个对象的比较

代码示例：
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("周杰轮",12)
stu2 = Student("周杰",12)
print(stu1 == stu2) # True
print(stu1 == stu2) # True
```

## 07 封装
> 本节要点
>> 1. 理解封装的概念
>> 2. 掌握私有成员的使用

面向对象的三大特性：封装、继承、多态

封装可以看作是一种思想，封装表示的是将现实世界事物的属性、行为封装到类中，描述为成员变量、成员方法，从而完成程序对现实世界事物的描述。

现实世界中的事物，有属性和行为，不是所有属性和行为都是开放的，程序中也是如此。

类中提供了私有成员的形式来支持：私有成员变量、私有成员方法。

定义私有成员的方式很简单，只需要在变量名和方法名前面加两个下划线即可完成私有成员的设置。

代码示例：
```python
class Phone:
    __current_voltage = None        # 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

phone = Phone()
# phone.__keep_single_core()          # 会报错
# print(phone.__current_voltage)      # 会报错
```

私有成员无法被类对象使用，但是可以被类中的其他成员使用。

代码示例：
```python
class Phone:
    __current_voltage = 0.5        # 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，已设置为单核运行进行省电")

phone = Phone()
phone.call_by_5g()
```

## 08 封装的课后习题
<img src="\img\python从入门到进阶（二）\设计带有私有成员的手机.jpg" alt="设计带有私有成员的手机" title="设计带有私有成员的手机">

代码示例：
```python
class Phone:
    __is_5g_enable = False
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()
# 5g关闭，使用4g网络
# 正在通话中
```

## 09 继承
使用继承的功能可以实现将旧的类改为新的类。

继承分为单继承和多继承。

### 1、继承的基础语法
- 单继承
    - 语法： class 类名(父类名):
            &emsp;&emsp;类内容体

被继承的类叫做父类，继承别人的类叫做子类。

代码示例：
```python
"""
演示单继承
"""
class Phone:
    IMEI = None     # 序列号
    producer = None # 厂商

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = "10001"   # 面部识别ID

    def call_by_5g(self):
        print("2022年新功能；5g通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()
# None
# 4g通话
# 2022年新功能；5g通话
```

- 多继承
    - Python的类之间也支持多继承，即一个类可以继承多个类。
    - 语法： class 类名(父类名1,父类名12,...):
            &emsp;&emsp;类内容体
- pass关键字
    - 表示无内容，空的意思

代码示例：
```python
"""
演示单继承
"""
class Phone:
    IMEI = None     # 序列号
    producer = None # 厂商

    def call_by_4g(self):
        print("4g通话")

class NFCReader:
    nfc_type = "第五代"
    producer = "HM"
    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控开启")

class MyPhone(Phone,NFCReader,RemoteControl):
    pass    # 补全语法

phone = MyPhone()
print(phone.producer)
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()
# None
# 4g通话
# NFC读卡
# NFC写卡
# 红外遥控开启
```

>多继承注意事项：
>>多个父类中，如果有同名的成员，那么默认以继承顺序（从左往右）为优先级。
>>即：先继承的先保留，后继承的被覆盖。

### 2、复写和使用父类成员
- 复写
    - 子类继承父类的成员属性和成员方法后，如果对其不满意，那么可以进行复写。
    - 即：在子类中重新定义同名的属性和方法即可。

- 调用父类同名成员
    - 一旦复写父类成员，那么类对象调用成员时，就会调用复写后的新成员；如果需要使用被复写的父类的成员，就需要特殊的调用格式

在子类中使用父类成员。

方式一：

代码示例：
```python
class Phone:
    IMEI = None                 # 序列号
    producer = "ITCAST"         # 厂商

    def call_by_5g(self):
        print("使用5g网络进行通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"        # 复写父类成员属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")

        # 方式一：使用父类名调用父类成员
        print(f"父类的厂商是:{Phone.producer}")
        Phone.call_by_5g(self)

        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)
# 开启CPU单核模式，确保通话的时候省电
# 父类的厂商是:ITCAST
# 使用5g网络进行通话
# 关闭CPU单核模式，确保性能
# ITHEIMA
```

方式二：

代码示例：
```python
class Phone:
    IMEI = None                 # 序列号
    producer = "ITCAST"         # 厂商

    def call_by_5g(self):
        print("使用5g网络进行通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"        # 复写父类成员属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")

        # 方式二
        print(f"父类的厂商是:{super().producer}")
        super().call_by_5g()

        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)
# 开启CPU单核模式，确保通话的时候省电
# 父类的厂商是:ITCAST
# 使用5g网络进行通话
# 关闭CPU单核模式，确保性能
# ITHEIMA
```

<font color=#FF0000 ><font size=3 >**注意：只可以在子类内部调用父类的同名成员，子类的实体类对象调用默认是调用子类复写的。**</font></font>

## 10 类型注解
>为什么要使用类型注解？
>>有时候pycharm无法给出提示以及自动补全，这时候需要使用类型注解。

- 类型注解：在代码中设计数据交互的地方，提供数据类型的注解（显式的说明）
- 主要功能
    - 帮助第三方IDE工具对代码进行类型推断，协助做代码提示
    - 帮助开发者自身对变量进行类型注释
- 支持：
    - 变量的类型注解
    - 函数（方法）形参列表和返回值的类型注解

### 1、变量的类型注解
基础语法： 变量：类型

注意：
1、元组类型设置类型详细注解，需要将每一个元素都标记出来
2、字典类型设置类型详细注解，需要两个类型，第一个是key，第二个是value

代码示例：
```python
# 基础数据类型注解
var_1: int = 10
var_2: str = "itheima"
var_3: bool = True
# 类对象类型注解
class Student:
    pass
stu:Student = Student()
# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"itheima": 666}
# 容器类型详细注解
my_list1: list[int] = [1, 2, 3]
my_tuple1: tuple[int, str, bool] = (1, "itheima", False)
my_dict1: dict[str, int] = {"itheima": 666}
```

除了使用 变量：类型这种语法进行注解外，还可以在注释中进行注解。

语法：#type：类型

代码示例：
```python
import json
import random

var_1 = random.randint(1, 10)               # type: int
var_2 = json.loads('{"name":"zhangsan"}')   # type: dict[str, str]
def func():
    return 10
var_3 = func()                              # type: int
```

注意：一般在无法直接看出变量类型的时候才会添加变量的类型注解；类型注解只是提示性的，并非决定性的，及时写错了也不会报错

### 2、函数（方法）的类型注解
- 函数和方法的形参类型注解语法：
- def 函数方法名(形参名：类型，形参名：类型，...)：pass

代码示例：
```python
# 对函数（方法）的形参进行类型注解
def add(x: int, y: int):
    return x+y

print(add(10,20)) # 30
```

- 函数和方法的返回值注解
- def 函数方法名(形参名：类型，形参名：类型，...) -> 返回值类型：
pass

代码示例：
```python
# 对函数（方法）的形参进行类型注解
def add(x: int, y: int) -> int:
    return x+y
sum = add(10, 20)
print(sum) # 30
```

### 3、Union类型
Union联合类型注解，在变量注解、函数（方法）注解和返回值注解中均可使用。

代码实例：
```python
from typing import Union
my_list: list[Union[int, str]] = [1, 2, "itheima", "itcast"]

def func(data: Union[list, str]) -> Union[int, str]:
    pass
```

## 11 多态
> 本节要点
>> 1. 理解多态的概念
>> 2. 理解抽象类（接口）的编程思想

- 多态：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态。（同样的行为（函数），传入不同的对象，得到不同的状态）

<img src="\img\python从入门到进阶（二）\多态.jpg" alt="多态" title="多态">

代码示例：
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵喵")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)
# 汪汪汪汪
# 喵喵喵喵
```

- （抽象类）接口

在上述示例代码中，父类Animal的speak方法是空实现，这种设计的含义是：
- 父类用来确定有哪些方法
- 具体的方法实现，有子类自行决定

这种写法就叫做抽象类（也称之为接口）

- 抽象类：含有抽象方法的类就叫做抽象类
- 抽象方法：方法体是空实现的称之为抽象方法

抽象类好比定义了一个标准，包含了一些抽象方法，要求子类必须实现

配合多态，完成
- 抽象的父类设计（设计标准）
- 具体的子态实现（实现标准）

代码示例：
{% spoiler "点击显/隐内容" %}
```python
class AC:
    def cool_wind(self):
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass
    def swing_l_r(self):
        """左右摆风"""
        pass

class Midea_AC(AC):
    def cool_wind(self):
        """制冷"""
        print("美的空调核心制冷技术")
    def hot_wind(self):
        """制热"""
        print("美的空调电热丝加热")
    def swing_l_r(self):
        """左右摆风"""
        print("美的空调无风感左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        """制冷"""
        print("格力空调核心制冷技术")
    def hot_wind(self):
        """制热"""
        print("格力空调电热丝加热")
    def swing_l_r(self):
        """左右摆风"""
        print("格力空调无风感左右摆风")

def make_cool(ac: AC):
    ac.cool_wind()

midea = Midea_AC()
gree = GREE_AC()

make_cool(midea)
make_cool(gree)
```
{% endspoiler %}

## 12 综合案例
<img src="\img\python从入门到进阶（二）\第一章综合案例.jpg" alt="第一章综合案例" title="第一章综合案例">

<img src="\img\python从入门到进阶（二）\综合案例需求分析.jpg" alt="需求分析" title="需求分析">

全程使用面向对象的知识解决问题。

### 文件读取
首先，需要进行文件的读取。

1. 为充分利用面向对象的知识实现文件的读取，首先需要设计一个类来存储所有数据信息：

代码示例：
```python
"""
数据定义的类 data_define.py
"""
# 用来记录数据的基本信息
class Record:
    # 构造方法
    def __init__(self, date, order_id, money, province):
        self.date = date                # 订单日期
        self.order_id = order_id        # 订单ID
        self.money = money              # 订单金额
        self.province = province        # 销售省份

    def __str__(self):
        return f"{self.date},{self.order_id},{self.money},{self.province}"
```
2. 接着是进行文件内容的读取

由于有多个不同文件需要进行读取，其中一个是文本数据，另一个是JSON数据，对此，需要设计一个抽象类，再设计子类分别针对这两种不同的数据进行读取。

涉及的知识点：
1. <font color=#008000 ><font size=5 >**readlines()用于读取文件中的所有数据，每一行的数据作为一个字符串存入列表中**</font></font>
2. <font color=#008000 ><font size=5 >**字符串的规整str.strip()可用于消去字符串前后的空格以及特殊字符**</font></font>

代码示例：
{% spoiler "点击显/隐内容" %}
```python
"""
和文件相关的类定义 file_define.py
"""
import json

from data_define import Record

# 定义抽象类
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件数据，将读到的每一条数据都转换为record对象，将它们都封装到list内返回即可"""
        pass

# 读取文本数据的文件读取器
class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path                # 定义成员变量记录文件的路径
    # 复写父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            line = line.strip()         # 消除读到的每一行数据后的换行符
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        f.close()
        return record_list

class JsonFileReader(TextFileReader):
    def __init__(self, path):
        self.path = path                # 定义成员变量记录文件的路径
    # 复写父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list

if __name__ == '__main__':
    text_file_reader = TextFileReader("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)
```
{% endspoiler %}

3. 进行数据整理：计算每一天的总销售额

可以使用字典来记录每日销售额

代码示例：
```python
# text.py
from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record

text_file_reader = TextFileReader("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并为一个list
all_data: list[Record] = jan_data + feb_data

#计算每一天的销售额
data_dict = {}
for record in all_data:
    # 判断日期是否在该字典中
    if record.date in data_dict.keys():
        # 当前日期已有记录
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money
```

4. 可视化图表开发

代码示例：
```python
# text.py
from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("E:/文件总览/pythonlearning/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并为一个list
all_data: list[Record] = jan_data + feb_data

#计算每一天的销售额
data_dict = {}
for record in all_data:
    # 判断日期是否在该字典中
    if record.date in data_dict.keys():
        # 当前日期已有记录
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.VINTAGE))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")
```


<img src="\img\python从入门到进阶（二）\第一章综合案例.png" alt="第一章综合案例" title="第一章综合案例">