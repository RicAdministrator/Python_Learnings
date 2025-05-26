_str = str("Hello World")
print(_str, type(_str))

_int = int(20)
print(_int, type(_int))

_float = float(20.5)
print(_float, type(_float))

_complex = complex(1j)
print(_complex, type(_complex))

_list = list(("apple", "banana", "cherry"))
print(_list, type(_list))

_tuple = tuple(("apple", "banana", "cherry"))
print(_tuple, type(_tuple))

_range = range(6)
print(_range, type(_range))

_dict = dict(name="John", age=36)
print(_dict, type(_dict))

_set = set(("apple", "banana", "cherry"))
print(_set, type(_set))

_frozenset = frozenset(("apple", "banana", "cherry"))
print(_frozenset, type(_frozenset))

_bool = bool(5)
print(_bool, type(_bool))

_bytes = bytes(5)
print(_bytes, type(_bytes))

_bytearray = bytearray(5)
print(_bytearray, type(_bytearray))

_memoryview = memoryview(bytes(5))
print(_memoryview, type(_memoryview))