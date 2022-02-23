'''
Main script
'''
from converter import fahrenheit_to_celsius
def main():
    '''
    main function
    '''
    fahrenheit_values = [-40.0, 0.0, 32.0, 68.0, 98.6, 212.0]
    celsius_values = [-40.0, -17.7778, 0.0, 20.0, 37.0, 100.0]
    # pylint: disable=consider-using-enumerate, line-too-long
    for i in range(len(fahrenheit_values)):
        fahrenheit_value = fahrenheit_values[i]
        celsius_value = celsius_values[i]
        print(f"Expected value: {fahrenheit_to_celsius(fahrenheit_value)} -- Output value: {celsius_value}")

if __name__ == "__main__":
    main()
