'''
Logger module
'''
from .converter import fahr_to_cent

def print_fahr_to_cent(fahr):
    '''
    Converts fahrenheit to celsius and logs it
    :param float fahr: Fahrenheit in degrees
    '''
    result = fahr_to_cent(fahr)
    print(result)
