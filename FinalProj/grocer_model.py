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

categories = ['onpromotion','perishable','AUTOMOTIVE', 'BEAUTY', 'BEVERAGES',
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
st.write("This app uses an RNN to predict sales for an item.")
date = st.date_input("Choose a date to forecast from. The model will create a 7 day forecast from this date.", key = 'date')

st.sidebar.title('Parameters')
cat = st.sidebar.selectbox("Choose an item category:", options = categories[2:], key = 'cat')
perishable = st.sidebar.radio("Is this item perishable?", options = ['Yes','No'], key = 'perishable')
promo = st.sidebar.radio("Is this item on promotion?",options = ['Yes','No'], key = 'promo')

df = pd.DataFrame({
    'Date': [date],
    'Category': [cat],
    'Perishable': [perishable],
    'On Promotion':[promo]
})

st.table(df)
dates = pd.date_range(start=date, periods=7)
data = np.zeros(len(categories))
if promo == 'Yes':
    data[0] = 1
if perishable == 'Yes':
    data[1] = 1
data[categories.index(cat)] = 1

