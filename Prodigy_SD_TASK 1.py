# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 09:58:06 2024

@author: THRISHA DAS
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature(value, unit):
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    elif unit == 'K':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    else:
        raise ValueError("Unknown unit")

def main():
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()
        
        if unit not in ['C', 'F', 'K']:
            raise ValueError("Invalid unit. Please enter C, F, or K.")
        
        converted_values = convert_temperature(value, unit)
        
        if unit == 'C':
            print(f"{value}°C is equal to {converted_values[0]:.2f}°F and {converted_values[1]:.2f}K")
        elif unit == 'F':
            print(f"{value}°F is equal to {converted_values[0]:.2f}°C and {converted_values[1]:.2f}K")
        elif unit == 'K':
            print(f"{value}K is equal to {converted_values[0]:.2f}°C and {converted_values[1]:.2f}°F")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()