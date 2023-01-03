#!/usr/bin/env python
# coding: utf-8

# In[292]:


import pandas as pd


# In[293]:


df = pd.read_csv('world population.csv')
df.head(5)


# In[294]:


df.isnull().sum().any()


# There is some null values and punctuations. so we have to clean it

# ### preprocessing
# 
# * drop unnecessary column
# * fill null values
# * remove punctuation
# * proper column data-type 

# In[295]:


# actually we don't need this col so drop it 

df = df.drop('Rank', axis=1)


# In[296]:


# fill all null values with 0 

df = df.fillna(0)


# In[297]:


# remove punctuations

df.replace(',','', regex=True, inplace=True)


# In[298]:


df.head(1)


# In[ ]:





# ### Our dataset contains percentages and dollar signs. If we wanted, we could have removed these in the previous simple rules [ replace() ] . But we will apply different rules here.
# 

# In[299]:


# in our datasets their are some percentage, we have to remove them. and we are gonna using rstrip().
# well, basically rstrip() returns a copy of the string with trailing characters removed (based on the string argument passed)

df['Yearly_Change'] = df['Yearly_Change'].str.rstrip('%').astype('float64')
df['Urban _Pop %'] = df['Urban _Pop %'].str.rstrip('%')
df['World_Share'] = df['World_Share'].str.rstrip('%')


# In[300]:


# but still our 'Urban_Pop % and Median_Age' is not free to go. this cols contain some non-numeric value. 
# we have clean it and make it numeric

df['Urban _Pop %'] = pd.to_numeric(df['Urban _Pop %'], errors='coerce')
df['Median_Age'] = pd.to_numeric(df['Median_Age'], errors='coerce')
df['Fertility_Rate'] = pd.to_numeric(df['Fertility_Rate'], errors='coerce')


# In[301]:


# now fill this nan values with zero

import numpy as np

df['Urban _Pop %'] = df['Urban _Pop %'].replace(np.nan, 0)
df['Median_Age'] = df['Median_Age'].replace(np.nan, 0)
df['Fertility_Rate'] = df['Fertility_Rate'].replace(np.nan, 0)


# In[ ]:





# In[302]:


# remove dollar '$' sign

df['Density(P/Km²)'] = [x.strip('$') for x in df['Density(P/Km²)']]


# In[ ]:





# In[303]:


# now change data type

df['Population(2020)'] = df['Population(2020)'].astype('int64')
df['Net_Change'] = df['Net_Change'].astype('int64')
df['Yearly_Change'] = df['Yearly_Change'].astype('float64')
df['Density(P/Km²)'] = df['Yearly_Change'].astype('float64')
df['Land_Area(Km²)'] = df['Land_Area(Km²)'].astype('int64')
df['Migrants(net)'] = df['Migrants(net)'].astype('int64')
df['Fertility_Rate'] = df['Fertility_Rate'].astype('float64')
df['Median_Age'] = df['Median_Age'].astype('int64')
df['Urban _Pop %'] = df['Urban _Pop %'].astype('int64')
df['World_Share'] = df['World_Share'].astype('float64')


# In[ ]:





# In[ ]:


## Our Desired Dataset is now crystal clear


# In[305]:


df.head(10)


# In[ ]:





# #### Here are several ways to remove the dollar sign

# In[291]:


#1. df['Density(P/Km²)'] = df['Density(P/Km²)'].apply(lambda x: float(x.split()[0].replace('$', '')))

#2. df['Density(P/Km²)'] = df['Density(P/Km²)'].apply(lambda x: x.strip('$'))

#3. df['Density(P/Km²)'] = df['Density(P/Km²)'].apply(lambda x: x.replace('$',''))

#4. df['Density(P/Km²)'] = [x.strip('$') for x in df['Density(P/Km²)']]

#5. df['Density(P/Km²)'] = [x.strip('$') for x in df['Density(P/Km²)']]

#6. df['Density(P/Km²)'] = [x[1:] for x in df['Density(P/Km²)']]


# In[ ]:




