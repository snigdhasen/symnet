import pandas as pd 
import numpy as np

base_path="/home/tejas/PESU/RC/SymNet_Rahul/symnet/tej_tests/CaliforniaHousing/method_26/trial_1/"

df_time_constant=pd.read_csv(base_path+"epoch_times.log")
print(df_time_constant.columns)
a=df_time_constant.loc[:181,'Time taken'].values
print(a)
print(np.sum(a))