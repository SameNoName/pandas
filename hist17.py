# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv')
l=[]
for x in df.iloc[:, -1]:
    n = x.count(' ') + 1
    l.append(n)
i = min(l)
index=[]
l1=[]
while i <= max(l):
    l1.append(l.count(i))
    index.append(i)
    i=i+1
plt.bar(index,l1)