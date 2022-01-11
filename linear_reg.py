import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets , linear_model
from sklearn.metrics import mean_squared_error

dbts=datasets.load_diabetes()
#print(dbts.keys())

#dbts_x=dbts.data[:,np.newaxis,2]                         #use only one feature to find output
dbts_x=dbts.data                                          #use all features to find the output
dbts_x_train=dbts_x[:-30]
dbts_x_test=dbts_x[-30:]
dbts_y_train=dbts.target[:-30]
dbts_y_test=dbts.target[-30:]

model=linear_model.LinearRegression()
model.fit(dbts_x_train,dbts_y_train)
dbts_y_predict=model.predict(dbts_x_test)

print ("Mean squared error is :", mean_squared_error(dbts_y_test,dbts_y_predict))
print ("Weights :",model.coef_)
print ("Intercept :",model.intercept_)

#plt.scatter(dbts_x_test,dbts_y_test)
#plt.plot(dbts_x_test,dbts_y_predict)
#plt.show()
fig, x = plt.subplots(figsize =(10, 10))
x.hist(dbts_x_test, bins = [0, 5,10,15,20,25])
  
# Show plot
plt.show()