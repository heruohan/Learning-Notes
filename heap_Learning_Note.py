# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:16:51 2019

@author: hecongcong
"""



#堆的插入操作add实现：
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
    
    
                
    





