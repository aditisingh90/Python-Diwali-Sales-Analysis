#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[5]:


diwali = pd.read_csv("Diwali Sales Data.csv", encoding='unicode_escape')


# In[6]:


diwali.head()


# In[27]:


diwali.describe()


# In[7]:


diwali.shape


# In[16]:


diwali.info()


# In[19]:


pd.isnull(diwali).sum()


# In[20]:


diwali.dropna(inplace=True)


# In[22]:


pd.isnull(diwali).sum()


# In[23]:


diwali['Amount']=diwali['Amount'].astype('int')


# In[26]:


diwali['Amount'].dtype


# ## Exploratory Data Analysis

# ### Gender

# In[28]:


diwali.info()


# In[29]:


ax= sns.countplot(x='Gender',data= diwali)
for bars in ax.containers:
    ax.bar_label(bars)


# In[37]:


diwali.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=True)


# In[55]:


gender_sales = diwali.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=True)

sns.barplot(x='Gender',y='Amount' , data = gender_sales)


# ### Age

# In[39]:


diwali.info()


# In[41]:


age_s = sns.countplot(data = diwali,x='Age Group')
for bars in age_s.containers:
    age_s.bar_label(bars)


# In[42]:


age_s = sns.countplot(data = diwali,x='Age Group', hue= 'Gender')
for bars in age_s.containers:
    age_s.bar_label(bars)


# In[44]:


gender_sales = diwali.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=True)

sns.barplot(x='Age Group',y='Amount' , data = gender_sales)


# In[56]:


state_sales = diwali.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(30,10)})
sns.barplot(x='State',y='Orders' , data = state_sales)


# In[57]:


state_sales = diwali.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(30,10)})
sns.barplot(x='State',y='Amount' , data = state_sales)


# #### From above geaph we can draw coclusion that more orders are from Himachal Pradesh and Kerala but the amount spent is more in Himachal Pradesh and Haryana.

# ### Marital Status

# In[61]:


age_s = sns.countplot(data = diwali,x='Marital_Status', hue= 'Gender')
sns.set(rc={'figure.figsize':(12,1)})
for bars in age_s.containers:
    age_s.bar_label(bars)
    
    


# In[67]:


state_sales = diwali.groupby(['Marital_Status'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(8,7)})
sns.barplot(x='Marital_Status',y='Amount' , data = state_sales)


# #### From above graphs we can see that most of the buyers are married females.

# ### Occupation

# In[72]:


age_s = sns.countplot(data = diwali,x='Occupation')
sns.set(rc={'figure.figsize':(20,5)})
for bars in age_s.containers:
    age_s.bar_label(bars)


# In[75]:


state_sales = diwali.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(12,5)})
sns.barplot(x='Occupation',y='Amount' , data = state_sales)


# ##### From above graphs we can see that most buyers work in IT Sector, Healthcare and Aviation Sector.

# ### Product Category

# In[79]:


age_s = sns.countplot(data = diwali,x='Product_Category')
sns.set(rc={'figure.figsize':(37,10)})
for bars in age_s.containers:
    age_s.bar_label(bars)


# In[81]:


state_sales = diwali.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Product_Category',y='Amount' , data = state_sales)


# #### From above graphs we can see that most products are are from Food , Cothing and Electronics category.

# In[82]:


state_sales = diwali.groupby(['Product_ID'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Product_ID',y='Amount' , data = state_sales)


# In[83]:


state_sales = diwali.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x='Product_ID',y='Orders' , data = state_sales)


# ### Conclusion

# Married females age group 26-35 years from UP, Maharashtra and Karnataka working in IT and Healthcare Sector are more likely to buy products from Food, Clothing and Electronic Category.

# In[ ]:




