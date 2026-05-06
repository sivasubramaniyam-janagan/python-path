import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('husl')
import matplotlib.pyplot as plt
#%matplotlib inline

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.metrics import classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier


url ='https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=col_names)

print(dataset.head())
print(dataset.describe())
print(dataset.info() )


sns.violinplot(x='class', y='sepal-length', data=dataset)
plt.show()


plt.figure(figsize=(10, 6))
sns.heatmap(dataset.corr(), annot=True, cmap='cubehelix_r')
plt.show()