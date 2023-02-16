# 属性访问控制
class Access(object):

    def __getattr__(self, name):
        print('__getattr__')
        return super(Access, self).__getattr__(name)

    def __setattr__(self, name, value):
        print('__setattr__')
        return super(Access, self).__setattr__(name, value)

    def __delattr__(self, name):
        print('__delattr__')
        return super(Access, self).__delattr__(name)

    def __getattribute__(self, name):
        print('__getattribute__')
        return super(Access, self).__getattribute__(name)


# 例子说明__setattr__的无限递归错误:
#
# def__setattr__(self, name, value):
#     self.name = value
#     # 每一次属性赋值时, __setattr__都会被调用，因此不断调用自身导致无限递归了。
# 因此正确的写法应该是:
#
# def__setattr__(self, name, value):
#     self.__dict__[name] = value

# __delattr__如果在其实现中出现del self.name 这样的代码也会出现"无限递归"错误，这是一样的原因。


access = Access()
access.attr1 = True  # __setattr__调用
access.attr1  # 属性存在,只有__getattribute__调用
try:
    access.attr2  # 属性不存在, 先调用__getattribute__, 后调用__getattr__
except AttributeError:
    pass
del access.attr1  # __delattr__调用


# 描述器对象
class Meter(object):
    '''Descriptor for a meter.'''

    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Foot(object):
    '''Descriptor for a foot.'''

    def __get__(self, instance, owner):
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Distance(object):
    meter = Meter()
    foot = Foot()


d = Distance()
print(d.meter, d.foot)  # 0.0, 0.0
d.meter = 1
print(d.meter, d.foot)  # 1.0 3.2808
d.meter = 2
print(d.meter, d.foot)  # 2.0 6.5616


# 在上面例子中,在还没有对Distance的实例赋值前, 我们认为meter和foot应该是各自类的实例对象, 但是输出却是数值。这是因为__get__发挥了作用.
#
# 我们只是修改了meter,并且将其赋值成为int，但foot也修改了。这是__set__发挥了作用.
#
# 描述器对象(Meter、Foot)不能独立存在, 它需要被另一个所有者类(Distance)所持有。
# 描述器对象可以访问到其拥有者实例的属性，比如例子中Foot的instance.meter。
#
# 在面向对象编程时，如果一个类的属性有相互依赖的关系时，使用描述器来编写代码可以很巧妙的组织逻辑。
# 在Django的ORM中, models.Model中的IntegerField等, 就是通过描述器来实现功能的。


# 构造自定义容器(Container)
# 如果要自定义不可变容器类型，只需要定义__len__ 和 __getitem__方法;
# 如果要自定义可变容器类型，还需要在不可变容器类型的基础上增加定义__setitem__ 和 __delitem__。
# 如果你希望你的自定义数据结构还支持"可迭代", 那就还需要定义__iter__。

# __len__(self)
#
# 需要返回数值类型，以表示容器的长度。该方法在可变容器和不可变容器中必须实现。
#
# __getitem__(self, key)
#
# 当你执行self[key]的时候，调用的就是该方法。该方法在可变容器和不可变容器中也都必须实现。
# 调用的时候,如果key的类型错误，该方法应该抛出TypeError；
# 如果没法返回key对应的数值时,该方法应该抛出ValueError。
#
# __setitem__(self, key, value)
#
# 当你执行self[key] = value时，调用的是该方法。
#
# __delitem__(self, key)
#
# 当你执行del self[key]的时候，调用的是该方法。
#
# __iter__(self)
#
# 该方法需要返回一个迭代器(iterator)。当你执行for x in container: 或者使用iter(container)时，该方法被调用。
#
# __reversed__(self)
#
# 如果想要该数据结构被內建函数reversed()支持,就还需要实现该方法。
#
# __contains__(self, item)
#
# 如果定义了该方法，那么在执行item in container 或者 item not in container时该方法就会被调用。
# 如果没有定义，那么Python会迭代容器中的元素来一个一个比较，从而决定返回True或者False。
#
# __missing__(self, key)
#
# dict字典类型会有该方法，它定义了key如果在容器中找不到时触发的行为。
# 比如d = {'a': 1}, 当你执行d[notexist]时，d.__missing__('notexist')就会被调用。
class FunctionalList:
    '''
    实现了内置类型list的功能,并丰富了一些其他方法: head, tail, init, last, drop, take
    '''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        # 获取第一个元素
        return self.values[0]

    def tail(self):
        # 获取第一个元素之后的所有元素
        return self.values[1:]

    def init(self):
        # 获取最后一个元素之前的所有元素
        return self.values[:-1]

    def last(self):
        # 获取最后一个元素
        return self.values[-1]

    def drop(self, n):
        # 获取所有元素，除了前N个
        return self.values[n:]

    def take(self, n):
        # 获取前N个元素
        return self.values[:n]


