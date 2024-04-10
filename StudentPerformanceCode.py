#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[6]:


ds = pd.read_csv('study_performance.csv')


# In[14]:


ds.count()


# In[15]:


ds.head(15)


# In[17]:


ds.tail(15)


# In[18]:


ds.info()


# In[20]:


ds = pd.read_csv('study_performance.csv', sep=',', header=None)
ds.to_csv('study_performance.csv', index_label='index')


# In[21]:


ds.head()


# In[22]:


ds.to_csv(r"/Users/asm/Desktop/prime energy all files/Kaggle Datasets")


# In[ ]:




