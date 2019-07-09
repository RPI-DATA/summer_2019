#!/usr/bin/env python
# coding: utf-8

# Initialize the OK tests to get started.

# In[4]:


from client.api.notebook import Notebook
ok = Notebook('lab02.ok')
_ = ok.auth(inline=True)


# **Submission**: This should be submitted in PDF format with Homework 2.  

# In[6]:


a=5*13*31+2
b=2**5-2**11-2**1
b=2018
new_year = max(a,b)
new_year


# Check your work by executing the next cell.

# In[7]:


_ = ok.grade('q11')


# **Question 2.1.** Yuri Gagarin was the first person to travel through outer space.  When he emerged from his capsule upon landing on Earth, he [reportedly](https://en.wikiquote.org/wiki/Yuri_Gagarin) had the following conversation with a woman and girl who saw the landing:
# 
#     The woman asked: "Can it be that you have come from outer space?"
#     Gagarin replied: "As a matter of fact, I have!"
# 
# The cell below contains unfinished code.  Fill in the `...`s so that it prints out this conversation *exactly* as it appears above.

# In[8]:


woman_asking = "The woman asked:"
woman_quote = '"Can it be that you have come from outer space?"'
gagarin_reply = 'Gagarin replied:'
gagarin_quote = '"As a matter of fact, I have!"'

print(woman_asking, woman_quote)
print(gagarin_reply, gagarin_quote)


# In[9]:


_ = ok.grade('q21')


# ## 2.1. String Methods

# Strings can be transformed using **methods**, which are functions that involve an existing string and some other arguments. One example is the `replace` method, which replaces all instances of some part of a string with some alternative. 
# 
# A method is invoked on a string by placing a `.` after the string value, then the name of the method, and finally parentheses containing the arguments. Here's a sketch, where the `<` and `>` symbols aren't part of the syntax; they just mark the boundaries of sub-expressions.
# 
#     <expression that evaluates to a string>.<method name>(<argument>, <argument>, ...)
# 
# Try to predict the output of these examples, then execute them.

# In[11]:


# Replace one letter
'Hello'.replace('o', 'a')


# In[12]:


# Replace a sequence of letters, which appears twice
'hitchhiker'.replace('hi', 'ma')


# Once a name is bound to a string value, methods can be invoked on that name as well. The name is still bound to the original string, so a new name is needed to capture the result. 

# In[13]:


sharp = 'edged'
hot = sharp.replace('ed', 'ma')
print('sharp:', sharp)
print('hot:', hot)


# You can call functions on the results of other functions.  For example,
# 
#     max(abs(-5), abs(3))
# 
# has value 5.  Similarly, you can invoke methods on the results of other method (or function) calls.

# In[14]:


# Calling replace on the output of another call to
# replace
'train'.replace('t', 'ing').replace('in', 'de')


# Here's a picture of how Python evaluates a "chained" method call like that:
# 
# <img src="chaining_method_calls.jpg"/>

# **Question 2.1.1.** Assign strings to the names `you` and `this` so that the final expression evaluates to a 10-letter English word with three double letters in a row.
# 
# *Hint:* After you guess at some values for `you` and `this`, it's helpful to see the value of the variable `the`.  Try printing the value of `the` by adding a line like this:
#     
#     print(the)
# 
# *Hint 2:* Run the tests if you're stuck.  They'll often give you help.

# In[9]:


you = "kkeep"
this = "boo"
a = 'beeper'
the = a.replace('p', you) 
the.replace('bee', this)
#repeekkoob


# In[10]:


_ = ok.grade('q211')

# get_ipython().run_line_magic('matplotlib', 'inline')
import grade

# import importlib
# importlib.reload(grade)
ok = Notebook('final.ok')
name = "test"
points_per_test = 2.5
comments = ""

# In[15]:


grade.grade(name, points_per_test, comments, ok)
# In[ ]:




