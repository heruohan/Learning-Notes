# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:16:51 2019

@author: hecongcong
"""



'''
堆：是一类特殊的树结构，堆的通用特点就是各个父节点大于或小于所有子节点。
最小推(min-heap)就是其中的每个节点都小于或者等于其两个子节点的一个二叉树，
其根节点的值最小。最大堆(max-heap)其根节点的值最大；

特点：
堆是一种经过排序的树形数据结构，每个节点都有一个值。通常我们所说的堆的
数据结构是指二叉树。堆的特点是根节点的值最小（或最大），且根节点的两个
树也是一个堆。由于堆的这个特性，常用来实现优先队列。

堆的各种操作时用数组来实现的，两个最为重要的堆操作是add和pop。

Note:
数组一个元素的父节点的位置索引的i，则其左右子节点的索引位置如下：
letf_idx=2*i+1
right_idx=2*i+2
堆的最顶端元素在数组种的位置索引为0;
'''




#堆的插入操作add实现(以最小堆为例)：
'''
add:接收一个可比较的元素作为参数，并且将该元素插入到堆中合适的位置,维护
堆的属性不变.
目标：在堆中找到新元素的合适位置，并且将其插入.
实现策略如下：
1.首先在堆的底部插入该元素，在数组实现中，这是数组中最后一个元素之后的位置.
2.然后，进入一个循环，只要新元素的值小于其父节点的值，循环就让这个新元素沿
着堆向上“走”,将新的元素和其父节点交换。当这个过程停止的时候(要么新的元素大于,
或等于其父节点，要么到达了顶部的节点),新的元素就位于其适当的位置。
代码如下；
'''

def heap_add(heaps,item):
    heaps.append(item)
    curpos=len(heaps)-1
    while(curpos>0):
        parentpos=(curpos-1)>>1
        parentItem=heaps[parentpos]
        if(parentItem<=item):
            break
        else:
            heaps[curpos]=parentItem
            curpos=parentpos
    heaps[curpos]=item
    




#堆的删除操作pop实现：
'''
pop:删除堆中最顶端的元素，并返回最顶端的元素，并且维护堆的属性.
目标：在删除根节点之后，返回该节点中的元素，并且调整其他节点的位置
以维护堆属性.
实现策略如下：
1.保持顶部元素topItem,同时将底部元素bottomItem删除，并将顶部元素替换为
bottomItem.
2.从堆的顶部往下走，求出其左右子节点种较小的元素minchild，与bottomItem
进行比较，如果minchild<bottomItem,则将minchild与bottomItem交换，不断
循环；直到minchild>bottomItem,或者到达了堆的底部，则停止循环；
代码如下；
'''

def heap_pop(heaps):
    if(len(heaps)==0):
        raise Exception('Heap is empty')
    topItem=heaps[0]
    bottomItem=heaps.pop()
    if(len(heaps)==0):
        return(bottomItem)
    heaps[0]=bottomItem
    lastIndex=len(heaps)-1
    curpos=0
    while(True):
        leftchild=2*curpos+1
        rightchild=2*curpos+2
        if(leftchild>lastIndex):
            break
        if(rightchild>lastIndex):
            minchild=leftchild
        else:
            leftItem=heaps[leftchild]
            rightItem=heaps[rightchild]
            if(leftItem<=rightItem):
                minchild=leftchild
            else:
                minchild=rightchild
        minItem=heaps[minchild]
        if(bottomItem<=minItem):
            break
        else:
            heaps[curpos]=minItem
            curpos=minchild
    heaps[curpos]=bottomItem
    return(topItem)
    
    
                
    





