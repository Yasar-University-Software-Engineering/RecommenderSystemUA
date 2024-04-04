#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors


# In[2]:


df = pd.read_csv('data.csv', encoding="ISO-8859-1")


# In[3]:


df.head(10)


# In[4]:


## df = df.drop('InvoiceDate', axis=1)
LE=LabelEncoder()
df['CustomerID']=LE.fit_transform(df['CustomerID'])
df['StockCode']=LE.fit_transform(df['StockCode'])


# In[5]:


df


# In[6]:


train, test=train_test_split(df,test_size=0.2)
train


# In[7]:


no_of_rated_products_per_user =df.groupby(by='CustomerID')['Quantity'].count().sort_values(ascending=False)
no_of_rated_products_per_user.head(25)


# In[8]:


nearest_neighbors = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=5)


# In[9]:


nearest_neighbors


# In[10]:


nearest_neighbors.fit(train[['CustomerID','StockCode']])


# In[11]:


desired_order = ['CustomerID', 'StockCode', 'Quantity']  # Adjust as needed
df = df[desired_order]


# In[12]:


##unwanted_columns = ['Country', 'Description', 'InvoiceNo', 'UnitPrice']
##df = df.drop(unwanted_columns, axis=1)


# In[13]:


def recommendation_system_function(CustomerID, n_recommendation, nearest_neighbors):
    user_profile = df[df['CustomerID'] == CustomerID].drop('Quantity', axis=1)
    
    distances, indices = nearest_neighbors.kneighbors(user_profile)
    similar_users = indices.flatten()
    
    user_recommendations = []
    for user in similar_users:
        products_rated_by_user = df[df['CustomerID'] == user]
        product_list = products_rated_by_user['StockCode'].unique()
        user_recommendations.extend(product_list)
    unique_recommendations = list(set(user_recommendations))
        
    product_ratings_count = df[df['StockCode'].isin(unique_recommendations)]['StockCode'].value_counts()
    sorted_recommendations = product_ratings_count.sort_values(ascending=False)
    top_recommendations = sorted_recommendations.index[:n_recommendation]
    #recommended_product_codes = LE.inverse_transform(top_recommendations)
        
    #recommendation_table = pd.DataFrame({'StockCode' : top_recommendations, 'Product Code' : recommended_product_codes})
    recommendation_table = pd.DataFrame({'CustomerID':CustomerID,'StockCode' : top_recommendations})
    #recommendation_table['Rating Count'] = recommendation_table['StockCode'].map(product_ratings_count)
    recommendation_table.set_index('CustomerID', inplace = True)
    #print("\n_________________________\nRecommended Product:\n")
    #print(recommendation_table)
    #return recommended_product_codes
    return recommendation_table


# In[14]:


print(df[df['StockCode']=='3571']['CustomerID'])


# In[15]:


#CustomerID = 105
#num_recommendations = 3
#recommended_products = recommendation_system_function(CustomerID, num_recommendations, nearest_neighbors)


# In[ ]:

unique_CustomerID = df['CustomerID'].unique()
all_recommendation_tables = []
unique_CustomerID.size

# In[ ]:

for customer_id in unique_CustomerID:
    num_recommendations = 3
    recommended_products = recommendation_system_function(customer_id, num_recommendations, nearest_neighbors)
    all_recommendation_tables.append(recommended_products)

    print('-------------------\n')
    print(recommended_products)


# In[ ]:

final_recommendation_table = pd.concat(all_recommendation_tables)

final_recommendation_table