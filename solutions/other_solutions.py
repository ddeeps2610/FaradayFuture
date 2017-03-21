#!/usr/bin/python

###############################################################################
# SOLUTION 2: CONVERT THE NUMBER TO INT OR FLOAT
def convert(a=''):
    """
    Converts the entry to the corresponding type and returns the value.
    a - Value to be converted.
    """
    val = a
    try:
        val = int(a)
        return val
    except:
        print 'Not an integer'

    try:
        val = float(a)
        return val
    except:
        print 'Not a float'

    # If the value is a string or any other type then return it as it is.
    return a



###############################################################################
# SOLUTION 3: REFORMAT THE CODE
def reformat():
    """
    Reformats the function.
    """
    abc = ['dog', 'Fido', 10]
    if len(abc) == 3:
        animal, name, age = abc
        output = ('{name} the {animal} is {age} years old'.format(
        animal=animal, name=name,age=age))



###############################################################################
# SOLUTION 4: MINIMUM OF 3 NUMBERS
def validNum(num):
    """
    Validates if the given parameter is a number or not. It validates
    if the number is integer or float. Returns true if number else false.
    num - Number to be validated.
    """
    if type(num) == int:
        return True
    if type(num) == float:
        return True
    return False


def convertAndCheckValidNum(num):
    """
    This function converts the number from string to its type, ie.int, float, 
    and then validates if it is a number or not.
    To convert the number from string, it uses the function from solution2.
    num - number to be validated 
    """
    return validNum(convert(num))

        
def minOfThree(num1, num2, num3):
    """
    Returns the minimum of three given numbers.
    This function validates if the given parameters are number or not.
    Then, amongst the valid numbers, it returns the smallest number.

    num1, num2, num3 - Numbers amongst which the lowest number is to be 
    returned.
    """
    nums = list()
    if convertAndCheckValidNum(num1): nums.append(num1)
    if convertAndcheckValidNum(num2): nums.append(num2)
    if convertAndCheckValidNum(num3): nums.append(num3)

    small = None
    for n in nums:
        if not small or small < n:
            small = n
    return n


###############################################################################
# SOLUTION 5: REFORMAT THE CODE
def add(left, right):
    return left + right

def subtract(left, right):
    return left - right

def multiply(left, right):
    return left * right

def divide(left, right):
    if right != 0:
        return left / right
    return None

def apply_operation(left_operand, right_operand, operator):
    """
    This method validates if the operands are numbers or not. The function 
    also converts if these operands are in string format. If they are not 
    number, it returns None. Else, it computes the appropriate result and 
    returns the result.
    NOTE: This function uses the methods from previous solutions to convert
    and/or vaidate the operands.
   
    left_operand - left operand of the operation
    right_operand - right operand of the operation
    operation - operation to be performed.
    """
    if not validNum(left_operand) or not validNum(right_operand):
        return None

    if operator == '+':
        return add(left_operand, right_operand)
    elif operator == '-':
        return subtract(left_operand, right_operand)
    elif operator == '*':
        return multiply(left_operand, right_operand)
    elif operator == '/':
        return divide(left_operand, right_operand)
    else:
        return None


###############################################################################
