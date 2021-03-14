#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-35)
engine.setProperty('voice', voices[7].id)
engine.save_to_file(txt , "/Users/arjunsingh/Recordings/narayan.mp3")
engine.runAndWait()

