import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
df=pd.read_csv('disease_detection\dengue.csv')
df=df.drop('serial',axis=1)
df.duplicated().sum()
df.isnull().sum()
df.nunique()
for i in range(df.shape[0]):
    if df.loc[i,'cases']>19000:
        df.loc[i,'labels']=1
    elif df.loc[i,'cases']>10000:
        df.loc[i,'labels']=2
    elif df.loc[i,'cases']>5000:
        df.loc[i,'labels']=3
    elif df.loc[i,'cases']>1000:
        df.loc[i,'labels']=4
    else:
        df.loc[i,'labels']=5
import warnings
warnings.filterwarnings('ignore')
import numpy as np
df['labels'].unique

df['labels'].value_counts()

df_corr = df.corr()

# plt.figure(figsize=(30,10))
# matrix=np.triu(df_corr)
# sns.heatmap(df_corr,annot=True,linewidth=.8,mask=matrix,cmap="rocket");
# plt.show()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['labels']=le.fit_transform(df['labels'])
X=df.iloc[:,:-1]
y=df['labels']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,stratify=y,random_state=42)

rf=RandomForestRegressor()
rf.fit(X_train,y_train)
y_pred=rf.predict(X_test)
rf.score(X_test,y_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred.round())

if accuracy_score(y_test,y_pred.round())>0.8:
    print("Dengue cases are high")
else:
    print("Dengue cases are low")


filename= 'dengue_model.sav'
saved_model=joblib.dump(rf,filename)
