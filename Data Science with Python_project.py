#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Import data into Python environment.
Comcast_telecom_complaints_data=pd.read_csv('Comcast_telecom_complaints_data.csv')


# In[4]:


Comcast_telecom_complaints_data.head()


# In[5]:


#Provide the trend chart for the number of complaints at monthly and daily granularity levels.
Comcast_telecom_complaints_data['Date_month_year'] = pd.to_datetime(Comcast_telecom_complaints_data['Date_month_year'])
Comcast_telecom_complaints_data['Created_Month'] =  Comcast_telecom_complaints_data['Date_month_year'].apply(lambda x: x.month)
Comcast_telecom_complaints_data['Created_Day'] = Comcast_telecom_complaints_data['Date_month_year'].apply(lambda x: x.day)


# In[6]:


Comcast_telecom_complaints_data.head(3)


# In[ ]:





# In[9]:


#number of complaints monthly
plt.figure(figsize=(8,4))
bymonth = Comcast_telecom_complaints_data.groupby('Created_Month').count().reset_index()
sns.lineplot(x='Created_Month', y= 'Customer Complaint', data = bymonth,color='g',linewidth=2) 


# In[10]:


#number of complaints Daily
plt.figure(figsize=(8,4))
byday = Comcast_telecom_complaints_data.groupby('Created_Day').count().reset_index()
sns.lineplot(x='Created_Day', y= 'Customer Complaint', data = byday, color = 'red',linewidth=2 )


# In[15]:


#Provide a table with the frequency of complaint types.
Comcast_telecom_complaints_data['Customer Complaint'].value_counts()


# In[94]:


#Which complaint types are maximum i.e., around internet, network issues, or across any other domain
Comcast_telecom_complaints_data['Customer Complaint'].describe


# In[16]:


#Create a new categorical variable with value as Open and Closed. Open & Pending is to be categorized as Open and Closed & Solved is to be categorized as Closed.


# In[17]:


Comcast_telecom_complaints_data['New_Cat_Var'] = ["Open" if Status=="Open" or Status=="Pending" else "Closed" for Status in Comcast_telecom_complaints_data["Status"]]


# In[18]:


Comcast_telecom_complaints_data


# In[34]:


#Provide state wise status of complaints in a stacked bar chart.
ST_COM=Comcast_telecom_complaints_data.groupby(['State','New_Cat_Var']).size().unstack().fillna(0)


# In[35]:


ST_COM


# In[48]:


ST_COM.plot(kind='barh',figsize=(7,7), stacked=True)


# In[46]:


#Which state has the maximum complaints
Comcast_telecom_complaints_data.groupby(["State"]).size().sort_values(ascending=False)


# In[62]:


Unres_com=Comcast_telecom_complaints_data.groupby(['State','New_Cat_Var']).size().unstack().fillna(0).sort_values('Open',axis=0,ascending=False)


# In[75]:


#Which state has the highest percentage of unresolved complaints
Unres_com['unresolved']=Unres_com['Open']/Unres_com['Open'].sum()*100
Unres_com['resolved']=Unres_com['Closed']/Unres_com['Closed'].sum()*100


# In[77]:


Unres_com.sort_values('unresolved',axis=0,ascending=False)[:10]


# In[80]:


#Provide the percentage of complaints resolved till date, which were received through the Internet and customercare calls.
PCT_COM=Comcast_telecom_complaints_data.groupby(['Received Via','New_Cat_Var']).size().unstack().fillna(0).sort_values('Open',axis=0,ascending=False)


# In[81]:


PCT_COM


# In[82]:


PCT_COM['resolved']=PCT_COM['Closed']/PCT_COM['Closed'].sum()*100


# In[84]:


PCT_COM['resolved'].sort_values(ascending=False)


# In[ ]:




