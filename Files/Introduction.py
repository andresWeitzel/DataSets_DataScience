#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[6]:


df= pd.read_csv('C:\Users\andre\Downloads\gapminder-FiveYearData.csv')


# In[3]:


df= pd.read_csv('C:/Users/andre/OneDrive/Escritorio/LenguajesProgramacion/DataAnalyticsPython/gapminder-FiveYearData.csv')


# In[4]:


df


# In[ ]:





# In[6]:


print(df.head())


# In[ ]:





# In[7]:


print(df.shape)


# In[ ]:





# In[8]:


print(df.columns)


# In[ ]:





# In[9]:


print(df.rows)


# In[ ]:



   


# In[ ]:





# In[10]:


print(df.dtypes)


# In[ ]:





# In[11]:


print(df.info)


# In[12]:


country_df=df['country']


# In[13]:


print(country_df.head())


# In[ ]:





# In[14]:


df.loc[0]


# In[ ]:





# In[1]:


print(df.loc[10:13, ['country', 'lifeExp']])


# In[6]:


print(df.loc[10:13, ['country', 'lifeExp','gdpPercap']])


# In[7]:


df= pd.read_csv('C:/Users/andre/OneDrive/Escritorio/LenguajesProgramacion/DataAnalyticsPython/gapminder-FiveYearData.csv')


# In[ ]:





# In[8]:


print(df.loc[10:13, ['country', 'lifeExp']])


# In[ ]:





# In[11]:


df= pd.read_csv('C:/Users/andre/OneDrive/Escritorio/LenguajesProgramacion/DataAnalyticsPython/gapminder-FiveYearData.csv')


# In[10]:


datafile= pd.read_csv('C:/Users/andre/OneDrive/Escritorio/LenguajesProgramacion/DataAnalyticsPython/gapminder-FiveYearData.csv')


# In[ ]:





# In[ ]:





# In[12]:


print(df.groupby('year')['lifeExp'].mean())


# In[ ]:





# In[13]:


print(df.head(n=10))


# In[ ]:





# In[14]:


print(df.groupby('year')['lifeExp'].mean())


# In[ ]:





# In[15]:


print(df.groupby('country')['lifeExp'].mean())


# In[16]:


print(df.groupby('year' & 'country')['lifeExp'].mean())


# In[17]:


print(df.groupby('year')& df.groupby('country')['lifeExp'].mean())


# In[18]:


print(cls)


# In[ ]:





# In[19]:


print(df.groupby(['country','year'])\['lifeExp'].mean())


# In[21]:



print(df.groupby(['year','country'])['lifeExp'].mean())


# In[ ]:





# In[26]:


print(df.groupby(['year','country','lifeExp']).mean().head(n=60))


# In[ ]:





# In[27]:


print(df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean())


# In[36]:


x=df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()


# In[29]:



x


# In[ ]:





# In[31]:


x.plot()


# In[7]:



x=df.groupby(['year','continent'])['lifeExp'].mean()


# In[33]:


x


# In[34]:


X.PLOT()


# In[8]:


x.plot()


# In[38]:


x=df.groupby(['year'])[['lifeExp']].mean()


# In[10]:


x


# In[11]:


x.plot()


# In[ ]:





# In[ ]:





# In[ ]:




