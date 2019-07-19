#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sqlite3


# In[37]:


conn = sqlite3.connect('northwind_small.sqlite3')


# In[38]:


cursor = conn.cursor()


# In[40]:


cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()


# In[42]:


cursor.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()


# In[74]:


print("The TOP 10 products by max Unit Price are:")
price = cursor.execute("SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC limit 10").fetchall()
price


# In[78]:


cursor.execute("SELECT AVG(HireDate - BirthDate) FROM Employee;");
print(f"The Average age of employee hire is {cursor.fetchall()[0][0]} years")


# In[89]:


cursor.execute("SELECT City, AVG(HireDate - BirthDate) FROM Employee GROUP BY CITY ;");
print(f"The Average age of employee hire by city is {cursor.fetchall()} ")


# # Part 3

# Using sqlite3 in northwind.py, answer the following:
# 
#     What are the ten most expensive items (per unit price) in the database and their suppliers?
#     What is the largest category (by number of unique products in it)?
#     (Stretch) Who's the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.
# 

# In[91]:


print("The TOP 10 products and Supplier by max Unit Price are:")
price = cursor.execute("SELECT CompanyName, ProductName, UnitPrice FROM Product JOIN Supplier ON Product.SupplierId = Supplier.Id ORDER BY UnitPrice DESC limit 10").fetchall()
price


# In[120]:


top =cursor.execute("SELECT CategoryName, COUNT(CategoryId) AS MOST_FREQUENT FROM Product JOIN Category ON Product.CategoryId = Category.Id GROUP BY CategoryName ORDER BY COUNT(CategoryName) DESC").fetchall()
top
print(f"The largest category by number of unique items in it is {top[0][0]}")


# # Part 4
# Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job):
# 
#     In the Northwind database, what is the type of relationship between the Employee and Territory tables?
#     What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
#     What is "NewSQL", and what is it trying to achieve?
# 

# In[ ]:


The Employee and Territory tables are associated with a "One to One" relationship whereby
the tables only share one unique key value between both. Territory ID is the associative 
key present in both tabes, thereby linking them together.

A document store is appropriate in a variety of hardware restrictive or agile development
scenarios where speed and resources are paramount. Startups benefit by the flexibility to 
scale on demand, multiple mixed file format functionality as well as the 
speed to deploy since they do not need complicated schema. This however would not be
appropriate if the information or data was highly relational or 
associative and the need for structured, referencing tables were important to the project.

NewSQL is an attempt to the bridge the divide of NoSql and traditional Sql. 
NewSQL is a new approach to relational databases that wants to combine transactional
ACID (atomicity, consistency, isolation, durability)guarantees of good RDBMSs
and the horizontal scalability of NoSQL.

