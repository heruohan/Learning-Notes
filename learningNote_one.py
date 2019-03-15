# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 23:57:29 2018

@author: hecongcong
"""

###问题1：将中序表达式转化为逆波兰表达式(后缀表达式)
##逆波兰记法不需要括号来标识操作符的优先级.

'''
步骤1：首先，需要分配2个栈，栈s1用于临时存储运算符
（含一个结束符号），此运算符在栈内遵循越往栈顶优先级越高的原则；
栈s2用于输入逆波兰式，为方便起见，栈s1需先放入一个优先级
最低的运算符，在这里假定为'#'；

步骤2：从中缀式的左端开始逐个读取字符x，逐序进行如下步骤：
1.若x是操作数，则分析出完整的运算数（在这里为方便，用字母代替数字），
将x直接压入栈s2；

2.若x是运算符，则分情况讨论：
      若x是'('，则直接压入栈s1；
      若x是')'，则将距离栈s1栈顶的
最近的'('之间的运算符，逐个出栈，依次压入栈s2，此时抛弃'('；
      若x是除'('和')'外的运算符，则再分如下情况讨论：
         若当前栈s1的栈顶元素为'('，则将x直接压入栈s1；
         若当前栈s1的栈顶元素不为'('，则将x与栈s1的栈顶元素比较，
         若x的优先级大于栈s1栈顶运算符优先级，则将x直接压入栈s1。
         否者，将栈s1的栈顶运算符弹出，压入栈s2中，
         直到栈s1的栈顶运算符优先级别低于（不包括等于）x的优先级，
         或栈s2的栈顶运算符为'('，此时再则将x压入栈s1;


步骤3：在进行完(2)后，检查栈s1是否为空，若不为空，
则将栈中元素依次弹出并压入栈s2中（不包括'#'）；
'''

#######question 224:Basic Calculator
def calculate(s):
    s1=['#']
    s2=[]
    tmp=''
    num1=0
    num2=0
    start=0
    end=0
    s=s+'*'
    i=0
    while(s[i]!='*'):
        if(s[i]==' '):
            i+=1
        elif(s[i]=='('):
            s1.append(s[i])
            i+=1
        elif(s[i]==')'):
            while(s1[-1]!='('):
                tmp=s1.pop()
                num1=s2.pop()
                num2=s2.pop()
                if(tmp=='+'):
                    s2.append(num2+num1)
                elif(tmp=='-'):
                    s2.append(num2-num1)
            s1.pop()
            i+=1
        elif(s[i]=='+' or s[i]=='-'):
            while(s1[-1]!='#' and s1[-1]!='('):
                  tmp=s1.pop()
                  num1=s2.pop()
                  num2=s2.pop()
                  if(tmp=='+'):
                      s2.append(num2+num1)
                  elif(tmp=='-'):
                      s2.append(num2-num1)
            s1.append(s[i])
            i+=1
        else:
            start,end=i,i
            while(s[end] not in ('+','-',' ','(',')')):
                end+=1
                if(s[end]=='*'):
                    break
            s2.append(int(s[start:end]))
            i=end
    while(len(s1)>1):
        tmp=s1.pop()
        num1=s2.pop()
        num2=s2.pop()
        if(tmp=='+'):
            s2.append(num2+num1)
        elif(tmp=='-'):
            s2.append(num2-num1)
    if(len(s2)==1):
        return(s2[0])
    elif(len(s2)>1):
        return(int(s[:-1]))
    elif(len(s2)==0):
        return(0)
                 
            
                
                
#########question 227:Basic Calculator II
def calculate1(s):
    s1=['#']
    s2=[]
    tmp=''
    num1,num2=0,0
    start,end=0,0
    s=s+'%'
    i=0
    while(s[i]!='%'):
        if(s[i]==' '):
            i+=1
        elif(s[i]=='+' or s[i]=='-'):
            while(s1[-1]!='#'):
                  tmp=s1.pop()
                  num1=s2.pop()
                  num2=s2.pop()
                  if(tmp=='+'):
                      s2.append(num2+num1)
                  elif(tmp=='-'):
                      s2.append(num2-num1)
                  elif(tmp=='*'):
                      s2.append(num2*num1)
                  elif(tmp=='/'):
                      s2.append(int(num2/num1))
            s1.append(s[i])
            i+=1
        elif(s[i]=='*' or s[i]=='/'):
            while(s1[-1]=='*' or s1[-1]=='/'):
                tmp=s1.pop()
                num1=s2.pop()
                num2=s2.pop()
                if(tmp=='*'):
                    s2.append(num2*num1)
                elif(tmp=='/'):
                    s2.append(int(num2/num1))
            s1.append(s[i])
            i+=1
        else:
            start,end=i,i
            while(s[end]>='0'):
                end+=1
                if(s[end]=='%'):
                    break
            s2.append(int(s[start:end]))
            i=end
    while(len(s1)>1):
        tmp=s1.pop()
        num1=s2.pop()
        num2=s2.pop()
        if(tmp=='/'):
            s2.append(int(num2/num1))
        elif(tmp=='*'):
            s2.append(num2*num1)
        elif(tmp=='+'):
            s2.append(num2+num1)
        elif(tmp=='-'):
            s2.append(num2-num1)
    return(s2[0])
    
                      

######问题二：
###tensorflow中的InteractiveSession().
###为了便于使用诸如 IPython之类的 Python 交互环境, 
###可以使用InteractiveSession 代替 Session 类, 
##使用Tensor.eval()和Operation.run()方法代替sess.run().



#######问题三：Kth Smallest Element in a BST
##Definition for a binary tree node.
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

###answer1:递归
class Solution:
    def kthSmallest(self,root,k):
        self.res=0
        self.count=0
        self.k=k
        self.inorderTravel(root)
        return(self.res)
    def inorderTravel(self,roots):
        if(roots==None):
            return
        self.inorderTravel(roots.left)
        self.count+=1
        if(self.count==self.k):
            self.res=roots.val
        self.inorderTravel(roots.right)


###answer2:非递归
class Solution1:
    def kthSmallest(self,root,k):
        s=[]
        while(True):
            while(root):
                s.append(root)
                root=root.left
            if(not s):
                break
            root=s.pop()
            k-=1
            if(k==0):
                return(root.val)
            root=root.right
        return(0)
        
        

########问题4：CNN中的padding:SAME和VALID.
###VALID:new_height,new_width=ceil((W-F+1)/S)
###SAME:new_height,new_width=ceil((W/S))
##其中:W为输入size,S为步长,F为filter的size.





#########问题5：

##tf.get_variable()和tf.variable()的区别.


##定义变量共享：获取已存在的变量（要求不仅名字，而且初始化方法等
##各个参数都一样），如果不存在，就新建一个.

##1.tf.variable用于初始化一个变量.
##.tf.get_variable可进行变量共享.


##2.tf.get_variable() 会检查当前命名空间下是否存在同样name的变量,
##可以方便共享变量。但是要配合reuse和tf.variable_scope() 
##使用进行变量共享。否则如已存在会报错。
##tf.Variable 每次都会新建一个变量名.
###变量共享例子如下：
'''
with tf.variable_scope("one"):
    a = tf.get_variable("v", [1]) #a.name == "one/v:0"
with tf.variable_scope("one"):
    b = tf.get_variable("v", [1]) #创建两个名字一样的变量会报错 ValueError: Variable one/v already exists 
with tf.variable_scope("one", reuse = True): #注意reuse的作用。
    c = tf.get_variable("v", [1]) #c.name == "one/v:0" 成功共享，因为设置了reuse

assert a==c #Assertion is true, they refer to the same object.

'''

##3.tf.get_variable() 如遇到已存在的变量名，则会报错（除变量共享），
##tf.variable()则会自动处理，新建一个变量。
'''
with tf.variable_scope("two"):
    d = tf.get_variable("v", [1]) #d.name == "two/v:0"
    e = tf.Variable(1, name = "v", expected_shape = [1]) #e.name == "two/v_1:0"  
'''
        
##4.tf.variable_scope()会作用于所有的变量，包括tf.variable,ops,和tf.get_variable等.
##tf.name_scope()只作用于tf.variable,ops等。




##################################问题6：
###python修饰器@.
import time

def timeit(func):
    def wrapper():
        start=time.clock()
        func()
        end=time.clock()
        print('used:',end-start)
    return(wrapper)

@timeit
def foo():
    print('in foo()')

###@即为修饰器，@下面一行函数foo,作为参数传给timeit函数，且等价于
##foo=timeit(foo)





#################问题7：Additive Number
####用深度优先搜索(dfs),即回溯+剪枝。

class Soluiton:
    def isAdditiveNumber(self,num):
        return(self.dfs(num,[]))
        
    def dfs(self,strs,path):
        if(len(path)>=3 and path[-1]!=path[-2]+path[-3]):  #1
            return(False)
        if(not strs and len(path)>=3):
            '''由于#1,所以默认有
            path[-1]==path[-2]+path[-3]
            '''
            return(True)
        for i in range(len(strs)):
            curr=strs[:i+1]
            if(curr[0]=='0' and len(curr)!=1):
                continue
            if(self.dfs(strs[i+1:],path+[int(curr)])):
                return(True)
        return(False)

'''如果循环全部为假，则最终返回False，如有一个为真，则最终为True.'''        
            
        

      
######################问题8：线段树题.

class NumArray:
    def __init__(self,nums):
        import math
        self.nums=nums
        self.size=size=len(nums)
        h=math.ceil(math.log(size,2)) if(size) else 0
        maxSize=2**(h+1)-1   ##等比数列求和公式
        self.st=[0]*maxSize
        if(size):
            self.initSt(0,size-1,0)
    
    def update(self,i,val):
        if(i<0 or i>=self.size):
            return
        diff=val-self.nums[i]
        self.nums[i]=val
        self.updateSt(0,self.size-1,i,diff,0)
        
    def sumRange(self,i,j):
        if(i<0 or j<0 or i>=self.size or j>=self.size):
            return(0)
        return(self.sumRangeSt(0,self.size-1,i,j,0))
    
    
    ###
    def initSt(self,ss,se,si):
        if(ss==se):
            self.st[si]=self.nums[ss]
        else:
            mid=(ss+se)//2
            self.st[si]=self.initSt(ss,mid,si*2+1)+\
                        self.initSt(mid+1,se,si*2+2)
        return(self.st[si])
    
    def updateSt(self,ss,se,i,diff,si):
        if(i<ss or i>se):
            return
        self.st[si]+=diff
        if(ss!=se):
            mid=(ss+se)//2
            self.updateSt(ss,mid,i,diff,2*si+1)
            self.updateSt(mid+1,se,i,diff,2*si+2)
    
    
    def sumRangeSt(self,ss,se,qs,qe,si):
        if(qs<=ss and qe>=se):
            return(self.st[si])
        if(se<qs or ss>qe):
            return(0)
        mid=(ss+se)//2
        return(self.sumRangeSt(ss,mid,qs,qe,2*si+1)+\
               self.sumRangeSt(mid+1,se,qs,qe,2*si+2))


####################问题9：Count of Smaller Numbers After Self.
##########归并排序+统计逆序个数.
def countSmaller(nums):
    smaller=[0]*len(nums)
    def merge_sort(enums):
        mid=len(enums)//2
        if(mid):
            left,right=merge_sort(enums[:mid]),merge_sort(enums[mid:])
            m,n=len(left),len(right)
            i=j=0
            while(i<m or j<n):
                if(j==n or (i<m and left[i][1]<=right[j][1])):
                    enums[i+j]=left[i]
                    smaller[left[i][0]]+=j
                    i+=1
                else:
                    enums[i+j]=right[j]
                    j+=1
        return(enums)
    
    merge_sort(list(enumerate(nums)))
    return(smaller)
    



##################问题10：for 循环的本质.
'''
for循环是以索引进行循环，第一索引0，第二为索引1，等等
b本次都在改变，相当循环有个计数器count,表示一共取了几次数，即第几个数；
'''
#Examples1:
def a():
    b=[1,2,3,4,5]
    for i in b:
        b.remove(i)
        print(i)
    return(b)

'''
打印：1，3，5.
返回:[2,4]
'''

#但是：Examples2:
'''
因为循环中，第一次调用sorted(b)以后，以后就不再调用这个函数，for循环其实就是静态的，
b的改变，不会影响for循环的进程，即不会每次都调用sorted(b)；即任何函数后过后，fn(b)和b是完全分离，相互没有关系的了；
'''
def a():
    b=[5,4,3,2,1]
    for i in sorted(b):
        b.remove(i)
        print(i)
    return(b)
'''
打印：1，2，3，4，5.
返回：[]
'''


############################问题11：二、八、十六进制的表示
'''
二进制：以0b开头，比如0b0011=3；逢2进1，基础元素是0,1;bin();
八进制：以0o开头，比如0o7=7,0o12=10;逢8进1，基础元素是0到7；oct();
十六进制：以0x开头，比如0x1F=31;逢16进1，基础元素是0到15，其中10到
15分别用A,B,C,D,E,F表示；hex();
'''


#############################问题12：python取模问题
'''
1.python中的取模和C/JAVA在负数上的取模运算的结果是不一样的.
2.取模运算在数学上就是通过辗转相除法得到余数，一般满足下式：
设m=A%B,n=A//B,则：A=n*B+m,其中|m|<|B|,
所以m=A-n*B,而n的计算历史上出现2个分支如下：

(1):truncate
思想很简单，就是截去小数部分,因此：
m=A-B*truncate(A/B);
比如：truncate(3/2)=1,truncate(-3/2)=-1

(2)floor
思想则是向下取整，在正数的时候和truncate一样，负数的时候则会不一样，则：
m=A-B*floor(A/B);
比如：floor(3/2)=1,floor(-3/2)=-2

3.C和Java用的是truncate,python用的是floor.

4.结论：在取模运算上，基本上不同的语言都有自己的一套机制，一般来说，在
正数上都一样，但是在负数上会有不同;

5.python举例：
(1):8%3=8-3*floor(8/3)=8-3*2=2
(2):-8%-3=-8-(-3*floor(-8/-3))=-8-(-3*2)=-2
(3):8%-3=8-(-3*floor(8/-3))=8-(-3*-3)=-1
(4):-8%3=-8-3*floor(-8/3)=-8-3*-3=1
'''


#################################问题13：PYTHONPATH与path
'''
PYTHONPATH:是python程序用来搜索模块的路径;
path:是系统环境变量,是服务器主机用于搜索可执行的程序的默认路径,目的不同;
'''




#################################问题14：locals和globals函数
'''
分别以字典的形式，返回相应作用域的局部变量与全局变量.
比如：
def fn(x):
    y=x+100
    b=9
    def fn1():
        c=99+b
        d=88
        return(locals(),globals())
    return(fn1())

返回：locals():{'b': 9, 'c': 108, 'd': 88}
'''



#################################问题15：作用域(全局变量和局部变量)
'''
1.每个函数调用都会创建一个新的作用域(命名空间),比如：
x=1
def foo():
    x=42
调用foo()以后，x还是等于1,这是因为调用foo()的时候，新的命名空间就被创建
了，它只作用于foo内的代码块.


2.在函数内部只想读取全局变量(不重新绑定变量)，时没有问题的;如果局部变量
或者参数的名字和想要访问的全局变量名相同的话，就不能直接访问了，全局变量
会被局部变量屏蔽.


3.重新绑定全局变量.如果在函数内部将值赋予一个变量,它会自动变成局部变量
--除非告知python将其声明为全局变量.比如：
x=1
def change():
    x+=1

returns:UnboundLocalError: 
local variable 'x' referenced before assignment.

def change():
    global x
    x+=1
Returns:x=2



4.各层函数内的变量被称为相关的局部变量,最外层函数之外的变量被称为
全局变量.比如:
x=1
def change():
    y=99
    def fn():
        z=88
    fn()
    return(y)

总结：x为全局变量,y为change函数内部作用域的相关局部变量,z为fn函数内部
作用域的相关局部变量.



5.(重点)嵌套作用域,python的函数是可以嵌套的,也就是说可以将一个
函数放在另一个里面.
内层函数可以访问外层函数所定义作用域中的参数,即它带着外层函数作用域
(相关的局部变量).


6.外部作用域的变量一般来说是不能重新绑定(和重新绑定全局变量区分),但在
python3.0中，nonlocal关键字被引入，它和global关键字使用方式类似,可以
让用户对外部作用域（但并非全局作用域）的变量进行赋值.

比如：
第一种情况：
x=1
def change():
    y=99
    def fn():
        nonlocal y
        y+=1
    fn()
    return(y)
    
Returns:100


x=1
def change():
    y=99
    def fn():
        global y
        y+=1
    fn()
    return(y)
    
Returns:NameError: name 'y' is not defined.


x=1
def change():
    y=99
    def fn():
        y+=1
    fn()
    return(y)
    
Returns:UnboundLocalError: 
        local variable 'y' referenced before assignment


x=1
def change():
    y=99
    def fn():
        global x
        x+=1
    fn()
    return(x)
    
Returns:2.
'''


##################################问题16：python中的==和is
'''
1.python中的对象包含三个基本要素，分别是：
id(身份标识)、type(数据类型)和value(值).

2.is和==都是对对象进行比较判断作用的，但对对象比较判断的内容并不相同.
==比较操作符和is同一性运算符区别如下：
首先，==是python标准操作符中的比较操作符，用来比较判断两个对象的value(值)
是否相等.
而，is是同一性运算符，这个运算符判断的是对象间的唯一身份标识，也就是id
是否相同.

3.举例如下：
x=[1,2,3],y=[1,2,3]
x==y   #True
x is y  # False

4.其中对象的id会涉及到小数据池和代码块的相关知识.
'''

##################################问题17：变量的赋值问题及ID
##################################(小整型池及代码块等)
'''
1.变量的赋值：在python中变量的赋值采用的是引用语义法，变量是对内存及其
地址的抽象.这和C语言的值语义法有区别.
对于python而言，python的一切变量都是对象，变量的存储，采用了引用语义的
方式，存储的只是一个变量的值所在的内存地址，而不是这个变量的只本身。

2.对于python而言，如果id相同则值肯定相同，但是值相同id不一定相同.
一般而言，只要重新创建一个变量，python解释器都会重新分配内存地址，即
id会不同，但是在python规定的特殊情况下除外，比如小整型池及代码块等.
'''


###################################问题18：小整形池和代码块问题
'''
1.代码块：Python程序是由代码块构造的。块是一个python程序的文本，它
是作为一个单元执行的.一个模块，一个函数，一个类，一个文件等都是一个
代码块.作为交互方式输入的每个命令都是一个代码块.

2.代码块缓存机制：Python在执行同一个代码块的初始化对象的命令时，会
检查是否其值是否已经存在，如果存在，会将对其重新引用.所以，文件在执
行时(同一个代码块)，如果i1=999已经出现，则重新初始化i2=999时，不会
重新分配内存地址，而是直接重新引用，因此i1和i2具有相同的内存地址(id).
代码块缓存机制的适用范围：int(float)、str、bool.
int:任何数字在同一代码块下都会复用.
bool:True和False在字典中会以1，0方式存在，并且复用.
str:几乎所有的字符串都会符合缓存机制，有其具体规定.
机制优点：需要值相同的字符串，整数的时候，直接从‘字典’中取出复用，避免
频繁的创建和销毁，提升效率，节约内存.

3.小数据池：小整数缓存机制，或者称为驻留机制.
适用范围：小数据池也是只针对 int(float)，str，bool且是针对不同代码块
之间的缓存机制！！！
Python自动将-5~256的整数进行了缓存，当将这些整数重新赋值给变量时，并
不会重新创建对象，既重新分配内存，而是引用已经建好的缓存对象，既id不变.
python会将一定规则的字符串在字符串驻留池中，创建一份，当将这些字符串赋
值给变量时，并不会重新创建对象，既重新分配内存，而是引用在字符串驻留池中
创建好的对象.
总结：无论是缓存还是字符串驻留池，都是python做的一个优化，就是将~5-256的整数，
和一定规则的字符串，放在一个‘池’（容器，或者字典）中，无论程序中那些变量指向
这些范围内的整数或者字符串，那么他直接在这个‘池’中引用，既不会重新分配内存地址.
因此，比如对于整数来说，小数据池的范围是-5~256 ，如果多个变量都是指向同一个（在这个范
围内的）数字，他们在内存中指向的都是一个内存地址.
机制优点:需要值相同的字符串，整数的时候，直接从‘池’里拿来用，避免频繁的创建和
销毁，提升效率，节约内存.

4.小结：
如果在同一代码块下，则采用同一代码块下的换缓存机制.
如果是不同代码块，则采用小数据池的驻留机制.
'''