# 它会在你每次引用一个值未定义的属性时为你自动创建数组或者字典。
class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


weather = AutoVivification()
weather['china']['guangdong']['shenzhen'] = 'sunny'
weather['china']['hubei']['wuhan'] = 'windy'
weather['USA']['California']['Los Angeles'] = 'sunny'
print(weather)


# 结果输出:{'china': {'hubei': {'wuhan': 'windy'}, 'guangdong': {'shenzhen': 'sunny'}}, 'USA':    {'California': {'Los Angeles': 'sunny'}}}

# 上下文管理
# 在with声明的代码段中，我们可以做一些对象的开始操作和清除操作,还能对异常进行处理。
# 这需要实现两个魔术方法: __enter__ 和 __exit__。
#
# __enter__(self)
#
# __enter__会返回一个值，并赋值给as关键词之后的变量。在这里，你可以定义代码段开始的一些操作。
#
# __exit__(self, exception_type, exception_value, traceback)
#
# __exit__定义了代码段结束后的一些操作，可以这里执行一些清除操作，或者做一些代码段结束后需要立即执行的命令，比如文件的关闭，socket断开等。如果代码段成功结束，那么exception_type, exception_value, traceback 三个参数传进来时都将为None。如果代码段抛出异常，那么传进来的三个参数将分别为: 异常的类型，异常的值，异常的追踪栈。
# 如果__exit__返回True, 那么with声明下的代码段的一切异常将会被屏蔽。
# 如果__exit__返回None, 那么如果有异常，异常将正常抛出，这时候with的作用将不会显现出来。
class DemoManager(object):

    def __enter__(self):
        pass

    def __exit__(self, ex_type, ex_value, ex_tb):
        if ex_type is IndexError:
            print(ex_value.__class__)
            return True
        if ex_type is TypeError:
            print(ex_value.__class__)
            return  # return None


with DemoManager() as nothing:
    data = [1, 2, 3]
    data[4]  # raise IndexError, 该异常被__exit__处理了

with DemoManager() as nothing:
    data = [1, 2, 3]
    data['a']  # raise TypeError, 该异常没有被__exit__处理



# __str__(self)
#
# 对实例使用str()时调用。
#
# __repr__(self)
#
# 对实例使用repr()时调用。str()和repr()都是返回一个代表该实例的字符串，
# 主要区别在于: str()的返回值要方便人来看,而repr()的返回值要方便计算机看。
#
# __unicode__(self)
#
# 对实例使用unicode()时调用。unicode()与str()的区别在于: 前者返回值是unicode, 后者返回值是str。unicode和str都是basestring的子类。
#
# 当你对一个类只定义了__str__但没定义__unicode__时,__unicode__会根据__str__的返回值自动实现,即return unicode(self.__str__());
# 但返回来则不成立。
# Python3中，str与unicode的区别被废除了,因而__unicode__没有了，取而代之地出现了__bytes__.


# __format__(self, formatstr)
#
# "Hello, {0:abc}".format(a)等价于format(a, "abc"), 等价于a.__format__("abc")。
#
# 这在需要格式化展示对象的时候非常有用，比如格式化时间对象。
#
# __hash__(self)
#
# 对实例使用hash()时调用, 返回值是数值类型。