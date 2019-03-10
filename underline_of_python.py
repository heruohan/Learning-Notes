# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 22:27:29 2019

@author: hecongcong
"""


####################:python中五种下划线组合的含义
'''
python中的下划线组合常用的有5种，其具有不同的约定、含义及工作原理；
其在Python变量和方法名称中都各有其含义。有一些含义仅仅是依照约定，
被视作是对程序员的提示，而有一些含义是由Python解释器严格执行的。
本笔记中，讨论以下5中下划线模式和命名约定，以及它们如何影响python程序的行为：
1.单前导下划线：_var
2.单末尾下划线：var_
3.双前导下划线：__var
4.双前导和末尾下划线：__var__
5.单下划线：_
'''


#######################:1、单前导下划线_var
'''
1、成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；

2、当涉及到变量和方法名称时，单个下划线前缀有一个约定俗成的含义,它是堆程序员
的提示，意味着Python社区一致认为它应该是什么意思，但程序的行为不受影响。

3、单下划线前缀的含义是告知其他程序员：以单个下划线开头的变量或方法仅供内部
使用。这不是Python强制规定的。 Python不像Java那样在“私有”和“公共”变量之间
有很强的区别。
例1：
class Test:
    def __init__(self):
        self.a=1
        self._b=2

t=Test()
t.a=1
t._b=2.  
因此，Python中的单个下划线前缀仅仅是一个约定，并没有阻止我们“进入”类并访问
该变量的值；

4、但是其影响我们从模块中导入名称的方式.
例2：如有以下模块
#this is my_module.py
def external_func():
    return(23)

def _internal_func():
    return(42)
    
if: from my_module import * 在编程过程中尽量不要使用此种导入方式)
>>>external_func()  
23
>>>_internal_func()
NameError:'name _internal_func is not defined'


if:import my_module
>>>my_module.external_func()
23
>>>my_module._internal_func()
42

5、总结：单个下划线是一个Python命名约定，表示这个名称是供内部使用的。 
它通常不由Python解释器强制执行，仅仅作为一种对程序员的提示。
'''



#######################:2、单末尾下划线var_
'''
1.有时候，一个变量的最合适的名称已经被一个关键字所占用。 因此，像class或
def这样的名称不能用作Python中的变量名称。可以附加一个下划线来解决命名冲突：
例1：
>>>def make_object(name,class):    class为一个关键字
SyntaxError:'invalid syntax'

>>>def make_object(name,class_):
    pass

2.总结：单个末尾下划线（后缀）是一个约定，用来避免与Python关键字产生命
名冲突.PEP 8解释了这个约定.
'''



##########################:3、双前导下划线__var
'''
1、"双下划线" 是私有成员，意思是只有类对象自己内部能访问，连子类
对象也不能访问到这个数据。python解释器修改了其名称，实在要访问也是
可以的；
例1：
class Test:
    def __init__(self):
        self.a=1
        self.__b=2
    def fn(self):
        return(self.__b)
>>>t=Test()
>>>t.__b   #从外部不能访问
AttributeError: 'Test' object has no attribute '__b'
>>>t.fn()   #内部可以访问
2
>>>t._Test__b   #要访问也可以，python解释器将其名称修改
2

class A(Test):
    def q(self):
        return(self.__b)

>>>t=A()
>>>t.q()  #子类内部也不能访问
AttributeError: 'A' object has no attribute '_A__b'
>>>t._Test__b  #要访问也可以，先继承，然后在访问修改后的
2




2、到目前为止，我们所涉及的所有命名模式的含义，来自于已达成共识的约定。
而对于以双下划线开头的Python类的属性（包括变量和方法），情况就不同了。
双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突。
例2：
class Test:
    def __init__(self):
        self.foo=1
        self._bar=2
        self.__baz=2  #其实被解释器把名字修改为_Test__baz
    
>>>t=Test()
>>>dir(t)
['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'__weakref__', '_bar', 'foo']

python解释器将以双下划线前缀的变量名字修改为_Test__baz.这就是Python解释器
所做的名称修饰。它这样做是为了防止变量在子类中被重写。

建立一个Test的子类A，
例2：
class A(Test):
    def __init__(self):
        super(A,self).__init__()
        self.foo=99
        self._bar=99
        self.__baz=99  #其实被解释器把名字修改为_A__baz

>>>t=A()
>>>t.foo
99
>>>t._bar
99
>>>t.__baz
AttributeError: "'ExtendedTest' object has no attribute '__baz'"
>>>t._Test__baz
2
>>>t._A__baz
99
>>>dir(t)
['_ExtendedTest__baz', '_Test__baz', '__class__', '__delattr__',
'__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__', '__le__',
'__lt__', '__module__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', '_bar', 'foo', 'get_vars']

因此，类A继承了类Test，通用情况是如果有重复的就子类覆盖基类；而__baz没有
被覆盖且有两个是因为__baz在基类和子类中分别被python解释器修改为不同的名字.



3、总结上文，看以下例子：
例3：
class A:
    def __init__(self):
        self.__private()   #实际的名字为self._A__private()
        self.public()
    def __private(self):   #解释器实际将方法的名字修改为了_A__private
        print('A.__private()')
    def public(self):
        print('A.public')
        
class B(A):
    def __private(self):    #解释器已将名字修改为_B__private()
        print('B.__private()')
    def public(self):
        print('B.public')

>>>b=B()
A.__private()
B.piblic()

原因：类B继承了类A的构造方法，但是解释器已将类A中的私有变量的名字修改为
_A__private,基类B中的私有变量也被修改为_B__private(),因为其和父类A是
不同名字的方法，所以基类的方法不能覆盖父类A的__private,类A构造方法里
访问的其实是self._A__private();
而对于普通的方法public()，子类B中有和父类A中名字完全相同的方法public(),
所以子类B中的public将父类中的public覆盖了；即子类B重写了自己的public()方法；
'''









