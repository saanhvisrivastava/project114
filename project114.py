# -*- coding: utf-8 -*-
"""project114.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WO3MSKOyALhhvHqR6x87IlfH2ALRDwzk
"""

import csv
import pandas as pd
import plotly.express as px
import numpy as np

df=pd.read_csv('class114data.csv')

TOEFL_score=df['TOEFL Score'].tolist()
chance_admission=df['Admit'].tolist()

fig=px.scatter(x=TOEFL_score,y=chance_admission)
fig.show()

m=0.009
c=-2.43
y=[]
for x in TOEFL_score:
  y_value=m*x+c
  y.append(y_value)

fig.update_layout(shapes=[
  dict(
      type='line',
      y0=min(y),y1=max(y),
      x0=min(TOEFL_score),x1=max(TOEFL_score)
  )])

fig.show()

TOEFL_score_array=np.array(TOEFL_score)
Admit_array=np.array(chance_admission)
m,c=np.polyfit(TOEFL_score_array,Admit_array,1)
y=[]
for x in TOEFL_score_array:
  y_value=m*x+c
  y.append(y_value)

fig.update_layout(shapes=[
  dict(
      type='line',
      y0=min(y),y1=max(y),
      x0=min(TOEFL_score),x1=max(TOEFL_score)
  )])

fig.show()

print(m,c)