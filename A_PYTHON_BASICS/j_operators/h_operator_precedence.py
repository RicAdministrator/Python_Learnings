# The precedence order is described in the table below, starting with the highest precedence at the top:
# OPERATOR                                     | DESCRIPTION
# ()	                                       | Parentheses	
# **	                                       | Exponentiation	
# +x  -x  ~x                                   | Unary plus, unary minus, and bitwise NOT	
# *  /  //  %                                  | Multiplication, division, floor division, and modulus	
# +  -	                                       | Addition and subtraction	
# <<  >>	                                   | Bitwise left and right shifts	
# &	                                           | Bitwise AND	
# ^	                                           | Bitwise XOR	
# |	                                           | Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in | Comparisons, identity, and membership operators	
# not	                                       | Logical NOT	
# and	                                       | AND	
# or	                                       | OR

# Operator : ()
# Description : Parentheses
print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""

##########################################################################################

# Operator : **
# Description : Exponentiation
print(100 - 3 ** 3)

"""
Exponentiation has higher precedence than subtraction, and needs to be evaluated first.
3 ** 3 = 3*3*3 = 27
The calculation above reads 100 - 27 = 73
"""

##########################################################################################

# Operator : *  /  //  % 
# Description : Multiplication, division, floor division, and modulus
print(100 + 5 * 3)

"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""

##########################################################################################

# Operator : +  -
# Description : Addition and subtraction
print(100 - 5 * 3)

"""
Subtraction has a lower precedence than multiplication, and we need to calculate the multiplication first.
The calculation above reads 100 - 15 = 85
"""

# To Do: Add more examples for the remaining operators in the precedence order.

##########################################################################################

# Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:
print(5 + 4 - 7 + 3) # Output: 5

"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""