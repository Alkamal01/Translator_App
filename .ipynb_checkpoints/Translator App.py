#!/usr/bin/env python
# coding: utf-8

# In[1]:


from googletrans import Translator



def translate(text, dest='en'):
    """
    Translates given text to the given destination language code
    """
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest=dest)
    return translation.text


# In[2]:


# Translate 'Hello, world!' to Spanish
print(translate('Hello, world!', 'es'))

# Translate 'Bonjour le monde!' to English
print(translate('Bonjour le monde!', 'en'))


# In[ ]:




