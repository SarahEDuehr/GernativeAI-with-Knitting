#!/usr/bin/env python
# coding: utf-8

# In[11]:


#!pip install tika
# import parser object from tike
from tika import parser  
  
# opening pdf file
parsed_pdf = parser.from_file("C:\\Users\\girlg\\Documents\\IT 496\\01323874.pdf")
  
# saving content of pdf
# you can also bring text only, by parsed_pdf['text'] 
# parsed_pdf['content'] returns string 
data = parsed_pdf['content'] 
  
# Printing of content 
print(data)
  
# <class 'str'>
print(type(data))


# In[ ]:


from tika import parser
import sys
import os
def convert_pdfs(path: str) -> bool:
    
    parsed_pdf = parser.from_file(path)
    data = parsed_pdf['content'] 
    
    file = open(r'C:\Users\girlg\Downloads\Ravelry\pattern_text.txt', 'a', encoding="utf-8")
    sys.stdout = file
    print(data)
    file.close()

    
convert_pdfs(r'C:\Users\girlg\IT496 -- Ravelry Project\00003472.pdf')
    
#cwd = os.getcwd() 

#files = os.listdir(cwd)    
#for i in files:
#    try:
#        result = convert_pdfs(i)
#        print(result)
#    except Exception as e:
#        print('Exception in convert_pdfs():', e)


# In[ ]:


cwd = os.getcwd() 

files = os.listdir(cwd)
print(files)

