'''
Converter module
'''
def celsius_to_fahrenheit(temp):
    '''
    Converts celsius to fahrenheit
    :param float temp: Fahrenheit in degrees
    '''
    return round(temp * 9 / 5 + 32, 4)

def fahrenheit_to_celsius(temp):
    '''
    Converts fahrenheit to celsius
    :param float temp: Celsius in degrees
    '''
    return round((temp - 32) * 5 / 9, 4)
