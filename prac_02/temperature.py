def main():
    celsius_temp = float(input("Enter temperature in Celsius: "))
    fahrenheit_temp = [0]  # List to hold the converted Fahrenheit temperature
    celsius_to_fahrenheit(celsius_temp, fahrenheit_temp)
    print(f"{celsius_temp}°C is {fahrenheit_temp[0]}°F")

    fahrenheit_temp_input = float(input("Enter temperature in Fahrenheit: "))
    celsius_temp_converted = [0]  # List to hold the converted Celsius temperature
    fahrenheit_to_celsius(fahrenheit_temp_input, celsius_temp_converted)
    print(f"{fahrenheit_temp_input}°F is {celsius_temp_converted[0]}°C")

def celsius_to_fahrenheit(celsius, fahrenheit):
    """Converts Celsius to Fahrenheit and updates the fahrenheit list."""
    fahrenheit[0] = (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit, celsius):
    """Converts Fahrenheit to Celsius and updates the celsius list."""
    celsius[0] = (fahrenheit - 32) * 5 / 9
main()
