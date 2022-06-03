# 區位分析選址課程範例資料
使用python開發以窮舉法求解p-median問題及p-center問題
cost matrix 資料採用list, 每一需求為一個list，作為cost matirx的元素。 
先使用迴圈解1-median, 2-median，3-medain。
其次發展一般式
* 所有子集的函數 poserset(n) n: 集合的個數，return list of 子集(list)
* 應用poserset，製作組合函數 enum(n,m) n取m的組合 return list of 子集(list), 元素均為3個
* 迴圈過enum的回傳子集，產生p-median及p-center的解。

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hchountnu/locaiton-allocation/HEAD)
