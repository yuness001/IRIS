

import pandas as pd

iris=pd.read_csv('/content/IRIS.csv')

iris.head()

iris.describe()

iris.info()

iris['species'].value_counts()

binary_species=[]
for i in iris['species']:
  if i == 'Iris-virginica':
    binary_species.append(0)
    continue
  elif i == 'Iris-versicolor':
    binary_species.append(1)
    continue
  else:
    binary_species.append(2)

print(binary_species)

print(iris['species'])

iris['type']=binary_species

iris=iris.drop('species',axis=1)

iris

from sklearn.model_selection import train_test_split

X=iris.iloc[:,:-1]
y=iris['type']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33)

from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)

knn.predict(X_test)

print(knn.score(X_test,y_test))
