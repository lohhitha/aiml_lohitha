#!/usr/bin/env python
# coding: utf-8

# In[7]:


def calculate_mean(values):
    if len(values) == 0:
        return None
        return int(values)/len(values)


# In[17]:


values = [1, 2, 3, 4, 5]
mean_value = calculate_mean(values)
print(mean_value)


# In[32]:


from collections import Counter

def find_mode(data):
    counter = Counter(data)
    mode = counter.most_common(1)[0][0]
    return mode
data = [1, 2, 2, 3, 3, 3, 4]
mode = find_mode(data)
print("Mode:", mode)


# In[60]:


def mode_value(L):
    s = set(L)
    d={}
    
    for x in s:
        d[x]=L.count(x)

    m = max(d.values())

    for k in d.keys():
        if d[k] == m:
            return k
        


# In[62]:


L = ["A","A","P","N","A","R","P","T"]
mode_value(L)


# In[ ]:




