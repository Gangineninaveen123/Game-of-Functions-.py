#!/usr/bin/env python
# coding: utf-8

# In[1]:


def my_func(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
addition_of_my_func = my_func(8,2,3,0,7)
print('8+2+3+0+7 = ',addition_of_my_func)


# In[ ]:




