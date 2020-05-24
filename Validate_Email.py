#!/usr/bin/env python
# coding: utf-8

# In[108]:


import pandas as pd 
from validate_email import validate_email
import numpy as np
import re


# In[79]:



path='G:/pc_antiguo/Escritorio/UNAB/CIEI/Proyectos/Articulo_1/Data/.xls/'
file3='F3.xlsx'
file4='F4.xlsx'
file5='F5.xlsx'
file6='F6.xlsx'
file7='F7.xlsx'
file9='F9.xlsx'
output='emails.csv'
output_F6='Email_F6.csv'

F3 = pd.read_excel(path+file3)
F4 = pd.read_excel(path+file4)
F5 = pd.read_excel(path+file5)
F6 = pd.read_excel(path+file6)
F7 = pd.read_excel(path+file7)
F9 = pd.read_excel(path+file9)


# In[80]:


F3['forma']='F3'
F4['forma']='F4'
F5['forma']='F5'
F6['forma']='F6'
F7['forma']='F7'
F9['forma']='F9'


# In[81]:


F3=F3[['forma', 'Email']]
F4=F4[['forma', 'email']]
F5=F5[['forma', 'email']]
F6=F6[['forma', 'email']]
F7=F7[['forma', 'email']]
F3.rename(columns={'Email': 'email'}, inplace=True)


# In[83]:


emails = F3.append([F4,F5,F7])
emails


# In[3]:




def validate(x):
    if validate_email(email_address= x , check_regex=True, check_mx=True, from_address='my@from.addr.ess', helo_host='my.host.name', smtp_timeout=10, dns_timeout=10, use_blacklist=True)==True:
        x='Verificado'
    else: 
        x='Por verificar'
    return(x)

validate('x')
    


# In[89]:


# Filtrar bases
emails=emails[~emails['email'].isnull()]
emails=emails.reset_index(drop=True)
emails


# In[143]:


F6_['Validador']='ok'
for i in range(0,len(F6_)):
    F6_['Validador'][i]=validate(F6_['email'][i])


# In[95]:


for i in range(0,len(emails)):
    emails['Validador'][i]=validate(emails['Email'][i])


# In[19]:


F3[['Email','Validador']]


# In[20]:


validador=validate_email(email_address= 'maximanse61@gmail.com' , check_regex=True, check_mx=True, from_address='my@from.addr.ess', helo_host='my.host.name', smtp_timeout=10, dns_timeout=10, use_blacklist=True)
print(validador)


# In[ ]:


#Exportar
emails.to_csv(path+output, sep='\t')


# In[132]:


#Función check formato
exp_regular_correo='[^@]+@[^@]+\.[^@]+'

def check(email):
    if (re.search(exp_regular_correo,str(email))):
        a='Verificado'
    else:
        a='Por verificar'
    return(a)


# In[134]:


emails = pd.read_csv(path+output, sep='\t')


# In[130]:


for i in range(0,len(emails)):
    if emails['email'][i]=='Verificado':
        emails['email'][i]=check(emails['email'][i])
    else:
        emails['email'][i]=emails['email'][i]
    
    


# In[128]:


F2=emails[emails['Validador']=='Verificado']
porcentaje=len(F2)/len(emails)
porcentaje

