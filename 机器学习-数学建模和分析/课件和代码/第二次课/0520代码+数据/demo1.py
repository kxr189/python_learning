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

#导入数据集
filename = 'C:/Users/22773/Desktop/pythonlearning/课件/第二次课/0520代码+数据/iris.data.csv'
names = ['separ-length', 'separ-width', 'petal-length', 'patal-width', 'class']
dateset = read_csv(filename, names=names)
print('数据维度：行 %s, 列 %s' % dateset.shape)

#查看一下数据集
print(dateset.head(10))

#描述性统计
print(dateset.describe())

#数据分布情况
print(dateset.groupby('class').size())

#数据可视化
dateset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

dateset.hist()
pyplot.show()

scatter_matrix(dateset)
pyplot.show()

#分离数据集
array = dateset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.2
seed = 7
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=validation_size, random_state=seed, shuffle=True)

#算法
models = {}
models['LR'] = LogisticRegression()
models['KNN'] = KNeighborsClassifier()
models['LDA'] = LinearDiscriminantAnalysis()
models['CART'] = DecisionTreeClassifier()
models['SVM'] = SVC()
models['NB'] = GaussianNB()

results = []
for key in models:
    kflod = KFold(n_splits=10, random_state=seed, shuffle=True)
    cv_results = cross_val_score(models[key], X_train, Y_train, cv=kflod, scoring='accuracy')
    results.append(cv_results)
    print('%s: %f (%f)' %(key, cv_results.mean(), cv_results.std()))

svm = SVC()
svm.fit(X=X_train, y=Y_train)
predictions = svm.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))