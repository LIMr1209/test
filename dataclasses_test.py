from dataclasses import dataclass, field
from typing import List
from datetime import datetime
import dateutil


@dataclass(order=True)  # 注意这里
class Article(object):
    # repr参数表示该field是否被包含进repr的输出，compare和hash参数表示field是否参与比较和计算hash值
    _id: int
    author_id: int
    title: str = field(compare=False)
    text: str = field(repr=False, compare=False)
    c: int = field(init=False)  # init参数如果设置为False，表示不为这个field生成初始化操作
    tags: List[str] = field(default=list, repr=False, compare=False)
    created: datetime = field(default=datetime.now(), repr=False, compare=False)
    edited: datetime = field(default=datetime.now(), repr=False, compare=False)

    # __post_init__在__init__后被调用，我们可以在这里初始化那些需要前置条件的field。
    def __post_init__(self):
        self.c = 1
        if type(self.created) is str:
            self.created = dateutil.parser.parse(self.created)

        if type(self.edited) is str:
            self.edited = dateutil.parser.parse(self.edited)


a = Article(1, 2, 'python', 'python人工智能')
b = Article(1, 2, 'python', 'python人工智能')
print(a == b)
print(a.created.__hash__())

from dataclasses import asdict, astuple

print(asdict(a))  # 转化字典
print(astuple(b))  # 转化元组

"""
python3.7引入dataclass的一大原因就在于相比namedtuple，dataclass可以享受继承带来的便利。
dataclass装饰器会检查当前class的所有基类，如果发现一个dataclass，就会把它的字段按顺序添加进当前的class，随后再处理当前class的field。所有生成的方法也将按照这一过程处理，因此如果子类中的field与基类同名，那么子类将会无条件覆盖基类。子类将会根据所有的field重新生成一个构造函数，并在其中初始化基类。
"""

@dataclass
class Base:
    x: float = 25.0
    y: int = 0

@dataclass
class C(Base):
    z: int = 10
    x: int = 15

c = C()
print(c)
