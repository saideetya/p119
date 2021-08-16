#Uploading the csv
from google.colab import files
data_to_load = files.upload()#Uploading the csv
from google.colab import files
data_to_load = files.upload()

import pandas as pd

#Column Name
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']

df = pd.read_csv("diabetes.csv", names=col_names).iloc[1:]

print(df.head())

#Uploading the csv
from google.colab import files
data_to_load = files.upload()#Uploading the csv
from google.colab import files
data_to_load = files.upload()

import pandas as pd

#Column name
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']

df = pd.read_csv("diabetes.csv", names=col_names).iloc[1:]

print(df.head())


ssssssssss