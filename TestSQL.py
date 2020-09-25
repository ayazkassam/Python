#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pyodbc as pyodbc


# In[4]:


import pandas as pd


# In[36]:


server = '.\MSSQLSERVER2017' 
database = 'capital' 
username = 'rouser' 
password = 'bha1934'


# In[38]:


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+ database +';UID='+username+';PWD='+ password)


# In[40]:


cursor = conn.cursor()

cursor.execute("SELECT * FROM [dbo].[t_capital_gross_net]") 
row = cursor.fetchone() 


# In[41]:


while row: 
    print("%s   %s" % (row[0], row[1]))
    row = cursor.fetchone()


# In[47]:


table_query="select gross_net_id, gross_net_alias from [dbo].[t_capital_gross_net] where gross_net_key=1"


# In[48]:


df = pd.read_sql(table_query,conn)


# In[53]:


print(df)


# In[54]:


print(df['gross_net_id'])


# In[55]:


gross_id = df['gross_net_id']


# In[57]:


print(gross_id);


# In[58]:


grs_alias= df['gross_net_alias'];


# In[59]:


print(grs_alias)


# In[ ]:




