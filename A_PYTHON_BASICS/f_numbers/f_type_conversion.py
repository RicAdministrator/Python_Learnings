# You can convert from one type to another with the int(), float(), and complex() methods
# You cannot convert complex numbers into another number type.

_int = 1    # int
_float = 2.8  # float
_complex = 1j   # complex

# convert from int to float:
intToFloat = float(_int)
printMessage = f"""convert from int to float
int = {_int}, type = {type(_int)}
intToFloat = {intToFloat}, type = {type(intToFloat)}
"""
print(printMessage)

# convert from int to complex:
intToComplex = complex(_int)
printMessage = f"convert from int to complex\nint = {_int}, type = {type(_int)}\nintToComplex = {intToComplex}, type = {type(intToComplex)}\n"
print(printMessage)

# convert from float to int:
floatToInt = int(_float)
printMessage = f"convert from float to int\nfloat = {_float}, type = {type(_float)}\nfloatToInt = {floatToInt}, type = {type(floatToInt)}\n"
print(printMessage)

# convert from float to complex:
floatToComplex = complex(_float)
printMessage = f"convert from float to complex\nfloat = {_float}, type = {type(_float)}\nfloatToComplex = {floatToComplex}, type = {type(floatToComplex)}\n"
print(printMessage)