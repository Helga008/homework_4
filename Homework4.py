#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import matplotlib as mpl
print(mpl.get_cachedir())


# In[3]:


import matplotlib.pyplot as plt


# ## Задача 1
# 
# Постройте график
# 
# Назовите график
# 
# Сделайте именование оси x и оси y
# 
# Сделайте выводы
# 
# 
# 1.1. Скачать следующие данные: kc-house-data и laptop_price
# 
# 1.2. Изучите стоимости недвижимости
# 
# 1.3. Изучите распределение квадратуры жилой
# 
# 1.4. Изучите распределение года постройки

# In[5]:


df = pd.read_csv("kc-house-data.csv", sep = ',', encoding='windows-1251')
df.head()


# In[6]:


df.info()


# In[8]:


# 1.2. Изучите стоимости недвижимости
plt.figure(figsize=(6,4))
plt.hist(df['price'])
plt.title("График")
plt.xlabel("Стоимость")
plt.ylabel("Количество")
plt.xticks(rotation=20)


# Вывод: больше всего домов стоимостью до 0.8 млн. Меньше всего - от 2,3 до 3,1 млн

# In[9]:


# 1.3. Изучите распределение квадратуры жилой
data1=df['sqft_living'].value_counts()
data1


# In[12]:


plt.figure(figsize=(6,4))
plt.hist(data1)
plt.title("График")
plt.xlabel("Жилая площадь")
plt.ylabel("Количество")
plt.xticks(rotation=20)


# Вывод: Большая часть домов имеет жилую площадь от 0.1 до 13, меньше всего домов с большой жилой площадью - выше 123

# In[13]:


# 1.4. Изучите распределение года постройки
plt.hist(
    df['yr_built'],
    bins=range(df['yr_built'].min(), df['yr_built'].max() + 1)
)
plt.xlabel("Год постройки")
plt.ylabel("Кол-во домов, построенных за год");


# Вывод: основная тенденция - рост строительства домов в год. Однако за период происходили резкие спады, очевидно из-за экономической и политической ситуации - например, в 1930 - 1938годы. Пик строительства пришелся на 2018 год

# ## 2 задача
# 
# 2.1. Изучите распределение домов от наличия вида на набережную
# 
# Постройте график
# 
# Сделайте выводы
# 
# 2.2. Изучите распределение этажей домов
# 
# 2.3. Изучите распределение состояния домов
# 

# In[15]:


# 2.1
data2 = df['waterfront'].value_counts()
plt.figure(figsize=(6, 4))
plt.pie(data2, autopct='%1.1f%%')
plt.legend(['no', 'yes']);


# Вывод: вид на набережную есть только в 0.8% домов

# In[17]:


# 2.2. Изучите распределение этажей домов
data3 = df['floors'].value_counts()
plt.figure(figsize=(6, 4))
plt.pie(data3, autopct='%1.1f%%', labels=data3.index)


# Вывод: почти половина (49.4%) домов имеют 1 этаж, на втором месте (38.1%) - 2 этажа

# In[19]:


# 2.3. Изучите распределение состояния домов
data4 = df['condition'].value_counts()
plt.figure(figsize=(6, 4))
plt.pie(data4, autopct='%1.1f%%', labels=data4.index)


# Вывод: Оценка состояния большей части домов (64.9%)равна 3. На втором месте (26.3%) имеют оценку 4.

# ## 3 задача
# 
# Исследуйте, какие характеристики недвижимости влияют на стоимость недвижимости, с применением не менее 5 диаграмм из урока.
# 
# Анализ сделайте в формате storytelling: дополнить каждый график письменными выводами и наблюдениями.

# In[24]:


import seaborn as sns


# In[ ]:


# Зависимость цены от жилой площади:


# In[23]:


sns.jointplot(x=df['sqft_living'], y=df['price'], kind='reg')

plt.xlabel("Жилая площадь, кв. м")
plt.ylabel("Цена дома, млн");


# Вывод: Наблюдаем высокую зависимость цены от жилой площади, Чем дешевле жилье, тем зависимость сильнее. Меньшая зависимость цены от жилой площади более дорогих домов связана с влиянием других факторов, на которые ориентируются покупатели

# In[28]:


def Format (col1, col2, df):
    data = df.groupby(col1) \
        .agg({col2: 'mean'}) \
        .sort_index().reset_index()
    
    data[col1] = data[col1].apply(
        lambda val:
            str(val) 
    )

    return data


# In[26]:


# Зависимость цены от состояния дома:


# In[30]:


data5 = Format('condition', 'price', df)

plt.bar(
    data5['condition'],
    data5['price']
)

plt.title("Зависимость цены от состояния дома")
plt.xlabel("Оценка состояния дома")
plt.ylabel("Средняя цена дома");


# Самые дорогие дома - с высокой оценкой 5. В целом, оценка влияет на стоимость - прямая зависимость

# In[32]:


data6 = Format('view', 'price', df)

plt.bar(
    data6['view'],
    data6['price']
)

plt.title("Зависимость цены от вида")
plt.xlabel("Рейтинг вида")
plt.ylabel("Средняя цена дома");


# Вывод: Чем выше рейтинг вида, тем выше стоимость. 

# In[35]:


data7 = Format('bedrooms', 'price', df)

plt.bar(
    data7['bedrooms'],
    data7['price']
)

plt.title("Зависимость цены от количества спален")
plt.xlabel("Кол-во спален")
plt.ylabel("Средняя цена дома");


# Вывод: Самые дорогие дома с 8-ю спальнями. В целом для домов с 1-8 спальнями прослеживается равномерный рост цены. Дома без спален стоят выше из-за влияния других особенностей (хороший вид, рейтинг и тд). Дома с 9-33 спальнями, скорее всего, отличаются более простыми условиями, т.к. предназначены для больших семей.

# In[ ]:




