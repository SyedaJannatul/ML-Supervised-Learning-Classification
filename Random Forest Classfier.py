#Random Forest Classifier

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing dataset
dataset = pd.read_csv("Social_Network_Ads.csv")
     #Set matrix of idependent variable
X=dataset.iloc[:,[2,3]].values
    #Set matrix of dependent variable
Y=dataset.iloc[:,4].values

"""
#Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
"""

""" 
#Categorical variable,Dummy variable & One hot encoding
    #Categorical variable
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
    #Dummy variable & One hot encoding
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
    #Categorical variable
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)
"""

#Spliting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=0)

#Feature Scalimg
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#Fitting Random Forest Classifier to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 15,criterion = 'entropy',random_state = 0)
classifier.fit(X_train,Y_train)

#Predicting the Test set results
Y_pred = classifier.predict(X_test)

#Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test,Y_pred)

#Visualizing the training  set result
from matplotlib.colors import ListedColormap
X_set,Y_set = X_train,Y_train
X1,X2 = np.meshgrid(np.arange(start=X_set[:,0].min() -1, stop=X_set[:,0].max()+1,step = 0.01),
                    np.arange(start=X_set[:,1].min() -1, stop=X_set[:,1].max()+1,step = 0.01))
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),alpha=0.75, 
             cmap = ListedColormap(('white','yellow')))
plt.xlim((X1.min(),X1.max()))
plt.ylim((X2.min(),X2.max()))
for i,j in enumerate(np.unique(Y_set)):
	plt.scatter(X_set[Y_set ==j,0],X_set[Y_set ==j,1],
	c = ListedColormap(('red','green'))(i),label = j)
plt.title('Random Forest Classifier(Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

#Visualizing the Testing set result
from matplotlib.colors import ListedColormap
X_set,Y_set = X_test,Y_test
X1,X2 = np.meshgrid(np.arange(start=X_set[:,0].min() -1, stop=X_set[:,0].max()+1,step = 0.01),
                    np.arange(start=X_set[:,1].min() -1, stop=X_set[:,1].max()+1,step = 0.01))
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),alpha=0.75, 
             cmap = ListedColormap(('white','yellow')))
plt.xlim((X1.min(),X1.max()))
plt.ylim((X2.min(),X2.max()))
for i,j in enumerate(np.unique(Y_set)):
	plt.scatter(X_set[Y_set ==j,0],X_set[Y_set ==j,1],
	c = ListedColormap(('red','green'))(i),label = j)
plt.title('Random Forest Classifier(Testing set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()



