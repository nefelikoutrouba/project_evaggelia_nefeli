#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker # τα ticks στους άξονες
import numpy as np


# In[2]:


df=pd.read_excel('A0515_DKT87_TS_MM_01_1999_11_2022_06_F_GR.xls')


# In[3]:


# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)


# In[4]:


#df.tail(70)


# In[5]:


# εξαγωγή του 2020
df20=df.iloc[359:374]
df20.reset_index(inplace=True) # Επαναρίθμηση του index
df20


# In[6]:


df20=df20.drop(columns=['index']) # Πέταμα της στήλης index που περιήχε το παλιό ndex
cols=df20[1:2].values.tolist()[0] # Εξαγωγή των τιμών της γραμμής 1 ώστε να ονομαστούν οι στήλες
# Δημιουργία λίστας με τα labels για τις στήλες
n_cols=[]
for value in cols:
    n_cols.append(value.strip())
df20=df20.drop(labels=[0, 1], axis=0) # σβήσιμο των labels των στηλών
df20.columns=n_cols # μετονομασία στηλών
df20.reset_index(inplace=True)
df20=df20.drop(columns=['index'])
df20


# In[7]:


# αντιμετάθεση των γραμμών με τις στήλες
df20_t = df20.transpose()
df20_t


# In[8]:


cols=df20_t[0:1].values.tolist()[0] # Εξαγωγή των τιμών της γραμμής 0 ώστε να ονομαστούν οι στήλες
# Δημιουργία λίστας με τα labels για τις στήλες
n_cols=[]
for value in cols:
    n_cols.append(value)
df20_t=df20_t.drop(df20_t.index[0]) # σβήσιμο των labels των στηλών
df20_t.columns=n_cols # μετονομασία στηλών
df20_t


# In[9]:


# εξαγωγή του 2021
df21=df.iloc[376:391]
df21.reset_index(inplace=True) # Επαναρίθμηση του index
df21=df21.drop(columns=['index'])  # Πέταμα της στήλης index που περιήχε το παλιό ndex
cols=df21[1:2].values.tolist()[0]  # Εξαγωγή των τιμών της γραμμής 1 ώστε να ονομαστούν οι στήλες
# Δημιουργία λίστας με τα labels για τις στήλες
n_cols=[]
for value in cols:
    n_cols.append(value.strip())
df21=df21.drop(labels=[0, 1], axis=0) # σβήσιμο των labels των στηλών
df21.columns=n_cols # μετονομασία στηλών
df21.reset_index(inplace=True)
df21=df21.drop(columns=['index'])
df21


# In[10]:


# εξαγωγή του 2022
df22=df.iloc[393:]
df22.reset_index(inplace=True) # Επαναρίθμηση του index
df22=df22.drop(columns=['index'])  # Πέταμα της στήλης index που περιήχε το παλιό ndex
cols=df22[1:2].values.tolist()[0]  # Εξαγωγή των τιμών της γραμμής 1 ώστε να ονομαστούν οι στήλες
# Δημιουργία λίστας με τα labels για τις στήλες
n_cols=[]
for value in cols:
    n_cols.append(value.strip())
df22=df22.drop(labels=[0, 1], axis=0) # σβήσιμο των labels των στηλών
df22.columns=n_cols # μετονομασία στηλών
df22.reset_index(inplace=True)
df22=df22.drop(columns=['index'])
df22


# In[11]:


# γραφήματα για την κατηγορία Διατροφή και μη αλκοολούχα ποτά, ανα μήνα και έτος
data20=df20.iloc[0, 1:13]
data21=df21.iloc[0, 1:13]
data22=df22.iloc[0, 1:13]
plt.plot(data20)
plt.plot(data21)
plt.plot(data22)
plt.xlabel('Μήνες')
plt.ylabel('ΔΤΚ')
plt.legend(['2020', '2021', '2022'])
# plt.title('Διατροφή και μη αλκοολούχα ποτά')
plot_title = df20.iloc[0, 0:1].values[0].strip() # Εξαγωγή του τίτλου από το df
plt.title(plot_title)


