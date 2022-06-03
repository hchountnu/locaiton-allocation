#!/usr/bin/env python
# coding: utf-8

# # Python Locaiton Allocaiton by Enumerate

# 輸入資料
# C: cost 矩陣 row 為客戶, column 為 設施

# In[1]:


c = [[ 2, 3, 6, 7, 1],
     [ 0, 5, 8, 4,12],
     [11, 6,14, 5, 8],
     [19,18,21,16,13],
     [ 3, 9, 8, 7,10],
     [ 4, 7, 9, 6, 0]]

f =[12,5,3,7,9]


# ## 1-median 程式

# In[2]:


mp_1 = 9999
mp_1_site = 0
for j in range(len(c[0])):
     total = 0
     for i in range(len(c)):
         total += c[i][j]
     if total < mp_1:
         mp_1 = total
         mp_1_site = j


# 察看結果

# In[3]:


mp_1,mp_1_site


# ## 2-median程式
# 使用兩層的迴圈

# In[4]:


# 2-MP 
mp_2 = 9999
mp_2_site = [0,1]
for j1 in range(len(c[0])-1):
    for j2 in range(j1+1,len(c[0])):
          total = 0
          for i in range(len(c)):
              if c[i][j1] <= c[i][j2]:
                  total += c[i][j1]
              else:
                  total += c[i][j2]
          if total < mp_2:
              mp_2 = total
              mp_2_site = [j1,j2]


# 察看結果

# In[5]:


mp_2,mp_2_site


# ## 3-median程式
# 須要三層迴圈

# In[6]:


# 3-MP 使用 min()    
mp_3 = 9999
mp_3_site = [0,1,2]
for j1 in range(len(c[0])-2):
    for j2 in range(j1+1,len(c[0])-1):
        for j3 in range(j2+1,len(c[0])):
            total = 0
            for i in range(len(c)):
                total += min(c[i][j1],c[i][j2],c[i][j3])
            if total < mp_3:
                mp_3 = total
                mp_3_site = [j1,j2,j3]


# 察看結果

# In[7]:


mp_3,mp_3_site


# ## 生成所有組合的函數
# 用迴圈寫法，p-median 迴圈的次數為p，無法一般化。
# 須要一個能夠產生所有組合的方法。
# 輸入集合的元素個數後，下面函數先產生所有可能的子集的數字註標

# In[8]:


# 產生所有子集的函數

def powerset (n):
    subset = [[]]
    for i in range(n):
        subset_tmp = []
        for j in subset:
            tmp = j + [i]
            subset_tmp.append(tmp)
        subset += subset_tmp
    return subset


# 試用 powerset

# In[9]:


powerset(5)


# powerset 函數可以改的更為簡潔的 powerset2

# In[10]:


# 產生所有子集，較為簡潔的寫法

def powerset2 (n):
    subset = [[]]
    for i in range(n):
        subset_tmp = [j + [i] for j in subset]
        subset += subset_tmp
    return subset


# 利用powset產生所有子集後，選出指定的rank的子集，得到n選m的組合

# In[11]:


# 產生排列組合 n:所有數 m:選取數

def enmu (n,m):
    subset = [[]]
    for i in range(n):
        subset_tmp = [j + [i] for j in subset]
        subset += subset_tmp
    return [x for x in subset if len(x) == m]


# 試用 enmu()

# In[12]:


q2 = enmu(5,2)
q2


# In[13]:


q3 = enmu(5,3)
q3


# 使用 enum() 寫 p-median，比較emum() 所產生的組合,所有的p，都只需一個迴圈

# In[14]:


# 3-MP min()中參數個數為P

mp_3 = 9999
mp_3_site = [0,1,2]
for j in q3:
    total = 0
    for i in range(len(c)):
        total += min(c[i][j[0]],c[i][j[1]],c[i][j[2]])
    if total < mp_3:
        mp_3 = total
        mp_3_site = j


# 察看結果

# In[15]:


mp_3, mp_3_site


# 上面函數比較大小時，min()中的參數，因p而改變，需修改

# In[16]:


# p-MP，將 min() 一般化

mp_3 = 9999
mp_3_site = [0,1,2]
for j in q3:
    total = 0
    for i in range(len(c)):
        total += min([c[i][l] for l in j])
    if total < mp_3:
       mp_3 = total
       mp_3_site = j


# 察看結果

# In[17]:


mp_3, mp_3_site


# ## 通用p-median
# 將上述過程，改為一般化的p-median函數，輸入cost及p即可用窮舉法得到解答
# c 為 cost matrix, row 為客戶, column 為設施
# p ： 欲選出設施數

# In[18]:


# p-MP 一般化函數 
# c 為 cost matrix, row 為客戶, column 為設施
# p ： 欲選出設施數

def p_mp(c,p):
    m = len(c) 
    n = len(c[0])
    tc = sum ([sum(b) for b in c])
    q = enmu(n,p)
    site = []
    records= []
    for j in q:
        total = 0
        for i in range(m):
            total += min([c[i][l] for l in j])
        records.append({'site':j,'cost':total})
        if total < tc :
            tc = total
            site = j
    return {'selected_site': site, 'min_cost':tc, 'records':records }


# 試用 p-mp函數

# In[19]:


p_mp(c,2)


# ## p-center通用函數
# p-median 通用式，只要將比較各種組合的方式，改為比較各組合中最遠的元素。就可得到p-center的通用函數

# In[20]:


def p_cp(c,p):
    m = len(c) 
    n = len(c[0])
    minmaxc = max ([max(b) for b in c])
    q = enmu(n,p)
    site = []
    records= []
    for j in q:
        mc = []
        for i in range(m):
            mc.append(min([c[i][l] for l in j]))
        records.append({'site':j,'cost':max(mc)})
        if  max(mc) < minmaxc:
            minmaxc = max(mc)
            site = j
    return {'selected_site': site, 'min_cost':minmaxc, 'records':records}


# 試用 p_cp

# In[21]:


p_cp(c,2)


# ## 進一步改進的可能
# 如果在p_mp中增加一些選項，可以容易寫出更通用 p-location函數，但p-median 通用式，配合 hillsman editing，可能更為簡潔與通用。

# In[ ]:




