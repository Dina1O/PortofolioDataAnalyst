#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[12]:


data = pd.read_csv('udemy_courses.csv', parse_dates=['published_timestamp'])
print(data)


# In[14]:


data.dtypes


# # 1). 10 Data teratas

# In[16]:


data.head(10)


# # 2). 5 Data terbawah

# In[18]:


data.tail()


# # 3). Jumlah Baris Dan Jumlah Kolom

# In[19]:


data.shape

print('Jumlah baris: ', data.shape[0])
print('Jumlah kolom: ', data.shape[1])


# # 4). Informasi mengenai Dataset seperti Tipe Data Setiap Kolom Dan Kebutuhan Memori dan deskripsi (min, max, std, mean, dan lain-lain) pada tiap kolom

# In[20]:


data.info()


# In[135]:


data.describe()


# # 5). Memeriksa Nilai Null Dalam Dataset

# In[25]:


print('Nilai null: ', data.isnull().values.any())


# In[28]:


data.isnull()


# In[27]:


data.isnull().sum()


# In[29]:


sns.heatmap(data.isnull())


# # 6). Cek duplikat kemudian dibuang

# In[30]:


duplikat = data.duplicated().any()
print('data duplikat: ', duplikat)


# In[132]:


data.drop_duplicates()


# # 7). Jumlah Mata Kuliah Per Mata Pelajaran

# In[47]:


data['subject'].value_counts()


# In[54]:


# sns.countplot(data['subject'])
# plt.xlabel('Mata Pelajaran', fontsize=13)
# plt.ylabel('Jumlah kursus per Mata Pelajaran', fontsize=13)
# plt.xticks(rotation=60)
# plt.show()

sns.countplot(data=data, x='subject')
plt.xlabel('Mata Pelajaran', fontsize=13)
plt.ylabel('Jumlah kursus per Mata Pelajaran', fontsize=13)
plt.xticks(rotation=60)
plt.show()


# # 8).  Untuk Tingkat Mana, Kursus Udemy Menyediakan Kursus

# In[55]:


data['level'].value_counts()


# In[57]:


sns.countplot(data=data, x='level')
plt.xlabel('Level/tingkatan', fontsize=13)
plt.ylabel('Jumlah kursus per Tingkatan/level', fontsize=13)
plt.xticks(rotation=60)
plt.show()


# # 9). Jumlah Kursus Berbayar dan Gratis 

# In[58]:


data['is_paid'].value_counts()


# In[60]:


sns.countplot(data=data, x='is_paid')
plt.xlabel('Berbayar', fontsize=13)
plt.ylabel('Jumlah kursus berbayar', fontsize=13)
plt.xticks(rotation=60)
plt.show()


# # 10).  Level Mana yang Memiliki Jumlah Pelanggan Tertinggi

# In[87]:


sns.barplot(x='level', y='num_subscribers', data=data)
plt.xticks(rotation=60)
plt.show()


# # 11). Judul Kursus Paling Populer

# In[95]:


data[data['num_subscribers'].max() == data['num_subscribers']]

# data[data['num_subscribers'].max() == data['num_subscribers']]['course_title']


# # 12). 10 Kursus Terpopuler Sesuai Jumlah Pelanggan

# In[100]:


data.sort_values(by='num_subscribers', ascending=False).head(10)


# In[101]:


top_10 = data.sort_values(by='num_subscribers', ascending=False).head(10)


# In[102]:


sns.barplot(x='num_subscribers', y='course_title', data=top_10)


# # 13). Kursus yang Memiliki Jumlah Ulasan Tertinggi.

# In[104]:


plt.figure(figsize=(10, 4))
sns.barplot(x='subject', y='num_reviews', data=data)


# # 14). Apakah Harga Mempengaruhi Jumlah Ulasan?

# In[110]:


plt.figure(figsize=(13,8))
sns.scatterplot(x='price', y='num_reviews', data=data)


# # 15). Jumlah Total Kursus Yang Terkait Dengan Python

# In[111]:


data[data['course_title'].str.contains('Python', case=False)]


# In[114]:


kursus_python=len(data[data['course_title'].str.contains('Python', case=False)])
print('Banyaknya kursus yang terkait dengan python: ', kursus_python)


# # 16). 10 Kursus Python Paling Populer Sesuai Jumlah Pelanggan

# In[117]:


data[data['course_title'].str.contains('Python', case=False)].sort_values(by='num_subscribers', ascending=False).head(10)


# In[118]:


python = data[data['course_title'].str.contains('Python', case=False)].sort_values(by='num_subscribers', ascending=False).head(10)


# In[119]:


sns.barplot(x='num_subscribers', y='course_title', data=python)


# # 17). Tahun yang Jumlah Kursus Tertinggi Diposting

# In[120]:


data['Year'] = data['published_timestamp'].dt.year


# In[122]:


data.head(5)


# In[126]:


sns.countplot(x='Year', data=data)


# # 18). Jumlah Mata Pelajaran yang Diposkan Berdasarkan Kategori [Tahun]

# In[127]:


data.groupby('Year')['subject'].value_counts()