# In[12]:


# γραφήματα για το γενικό δείκτη, ανα μήνα και έτος
data20=df20.iloc[12, 1:13]
data21=df21.iloc[12, 1:13]
data22=df22.iloc[12, 1:13]
plt.plot(data20)
plt.plot(data21)
plt.plot(data22)
plt.xlabel('Μήνες')
plt.ylabel('ΔΤΚ')
plt.legend(['2020', '2021', '2022'])
# plt.title('Γενικός Δείκτης')
plot_title = df20.iloc[-1, 0:1].values[0].strip() # EΕγαγωγή του τίτλου από το df
plt.title(plot_title)


# In[13]:


#γράφημα για όλες τις κατηγορίες 
for i in range(13):
    data20=df20.iloc[i, 1:13]
    data21=df21.iloc[i, 1:13]
    data22=df22.iloc[i, 1:13]
    plt.plot(data20, 'o-')
    plt.plot(data21, 'o-')
    plt.plot(data22, 'o-')
    plt.xlabel('Μήνες')
    plt.ylabel('ΔΤΚ')
    plt.legend(['2020', '2021', '2022'])
    plt.title(list(df20['Ομάδες αγαθών και υπηρεσιών'].values)[i])
    plt.savefig('Image_'+str(i+1)+'.png', dpi=300) #  αποθήκευση σε εικόνα (default=.png)
    plt.show() # reset ώστε κάθε διάγραμμα να είναι σε νέους άξονες


# In[28]:


# df20


# In[15]:


# Συγχώνευση df20, df21, df22
# Μετονομασία στηλών, να περιέχει την χρονολογία
# έτος 2020
df20a = df20
cols=list(df20[1:2].columns)
n_cols=[cols[0]]
for value in cols[1:]:
    n_cols.append(value+'20')
df20a.columns=n_cols
# έτος 2021
df21a = df21
cols=list(df21[1:2].columns)
n_cols=[cols[0]]
for value in cols[1:]:
    n_cols.append(value+'21')
df21a.columns=n_cols
# έτος 2022
df22a = df22
cols=list(df22[1:2].columns)
n_cols=[cols[0]]
for value in cols[1:]:
    n_cols.append(value+'22')
df22a.columns=n_cols
# ένωση df20a, df21a, df22a
df_mrg = pd.merge(df20a, df21a)
df_mrg = pd.merge(df_mrg, df22a)
df_mrg = df_mrg.drop(columns=['Μέσος20', 'Μέσος21', 'Μέσος22']) # Διαγραφή στηλών, δεν έχουν νόημα σ' αυτό το διάγραμμα


# In[16]:


df_mrg.head(3)


# In[17]:


