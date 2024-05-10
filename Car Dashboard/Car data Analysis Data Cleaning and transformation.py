#!/usr/bin/env python
# coding: utf-8

# ## Car data Analysis Data Cleaning and transformation
# #### Project by Mayur Borgude

# In[66]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[50]:


# reading CSV as dataframes
df = pd.read_csv(r"https://raw.githubusercontent.com/Mayborg121/Car_DataAnalysis_Dashboard/main/Car%20Dashboard/src/Raw/cars_data_raw.csv")
df


# - listing the cloumns to analyze the data

# In[51]:


attributes_list = list(df)
print(attributes_list)


# In[52]:


print(attributes_list.index("feature_0"))


# In[53]:


print(attributes_list.index("feature_9"))


# - removing multiple columns at time.

# In[54]:


df = df.drop("engine_type", axis = 1)
df


# - Checking for NuLL values in dataset.

# In[55]:


df.isnull().sum()


# 

# In[ ]:





# In[57]:


manufacturer_list = df['manufacturer_name'].value_counts()
print(manufacturer_list,len(manufacturer_list))


# In[45]:


# variable to hold the count
cnt = 0
 
# list to hold visited values
visited = []
 
# loop for counting the unique
# values in height
for i in range(0, len(df['manufacturer_name'])):
 
    if df['manufacturer_name'][i] not in visited:
 
        visited.append(df['manufacturer_name'][i])
 
        cnt += 1

print("unique values :",visited, len(visited))


# In[58]:


x = visited  # X-axis points
y = df['manufacturer_name'].value_counts()              # Y-axis points

plt.plot(x, y)             # Plot the chart
plt.xlabel("X-axis")       # Add X-axis label
plt.ylabel("Y-axis")       # Add Y-axis label
plt.title("Simple Line Plot")  # Add title
plt.show()                 # Display the plot


# In[ ]:





# In[64]:


plt.style.use('_mpl-gallery')

# make data
x = np.arange(0, 10, 2)
ay = [1, 1.25, 2, 2.75, 3]
by = [1, 1, 1, 1, 1]
cy = [2, 1, 2, 1, 2]
y = np.vstack([ay, by, cy])

# plot
fig, ax = plt.subplots()

ax.stackplot(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()


# - Exporting the clean data into .CSV file

# In[59]:


export_csv_data = df.to_csv('cars_data.csv', index = True)
print('\nCSV String:\n', export_csv_data)

