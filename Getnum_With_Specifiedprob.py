# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 23:41:06 2019

@author: hecongcong
"""

'''
本知识点是以指定概率prob，随机返回序列lst中的一个元素.
Example:
Intput:lst=[1,2,3,4],prob=[0.1,0.2,0.3,0.4]
Output:int.

思路：本题是以指定概率随机从序列中返回一个元素，思路如下：
第一步：随机产生一个0到1之间的数字x,构建累积概率变量cur_prob.
第二步：进行循环，如下：
当x<0.1时，返回1.
当0.1<x<0.3时，返回2.
当0.3<x<0.6时，返回3.
当0.6<x<1时，返回4.
因为这四个区间反应了个元素对应的概率,同时x是以均匀分布随机生产的，所以能满足题意要求.
代码如下.
'''
def random_pick(lst,prob):
    import random
    x=random.uniform(0,1)
    cur_prob=0.0
    for item,item_prob in zip(lst,prob):
        cur_prob+=item_prob
        if(x<cur_prob):
            break
    return(item)



'''
进行测试,nums是进行测试的次数，次数越大越接近相应的概率.例如：
Exaple1:
Input:nums=1000,lst=[1,2,3,4],prob=[0.1,0.2,0.3,0.4];
Output:{1: 0.118, 2: 0.201, 3: 0.289, 4: 0.392}

Example2:
Input:nums=10000,lst=[1,2,3,4],prob=[0.1,0.2,0.3,0.4];
Output:{1: 0.1012, 2: 0.1921, 3: 0.3039, 4: 0.4028}
'''
def test_random(nums,lst,prob):
    dic=dict(zip(lst,[0]*len(lst)))
    for i in range(nums):
        res=random_pick(lst,prob)
        dic[res]+=1
    for item,val in dic.items():
        dic[item]=val/nums
    return(dic)
    
    











