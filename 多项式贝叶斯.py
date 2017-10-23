import pandas as pd
import numpy as np
import numpy as np  
df=pd.read_csv('C:\Users\Administrator\Desktop\»ÀŒ¿≤Œøº£¨ø∆∆’‘§≤‚\zongti.csv',header=0)
X = df[[2,3,4,5,6]]  
y = df[[7]]
y=np.ravel(y)
mubiao=df[[3,4,5,6,7]]
from sklearn.naive_bayes import MultinomialNB  
clf = MultinomialNB().fit(X, y)  
print clf.predict(mubiao)  
