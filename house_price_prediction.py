import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\Afaq Latif\Downloads\House Price Dataset\housetrain.csv")
print(df.shape)
#print(df.head(5))
pd.set_option('display.max_columns',None)
##pd.set_option('display.max_rows',None)
print(df.head(5))
#df.info()                            #info about data
df.isnull().sum()                    #total missing values in each column
#plt.figure(figsize=(25,25))          # ???
#sns.heatmap(df.isnull())             # ???
null_var=df.isnull().sum()/df.shape[0] *100    #find percentage of missing values
print(null_var)
drop_columns=null_var[null_var>17].keys()      # @@@
print(drop_columns)
df1=df.drop(columns=drop_columns)              #drop columns
print(df1.shape)
#sns.heatmap(df1.isnull()) 
df2=df1.dropna()                               # @@@
print(df2.shape)
#sns.heatmap(df2.isnull()) 
