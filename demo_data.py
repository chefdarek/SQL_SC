#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sqlite3


# In[9]:


conn = sqlite3.connect('demo_data.sqlite')


# In[10]:


cursor = conn.cursor()


# In[11]:


#Creat a new table for our data, specify type and null acceptance or not

cursor.execute('''CREATE TABLE demo
    (ID INT PRIMARY KEY NOT NULL,
     s           TEXT NOT NULL,
     x            INT NOT NULL,
     y            INT NOT NULL);''')
cursor.close()


# In[12]:


cursor = conn.cursor()


# In[14]:


cursor.execute("INSERT INTO demo (ID, s, x, y)                 VALUES (1, 'g', 3, 9)");
cursor.execute("INSERT INTO demo (ID, s, x, y)                 VALUES (2, 'v', 5, 7)");
cursor.execute("INSERT INTO demo (ID, s, x, y)                 VALUES (3,'f',8, 7)");
conn.commit() 


# In[31]:


cursor.execute("SELECT COUNT(*)FROM demo;");
print(f"The table has {cursor.fetchall()[0][0]} rows")


# In[33]:


cursor.execute("SELECT COUNT(*)FROM demo WHERE x >= 5 AND y >= 5;");
print(f"The table has {cursor.fetchall()[0][0]} rows where x and y are >= 5")


# In[36]:


cursor.execute("SELECT COUNT(DISTINCT y) FROM demo;");
print(f"The table has {cursor.fetchall()[0][0]} distinct y values")


# In[ ]:




