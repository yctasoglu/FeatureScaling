from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import PowerTransformer
from sklearn import preprocessing
from scipy import stats
from scipy.stats import mstats
from sklearn.preprocessing import FunctionTransformer
from math import ceil
from scipy.stats import norm

import os
cwd = os.path.dirname(os.getcwd()) 
print(cwd)
#Get Data Frame from local parquet file
df = pd.read_parquet(r'path')

df_for_transformation = df.copy()
print("Transformation")

#Empty cells must be filled or eliminated before scaling.
df_for_transformation = df_for_transformation.fillna(df_for_transformation.mean())

#Get list of columns to use after transformation
columns_for_transformation = list(df_for_transformation)

#List of Scaling used together
#MinMaxScaler
#StandardScaler
#Normalizer
#MaxAbsScaler
#RobustScaler
#QuantileTransformer
#PowerTransformer
#FunctionTransformer(np.log1p)

Scalers1 = {0:MinMaxScaler(),1:Normalizer(),2:QuantileTransformer()}

Scalers2 = {0:FunctionTransformer(np.log1p), 1:StandardScaler(), 2:Normalizer(),
                3:MaxAbsScaler(),4:RobustScaler(),5:QuantileTransformer(),
                6:PowerTransformer(),1:MinMaxScaler()}


metrics_row = 0

for i in range(len(Scalers1)):
    for a in range(len(Scalers2)):
        if a < len(Scalers2):

            first_scaler = Scalers1[i]
            second_scaler = Scalers2[a]
            print("Selected Scalers:")
            print(first_scaler,second_scaler)
            print("Selected Items")
            print(i,a)

            scaler1 = first_scaler
            df_for_transformation = scaler1.fit_transform(df_for_transformation)

            scaler2 = second_scaler
            df_for_transformation = scaler2.fit_transform(df_for_transformation)

            df_for_transformation = pd.DataFrame(df_for_transformation)
            df_for_transformation.columns = columns_for_transformation


