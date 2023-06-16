# Program for demonstration of one hot encoding

# import libraries
import numpy as np
import pandas as pd

# import the data required
data = pd.read_csv('iris.csv')
#df = pd.DataFrame(data, columns=['f1', 'f2', 'f3', 'f4','class'])

print(data['class'].unique())
print(data['class'].value_counts())
# one hot encoding#

one_hot_encoded_data = pd.get_dummies(data, columns = ['class'])
print(one_hot_encoded_data)
