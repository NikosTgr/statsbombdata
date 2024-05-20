#!/usr/bin/env python
# coding: utf-8

# In[85]:


from statsbombpy import sb


# In[86]:


sb.competitions()


# In[87]:


sb.matches(competition_id=43,season_id=3)


# In[88]:


events=sb.events(match_id=8657)


# In[89]:


events.head()


# In[95]:


events.dropna(inplace=True)


# In[90]:


events.columns


# In[91]:


events=events[['team','type','minute','location', 'pass_end_location', 'player', 'pass_outcome' ]]
events = events[events['team'] == 'England']


# In[92]:


events.head()


# In[97]:


events.dropna(inplace=True)


# In[98]:


events.head()


# In[ ]:




