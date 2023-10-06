

# python机器学习————数学建模与分析
## 一、初始python与机器学习
### 1、初始python
   
   python有很多用途：

   <center>

   |Python数值运算： Numpy |Python数据分析：Pandas|
   |:----:|:-----:|
   |Python时序分析: FbProphet |Python可视化工具：matplotlib|
   |Python地图分析： folium |Python web开发：Flask|
   |Python机器学习： Scikit-Learn XGBoost |Python深度学习：TensorFlow PyTorch|
   </center>

### 2、python安装（Anaconda安装）

### 3、什么是机器学习？

**初识机器学习——什么是机器学习？**

      ● 机器学习（Machine Learning,ML）是一门多领域的交叉学科，涉及概率论、统计学、线性代数、算法等多门学科。它专门研究计算机如何模拟和学习人的行为，以获取新的知识和技能，重新组织已有的知识结构使之不断完善自身的性能。
      ● 机器学习已经有了十分广泛的应用，例如：数据挖掘、计算机视觉、自然语言处理、生物特征识别、医学诊断、检查信用卡欺诈、证券市场分析、DNA测序……

        如何解释数据，处理数据，从中抽取价值，展示和交流数据结果，在未来十年将是最重要的职业技能，甚至是大学，中学，小学的学生也必须具备的技能，因为我们每时每刻都在接触大量的免费信息，如何理解数据，从中抽取有价值的信息才是其中的关键。 
                                                         ---谷歌公司的首席经济学家Hal Varian
    
    
<center>

|||西瓜数据集|||
|:----:|:---:|:-----:|:-----:|:-----:|
|编号|色泽|根蒂|敲声|好瓜|
|1 |青绿|蜷缩|浊响|是|
|2 |乌黑|蜷缩|浊响|是|
|3 |青绿|硬挺|清脆|否|
|4 |乌黑|稍蜷|沉闷|否|
</center>

**机器学习常用术语：**

      - 数据集：这组记录的集合；
      - 样本：其中每条记录是关于一个事件或
      - 对象（这里是一个西瓜）的描述
      - 特征：反映对象在某方面的性质的事项，例如“色泽”“根蒂”“敲声”
      - 特征值：属性上的取值，例如“青绿”“乌黑”
      - 样本空间：由特征张成的空间，例如我们把“色泽”“根蒂”“敲声”作为三个坐标轴，每个西瓜都可在这个空间中找到自己的坐标位置。
      - 特征向量：空间中的每个点都对应一个坐标向量

**数据集：**

    数据集，从字面意思很容易理解，它表示一个承载数据的集合，如果说“模型”是“魔法盒”的话，那么数据集就是负责给它充能的“能量电池”，简单地说，如果缺少了数据集，那么模型就没有存在的意义了。数据集可划分为“训练集”和“测试集”，它们分别在机器学习的“训练阶段”和“预测输出阶段”起着重要的作用。

**训练集&假设：**

    从数据中学得的模型，称为“学习”或“训练”。这个过程通过执行某个学习算法完成，训练过程中使用的数据称为“训练数据”，其中每一个样本称为“训练样本”，由“训练样本”组成的集合称为“训练集”。学得模型对应了关于数据的某种潜在的规律，因此亦称“假设”，假设可以理解成“模型”；这种潜在的规律自身，则称为“真相”。学习的过程就是为了找出或逼近真相。

**测试集：**

    在获得“训练模型”后，我们还需要知道用该模型来预测其他情况的结果的效果好不好，所以需要引入“测试集”，如果该模型也能够很好的预测出“测试集”的结果，那么我们可以认为“训练模型”非常接近“真相”。

### 4、机器学习的分类

    ● 机器学习的算法分为两大类：监督学习、无监督学习
    ● 监督学习：在机器学习过程中提供对错指示。比如数据的结果部分为（0，1），通过算法让机器自己减少误差。这一类主要应用于分类和回归（Regression&Classify）。
      监督学习从给定的训练集中学习一个目标函数，当新的数据到来时，可以根据这个函数预测结果。监督学习要求包括输入和输出，也就是特征和目标。
    ● 非监督学习：归纳行学习，利用K方式建立中心，通过循环和递减运算减小误差达到分类的目的。

### 5、数学建模Python机器学习的五大步骤

    定义问题 ——> 数据理解 ——> 数据准备 ——> 评估算法 ——> 优化模型 ——> 结果部署 

## 二、第一个机器学习python数模项目
**项目**简介：
    
    本例题是针对鸢尾花进行分类的一个项目，数据集是包含鸢尾花的三个亚属的分类信息，通过机器学习算法生成一个模型，自动分类新数据到这三个亚属中的某一个。

分析数据集特征：
    
    1.所有的特征数据都是数字，不需要考虑如何导入和处理数据。
    2.这是一个分类问题，可以通过有监督学习算法来解决。
    3.所有的特征的数值采用相同的单位，不需要进行尺度的转换。

步骤：
<center>

<font color=#FF000 ><font size=4 >导入数据</font></font>\
&dArr;\
<font color=#FF000 ><font size=4 >分析数据</font></font>\
&dArr;\
<font color=#FF000 ><font size=4 >数据可视化</font></font>\
&dArr;\
<font color=#FF000 ><font size=4 >评估算法</font></font>\
&dArr;\
<font color=#FF000 ><font size=4 >实施预测</font></font>\
&dArr;\

</center>

具体步骤：
```
一、导入数据；
二、导入类库；
三、导入数据集；
四、概述数据
    1、数据的维度；
    2、查看数据自身；
    3、统计描述；
    4、数据分类的情况；
五、数据可视化
    1、单变量图表
    2、多变量图标
六、评估算法
    1、分离出评估数据集
    2、采用10折交叉验证来评估算法模型
    3、生成六种模型来预测新数据
    4、选择最优模型
七、实施预测
八、总结
```


### 1、下载安装类库

安装类库：

    直接在终端中安装：pip install pandas

导入类库：

    from pandas import read_csv 
    from pandas.plotting import scatter_matrix 
    from matplotlib import pyplot 
    from sklearn.model_selection import train_test_split 
    from sklearn.model_selection import KFold 
    from sklearn.model_selection import cross_val_score 
    from sklearn.metrics import classification_report 
    from sklearn.metrics import confusion_matrix 
    from sklearn.metrics import accuracy_score 
    from sklearn.linear_model import LogisticRegression 
    from sklearn.tree import DecisionTreeClassifier 
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
    from sklearn.neighbors import KNeighborsClassifier 
    from sklearn.naive_bayes import GaussianNB 
    from sklearn.svm import SVC 

### 2、导入数据并分析

代码示例：单引号中的是数据集的路径（注意）

```
 filename = 'C:/Users/22773/Desktop/pythonlearning/课件/第二次课/0520代码+数据/iris.data.csv'
```

#### 代码知识点

<font color=#FF000 ><font size=5 >**详见“自编代码”**</font></font>



### 3、创建六个模型并比较




