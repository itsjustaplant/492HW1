'''
Converter module
'''
def fahr_to_cent(fahr):
    '''
    Converts fahrenheit to celsius
    :param float fahr
    '''
    return (fahr - 32) * 5 / 9

def cent_to_fahr(cent):
    '''
    Converts celsius to fahrenheit
    :param float cent
    '''
    return cent * 9 / 5 + 32
