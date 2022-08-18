#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app = Flask(__name__)
#__ is reserved word 
#by default is __main__


# In[3]:


import joblib


# In[4]:


@app.route("/", methods=["GET","POST"])
#decorator: any function declared below will need to run this line first
def index():
    if request.method=="POST":
        #get entered value
        rates = float(request.form.get("rates")) #during the transmission from this to backend, the variable structure will be gone, so have to declare float again
        print(rates)
        
        #load and predict from the 2 files
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        
        return(render_template("index.html",result1=r1,result2=r2))
    else: #before pressing enter
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




