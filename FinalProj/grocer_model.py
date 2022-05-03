#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:59:34 2021

@author: pauljojy
"""

import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import pickle
import altair as alt

categories = ['onpromotion', 'year', 'month', 'day', 'perishable','AUTOMOTIVE', 'BEAUTY', 'BEVERAGES',
       'BOOKS', 'BREAD/BAKERY', 'CELEBRATION',
       'CLEANING', 'DAIRY', 'DELI', 'EGGS',
       'FROZEN FOODS', 'GROCERY I', 'GROCERY II',
       'HARDWARE', 'HOME AND KITCHEN I',
       'HOME AND KITCHEN II', 'HOME APPLIANCES',
       'HOME CARE', 'LADIESWEAR', 'LAWN AND GARDEN',
       'LINGERIE', 'LIQUOR,WINE,BEER', 'MAGAZINES',
       'MEATS', 'PERSONAL CARE', 'PET SUPPLIES',
       'PLAYERS AND ELECTRONICS', 'POULTRY',
       'PREPARED FOODS', 'PRODUCE',
       'SCHOOL AND OFFICE SUPPLIES', 'SEAFOOD']

st.title("Grocery Store Forecaster")
st.write("This app uses an RNN to predict sales for an item. Note that the dummy data used to train the model ranges from 2014-2017, so picking dates too far into the future leads to more unstable predictions.")
date = st.date_input("Choose a date to forecast from. The model will create a 30 day forecast from this date.", key = 'date')

st.sidebar.title('Parameters')
cat = st.sidebar.selectbox("Choose an item category:", options = categories[5:], key = 'cat')
perishable = st.sidebar.radio("Is this item perishable?", options = ['Yes','No'], key = 'perishable')
promo = st.sidebar.radio("Is this item on promotion?",options = ['Yes','No'], key = 'promo')

df = pd.DataFrame({
    'Date': [date],
    'Category': [cat],
    'Perishable': [perishable],
    'On Promotion':[promo]
})

model = tf.keras.models.load_model('Grocer_Model.h5')

st.table(df)
dates = pd.date_range(start=date, periods=60)
data = np.zeros(len(categories), dtype=int)
if promo == 'Yes':
    data[0] = 1
if perishable == 'Yes':
    data[4] = 1
data[categories.index(cat)] = 1

test = [data.copy() for i in range(60)]

for i in range(len(test)):
    test[i][1] = dates[i].year
    test[i][2] = dates[i].month
    test[i][3] = dates[i].day

    
#Load scalers
input_scaler = pickle.load(open('inpscale.sav','rb'))
scaler_y = pickle.load(open('outscale.sav','rb'))

X = input_scaler.transform(test)
print(np.shape(X))
Xs = []
for i in range(len(X) - 30):
    v = X[i:i+30, :]
    Xs.append(v)
X_transformed = np.array(Xs)
prediction = model.predict(X_transformed)
prediction = scaler_y.inverse_transform(prediction)
display = pd.DataFrame(prediction,columns=['Unit Sales'])
display['Days'] = range(len(display))

line_chart = alt.Chart(display).mark_line(interpolate='basis').encode(x='Days',y='Unit Sales').properties(title='Unit Sales vs. Days')

st.altair_chart(line_chart,True)

