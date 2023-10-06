# 导入类库

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

# 导入数据集

filename = 'C:/Users/22773/Desktop/pythonlearning/课件/第二次课/0520代码+数据/iris.data.csv'

# 写入每一列的概念
names = ['separ-length','separ-width','petal-length','petal-width','class']

# 建立数据集
dataset = read_csv(filename,names=names)

# 显示数据维度
print('数据维度：行 %s，列 %s' %dataset.shape)

# 查看数据集(前十行)
print(dataset.head(10))

# 描述性统计(均值、标准差、最大最小值)
print(dataset.describe())

# 查看分布情况(看class这一类)
print(dataset.groupby('class').size())

# 数据的可视化 箱型图
dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
pyplot.show()

# 直方图
dataset.hist()
pyplot.show()

# 散点图
scatter_matrix(dataset)
pyplot.show()

# 分离数据集 将所有数据集分为训练集和验证集
array = dataset.values
# 分离x 和 y
# 0到3列
X = array[:,0:4]
# 第4列
Y = array[:,4]
# 20%的验证集 8:2分
validation_size = 0.2
seed = 7
X_train,X_validation,Y_train,Y_validation = train_test_split(X, Y, test_size=validation_size,random_state=seed, shuffle=True)

# 算法
models = {}
# 回归模型
models['LR'] = LogisticRegression()
# 聚类模型
models['KNN'] = KNeighborsClassifier()
# 线性分析
models['LDA'] = LinearDiscriminantAnalysis()
# 决策树模型
models['CART'] = DecisionTreeClassifier()
# 向量机模型
models['SVM'] = SVC()
# 高斯分布
models['NB'] = GaussianNB()

results = []
for key in models:
    # 10折交叉检验
    kflod = KFold(n_splits=10, random_state=seed, shuffle=True)
    # 输出每个模型的准确度
    cv_results = cross_val_score(models[key], X_train, Y_train, cv=kflod, scoring='accuracy')
    results.append(cv_results)
    print('%s:%f (%f)' %(key, cv_results.mean(), cv_results.std()))

svm = SVC()
# 使用评估数据集来评估这个算法
svm.fit(X=X_train, y=Y_train)
# 用预测集进行预测
predictions = svm.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
# 混淆矩阵
print(confusion_matrix(Y_validation, predictions))
# 打印分析报告
print(classification_report(Y_validation, predictions))
