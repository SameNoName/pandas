# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('https://stepik.org/media/attachments/course/4852/iris.csv')
'''for column in df.iloc[:,1:]:
    sns.kdeplot(df[str(column)])'''
for column in df.iloc[:,1:]:
    g=sns.distplot(df[str(column)])
g.legend(df.iloc[:, 1:].columns)