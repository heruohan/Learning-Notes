# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 23:23:36 2019

@author: hecongcong
"""

'''
蓄水池抽样算法:实现代码及测试代码
时间复杂度为O(n).
'''



###################################当k=1时：
#实现代码
def reservoir_sample_1(lst):
    import random
    res=lst[0]
    idx=1
    while(True):
        try:
            j=random.randint(0,idx)
            if(j==0):
                res=lst[idx]
            idx+=1
        except IndexError:
            break
    return(res)
    

#测试代码
def test_1(lst,nums):
    dic=dict(zip(lst,[0]*len(lst)))
    for _ in range(nums):
        res=reservoir_sample(lst)
        dic[res]+=1
    for idx,value in dic.items():
        dic[idx]=value/nums
    return(dic)
    
'''
Example:
Input:lst=[1,2,3,4],nums=10000
Output:{1: 0.2523, 2: 0.2515, 3: 0.2479, 4: 0.2483}
'''






##################################当k!=1时：
def reservoir_sample_k(lst,k):
    import random
    res=lst[:k]
    idx=k
    while(True):
        try:
            j=random.randint(0,idx)
            if(0<=j<=k-1):
                res[j]=lst[idx]
            idx+=1
        except IndexError:
            break
    return(res)


def test_k(lst,k,nums):
    import collections
    dic=collections.defaultdict(int)
    for _ in range(nums):
        res=reservoir_sample_k(lst,k)
        for i in res:
            dic[i]+=1
    for idx,val in dic.items():
        dic[idx]=val/nums
    return(dic)


'''
Example:
Input:lst=[1,2,3,4,5,6],k=2,nums=10000
Output:
defaultdict(int,
{1: 0.3388, 2: 0.3338, 3: 0.3335, 4: 0.3331, 5: 0.3286, 6: 0.3322})
'''
    









