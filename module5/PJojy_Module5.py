import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv('cars.csv')
print (df.columns)
print(df.head())

print(df.dtypes)

# Check unique levels and see if any marker is used for a missing level
for col in df.columns:
    if df[col].dtype == np.object:
        print(col, df[col].unique())
        print(len(df[col].unique()))
#There seem to be no missing levels, so we can move on.
#For these variables in a pandas dataframe, we can use an ordinal encoder to assign numerical values. We do not care about order for these variables, so the numbering can be arbitrary. 
encoder = OrdinalEncoder()
df[['manufacturer_name','model_name','transmission','color', 'engine_fuel','engine_type','body_type','state','drivetrain','location_region']] = encoder.fit_transform(df[['manufacturer_name','model_name','transmission','color', 'engine_fuel','engine_type','state','body_type','drivetrain','location_region']])
print(df[['manufacturer_name','model_name','transmission','color', 'engine_fuel','engine_type','body_type','state','drivetrain','location_region']].head())



print(df.dtypes)

