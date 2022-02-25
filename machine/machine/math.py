'''
Redefined math module
'''
# pylint: disable = redefined-builtin, invalid-name
def square(x):
    '''
    Returns square of number
    :param float x: Number
    '''
    return x * x

def abs(x):
    '''
    Returns the absolute of number
    :param float x: Number
    '''
    if x < 0:
        return -x
    # This is a fallback actually, if we don't enter the if it will return the x
    return x
