# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 23:41:06 2019

@author: hecongcong
"""

def random_pick(lst,prob):
    import random
    x=random.uniform(0,1)
    cur_prob=0.0
    for item,item_prob in zip(lst,prob):
        cur_prob+=item_prob
        if(x<cur_prob):
            break
    return(item)




def test_random(nums,lst,prob):
    dic=dict(zip(lst,[0]*len(lst)))
    for i in range(nums):
        res=random_pick(lst,prob)
        dic[res]+=1
    for item,val in dic.items():
        dic[item]=val/nums
    return(dic)
    
    











