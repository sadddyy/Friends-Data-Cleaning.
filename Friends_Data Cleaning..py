#!/usr/bin/env python
# coding: utf-8

# In[1]:


# "D:\friends - Sheet1.csv"

import pandas as pd


# In[2]:


# Read csv file into a Pandas DataFrame
df = pd.read_csv(r"D:\friends - Sheet1.csv")


# In[3]:


#displaying dataset before Cleaning
print("Before Data Cleaning")
print(df.head().to_markdown(index=False,numalign="left",stralign="left"))


# In[4]:


# Handle invalid values by converting them to NaN
df['height(cm)'] = df['height(cm)'].replace('xx', pd.NA)
df['height(cm)'] = df['height(cm)'].replace('0', pd.NA)
df['weight(kg)'] = df['weight(kg)'].replace('xx', pd.NA)
df['weight(kg)'] = df['weight(kg)'].replace('?', pd.NA)
df['spend_C'] = df['spend_C'].replace('xx', pd.NA)
df['weight(kg)'] = pd.to_numeric(df['weight(kg)'], errors='coerce')
df['height(cm)'] = pd.to_numeric(df['height(cm)'], errors='coerce')


# In[5]:


# Split 'age_sex' column into 'age' and 'sex'
df[['age', 'sex']] = df['age_sex'].str.split('_', expand=True)


# In[11]:


# Reorder the column labels
df = df[['fname', 'lname', 'age_sex', 'age', 'sex', 'section', 'height(cm)', 'weight(kg)', 'spend_A', 'spend_B', 'spend_C']]



# In[12]:


#displaying dataset before Cleaning
print("\nAfter Data Cleaning")
print(df.head().to_markdown(index=False,numalign="left",stralign="left"))


# In[ ]:




