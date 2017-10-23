import pandas as pd;
import numpy as np;
from sklearn import ensemble, cross_validation;

df=pd.read_csv('E:\\tianchi\yongdian\yongdianyuce.csv',sep=',')

train=df[[2,3,4]]
train=np.array(train)
target=df[[1]]
target=np.array(target)  
params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2,  
              'learning_rate': 0.01, 'loss': 'ls'}  
clf = ensemble.GradientBoostingRegressor(**params)
  
clf.fit(train,target.ravel()) #—µ¡∑  
    # mse = mean_squared_error(test_target, clf.predict(test_feature)) #‘§≤‚≤¢«“º∆À„MSE  
    # print(mse)  
yuce=pd.read_csv('E:\\tianchi\yongdian\yuce.csv',sep=',')
pre=clf.predict(yuce)  
  
     
print pre;

  
 
