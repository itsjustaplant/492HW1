# pylint: disable = invalid-name, unused-variable
'''
Main script
'''
from machine import math
from machine import fahr_to_cent
from machine import cent_to_fahr
from machine import print_fahr_to_cent

def main():
    '''
    main function
    '''
    x = 42
    result = math.square(3) + math.square(4)
    print(x)
    boiling = fahr_to_cent(212)
    cold = cent_to_fahr(-40)
    print(result)
    print(math.abs(-22))
    print_fahr_to_cent(32)

if __name__ == "__main__":
    main()
