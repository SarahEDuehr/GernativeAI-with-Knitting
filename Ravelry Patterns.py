#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas
df = pandas.read_csv('C:\\Users\\girlg\\Documents\\IT 496\\pdfs.csv')
print(df)


# In[3]:


df['path1'] = r'C:\\Users\\girlg\\Downloads\\Ravelry\\'
df['path3'] = '.pdf'


# In[4]:


df['path'] = df['path1'].str.cat(df['id'].astype(str).str.zfill(8))
df['paths'] = df['path'].str.cat(df['path3'])


# In[5]:


inputs = zip(df['paths'], df['pdf_url'])
urls = df['pdf_url']
fns = df['paths']


# In[6]:


import time
import requests
""""
def download_url(args):
    t0 = time.time()
    url, fn = args[0], args[1]
    try:
        r = requests.get(url)
        with open(fn, 'wb') as f:
            f.write(r.content)
        return(url, time.time() - t0)
    except Exception as e:
        print('Exception in download_url():', e)

t0 = time.time()
for i in inputs:
    result = download_url(i)
    print('url:', result[0], 'time:', result[1])
print('Total time:', time.time() - t0)
"""


# In[11]:


import os
import time
from time import sleep
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=0, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)





def download_pdf_file(args) -> bool:
    """Download PDF from given URL to local directory.

    :param url: The url of the PDF file to be downloaded
    :return: True if PDF file was successfully downloaded, otherwise False.
    """
 
    fn, url = args[0], args[1]
    # Request URL and get response object
    response = session.get(url)

    # isolate PDF filename from URL
   
    if response.status_code == 200:
        # Save in current working directory
       
        with open(fn, 'wb') as pdf_object:
            pdf_object.write(response.content)
            print(f'{url} was successfully saved!')
            return True
    else:
        print(f'Uh oh! Could not download {url},')
        print(f'HTTP response status code: {response.status_code}')
        return False
    
t0 = time.time()
for i in inputs:
    try:
        result = download_pdf_file(i)
        print(result)
        sleep(3)
    except Exception as e:
        print('Exception in download_url():', e)
print('Total time:', time.time() - t0)


# In[12]:




