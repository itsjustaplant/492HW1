'''
Unit tests for converter module
'''
from converter import __version__
from converter import fahrenheit_to_celsius

def test_version():
    '''
    Version test
    '''
    assert __version__ == '0.1.0'


def test_converter():
    '''
    Unit test for fahrenheit_to_celsius function
    '''
    fahrenheit_values = [-40.0, 0.0, 32.0, 68.0, 98.6, 212.0]
    celsius_values = [-40.0, -17.7778, 0.0, 20.0, 37.0, 100.0]
    # pylint: disable=consider-using-enumerate
    for i in range(len(fahrenheit_values)):
        fahrenheit_value = fahrenheit_values[i]
        celsius_value = celsius_values[i]
        assert fahrenheit_to_celsius(fahrenheit_value) == celsius_value