# Δημιουργία ενός γραφήματος για τα έτη 2020,2021, 2022, όχι συγκριτικά, αλλά σε χρονολογική σειρά
titles=list(df_mrg['Ομάδες αγαθών και υπηρεσιών'].values)
titles=[title.strip().split(' ', 1)[1].strip() for title in titles]  # Αφαίρεση του αριθμού από τον τίτλο
for i in range(11):
    plt.figure(figsize=(12,5))
    data=df_mrg.iloc[i, 1:37]
    ax = plt.gca()
    plt.plot(data, 'o-')
    plt.xlabel('Μήνες')
    plt.ylabel('ΔΤΚ')
    plt.title(titles[i])
    xticks = ax.xaxis.get_major_ticks()
    every_nth = 3
    for n in range(len(xticks)):
        if n % every_nth != 0:
            xticks[n].set_visible(False)
    plt.tick_params(axis='x', labelrotation=30)
    for label in ax.get_xticklabels():
        label.set_horizontalalignment('center')
    plt.grid(axis='both', color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.savefig('Image_mrg_'+str(i+1)+'-A.png', dpi=300)
    plt.show()


# In[19]:


df_mrg_t = df_mrg.transpose() # αντιμετάθεση των γραμμών με τις στήλες
df_mrg_t


# In[20]:


cols=df_mrg_t[0:1].values.tolist()[0] # Εξαγωγή των τιμών της γραμμής 0 ώστε να ονομαστούν οι στήλες
# Δημιουργία λίστας με τα labels για τις στήλες
n_cols=[]
for value in cols:
    n_cols.append(value)
df_mrg_t=df_mrg_t.drop(df_mrg_t.index[0]) # σβήσιμο των labels των στηλών
df_mrg_t.columns=n_cols # μετονομασία στηλών
df_mrg_t


# In[21]:


df_pct = df_mrg_t.pct_change(periods=12, fill_method=None) # Δημιουργία του df με τα percentaces ανά 12-μηνο (έτος), αφήνοντας άδεια τα κενά


# In[22]:


df_pct.to_csv('pct.csv') # Εξαγωγή του df_pct


# In[23]:


df_pct


# In[24]:


#Line chart
categories = [0, 3, 4, 5] # Οι κατηγροίες που μας ενδιαφέρουν (τα indexes)
for cat in categories:
    data21=df_pct.iloc[12:24, cat] # φιλτράρισμα του έτους 2021
    index_21= list(data21.index) # εξαγωγή του index της ΣΕΙΡΑΣ data21 για να μετονομαστεί χωρίς το έτος
    for i in range(12):
        index_21[i] = index_21[i][:-2]
    data21.index = index_21 # Μετονομασία του index του data21
    data22=df_pct.iloc[24:36, cat] # φιλτράρισμα του έτους 2022
    index_22= list(data22.index)
    for i in range(12):
        index_22[i] = index_22[i][:-2]
    data22.index = index_22
    plt.plot(data21, 'o-')
    plt.plot(data22, 'o-')
    plt.xlabel('Μήνες')
    plt.ylabel('Μεταβολή (%) από έτος σε έτος ')
    plt.legend(['2021', '2022'])
    plt.title(list(df_pct.columns)[cat])
    plt.savefig('Image_pct_'+str(cat+1)+'.png', dpi=300) #  αποθήκευση σε εικόνα (default=.png)
    plt.show() # reset ώστε κάθε διάγραμμα να είναι σε νέους άξονες


# In[27]:


# Δημιουργία ραβδογραμμάτων
categories = [0, 3, 4, 5, 12] # Οι κατηγορίες που μας ενδιαφέρουν (τα indexes)
for cat in categories:
    data21=df_pct.iloc[12:24, cat] # φιλτράρισμα του έτους 2021
    index_21= list(data21.index) # εξαγωγή του index της ΣΕΙΡΑΣ data21 για να μετονομαστεί χωρίς το έτος
    for i in range(12):
        index_21[i] = index_21[i][:-2]
    data21.index = index_21 # Μετονομασία του index του data21
    data22=df_pct.iloc[24:36, cat] # φιλτράρισμα του έτους 2022
    index_22= list(data22.index)
    for i in range(12):
        index_22[i] = index_22[i][:-2]
    data22.index = index_22
    X = np.arange(12)
    plt.bar(X, data21.values, width=0.25) #πλάτος μπάρας
    plt.bar(X+0.25, data22.values, width=0.25)
    plt.xticks([r + 0.25 for r in range(12)],data21.index) #να μου τυπώσει τους μήνες όχι νούμερα
    plt.xlabel('Μήνες')
    plt.ylabel('Μεταβολή (%) από έτος σε έτος ')
    plt.legend(['2021', '2022'])
    plt.title(list(df_pct.columns)[cat])
    plt.savefig('Image_pct_BAR_'+str(cat+1)+'.png', dpi=300) #  αποθήκευση σε εικόνα (default=.png)
    plt.show() # reset ώστε κάθε διάγραμμα να είναι σε νέους άξονες


# In[ ]:




