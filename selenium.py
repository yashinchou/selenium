#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install selenium


# In[2]:


import os


# In[4]:


os.getcwd()


# In[8]:


# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


# In[24]:


# !pip install pandas


# In[25]:


service = Service("./chromedriver.exe")


# In[26]:


driver = webdriver.Chrome()


# In[27]:


driver.get('https://www.wsj.com/market-data/quotes/AAPL?mod=searchresults_companyquotes')  # 更改網址以前往不同網頁


# In[28]:


driver.implicitly_wait(15)


# In[29]:


ul = driver.find_element(By.CLASS_NAME, "WSJTheme--cr_newsSummary--2RNDoLB9")


# In[30]:


lis = ul.find_elements(By.TAG_NAME, 'a')


# In[31]:


data = []


# In[32]:


list(lis)[0].text


# In[33]:


for li in lis:
    # 整理資料
    data.append({'title': li.text, 'url': li.get_attribute('href')})


# In[34]:


df = pd.DataFrame(data)


# In[35]:


df.to_csv("wsj.csv")


# In[36]:


print(df)


# In[37]:


driver.close() # 關閉瀏覽器視窗

