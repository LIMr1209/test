
# str、float等基本类型，使用list、tuple复杂类型需要引用typing中的类型
def greeting(name: str) -> str:
    return 'Hello ' + name
x: str = 'xxx' # 声明一个变量为str类型
greeting(x) # Hello xxx
# greeting(123) # TypeError: can only concatenate str (not "int") to str

# 字典类型
from typing import Dict

# Dict[int, str] int代表key类型， str代表val类型
def test(t: Dict[int, str]) -> Dict:
    return t

test({1: '234'}) # {1: '234'}
test({'111':111})


# 数组类型
from typing import List

# 参数names为list类型并且元素都是str类型
# 返回为None
def greet_all(names: List[str]) -> None:
    for name in names:
        print('Hello ' + name)

names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)   # Ok!
# greet_all(ages)    #出错了 Error due to incompatible types

# 迭代对象类型 可以迭代类型包括 List、Set、Tuple、Str、Dict
from typing import Iterable

def greeting(names: Iterable[str]) -> None:
    for name in names:
        print(name)

greeting(['aaa', 'bbb']) # list aaa bbb
greeting(('ccc', 'ddd')) # tuple ccc ddd
greeting({'eee', 'fff'}) # set eee fff
greeting({'ggg': 'hhh'}) # dict ggg
greeting('123') # str 1 2 3
# greeting(678) # error: Argument 1 to "greeting" has incompatible type "int"; expected "Iterable[str]"


# 接受多个指定类型，但不接受除此外的类型
from typing import Union
# user_id 只能为int或者str
def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return 'user-{}'.format(100000 + user_id)
    else:
        return user_id
normalize_id(1) # user-100001
normalize_id('2') # 2


# 可选类型，给参数设置默认值
from typing import Optional

# Optional[str]只是Union [str，None]的简写或别名。它主要是为了方便帮助功能签名看起来更清洁
# Optional[str, int] 只能包含一个类型, 这样是不正确的
def greeting(name: Optional[str] = None) -> str:
    if name is None:
        name = 'stranger'
    return 'Hello, ' + name
greeting() # Hello, stranger
greeting('123') # Hello, 123


# 有时候我们不确定是什么类型的时候可以用到Any
from typing import Any

def greeting(name: Any = None) -> str:
    if name is None:
        name = 'stranger'

    return 'Hello, ' + str(name)

greeting() # Hello, stranger
greeting('123') # Hello, 123
greeting(234) # Hello, 234
greeting([345]) # Hello, [345]


# 自定义类型
from typing import TypeVar

T = TypeVar('T') # 任意类型
A = TypeVar('A', int, str) # A类型只能为int或str
def test(t: A) -> None:
    print(t)
test('1')
test(1)
test([1])
