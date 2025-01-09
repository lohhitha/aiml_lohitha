#!/usr/bin/env python
# coding: utf-8

# In[3]:


greet = lambda name : print(f"Good Morning {name}!")


# In[5]:


greet("Soumya")


# In[9]:


product =  lambda a,b,c : a*b*c


# In[11]:


product(20,30,40)


# In[19]:


even = lambda L :[x for x in L if x%2 == 0]


# In[21]:


my_list = [100,3,9,38,43,56,20]
even(my_list)


# In[17]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter +1
        sum += x
        mean = sum/counter
        return mean


# In[45]:


def product(*n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result


# In[47]:


product (2,9,8)


# In[ ]:





# In[ ]:




