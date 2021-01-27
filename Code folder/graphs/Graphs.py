#!/usr/bin/env python
# coding: utf-8

# In[170]:


import numpy as np


# In[171]:


import pandas as pd


# In[172]:


import matplotlib.pyplot as plt


# In[173]:


import seaborn as sns


# In[174]:


# downloading the data set


# In[175]:


dataset = pd.read_csv('/Users/oksanagera/Downloads/Covid Dataset.csv')


# In[176]:


print(dataset)


# In[177]:


dataset.info()


# In[178]:


# checking columns


# In[179]:


dataset.columns


# In[180]:


# checking if any value is missing


# In[181]:


dataset.isnull().sum()


# In[182]:


print(dataset.shape)


# In[183]:


# looking into the DataFrame header to get familiar with the data


# In[184]:


dataset.head(3)


# In[185]:


# Using matplotlib to create a pie chart to compare total percentage of patients with corona and without


# In[186]:


dataset["COVID-19"].value_counts()


# In[187]:


print(plt.style.available)


# In[188]:


dataset["COVID-19"].value_counts().plot.pie(autopct='%1.01f%%',shadow=False)
plt.style.use('seaborn-pastel')


# In[189]:


# changing Yes/No to 1/0


# In[190]:


for i in dataset.columns:
    dataset[i] = dataset[i].replace('No', 0).replace('Yes', 1)


# In[191]:


dataset.head(3)


# In[193]:


dataset.drop('Wearing Masks', axis = 1, inplace = True)


# In[194]:


dataset.head(3)


# In[195]:


dataset.drop('Sanitization from Market', axis = 1, inplace = True)


# In[196]:


dataset.head(3)


# In[198]:


cor = dataset.corr()


# In[199]:


print(cor)


# In[216]:


sns.heatmap(cor, annot=True, fmt=".2f", 
           linewidths=5, cmap='mako', vmin=-1, vmax=1, 
           cbar_kws={"shrink": .8}, square=True)


# In[217]:


# lowest correlation with COVID-19 - Running Nose, Gastrointestinal, Asthma, Chronic Lung Disease, Headache, Heart Disease, Diabetes, Fatigue 


# In[223]:


kot = cor[cor>=.3]
plt.figure(figsize=(12,8))
sns.heatmap(kot, cmap="Greens")


# In[227]:


c1 = cor.abs().unstack().drop_duplicates()
c1.sort_values(ascending = False)


# In[230]:


sns.countplot(x='Breathing Problem',hue='COVID-19',data=dataset)


# In[231]:


sns.countplot(x='Abroad travel',hue='COVID-19',data=dataset)


# In[232]:


sns.countplot(x='Sore throat',hue='COVID-19',data=dataset)


# In[234]:


sns.countplot(x='Dry Cough', hue='COVID-19', data=dataset)


# In[ ]:




