temperature = float(input("Enter the temperature: "))
source_scale = input("Enter the source scale (F or C): ")
# Perform the conversion
if source_scale == 'F':
    # Convert from Fahrenheit to Celsius
    celsius = (temperature - 32) * 5/9
    print(f"Temperature in Celsius: {celsius: .2f}")
elif source_scale == 'C':
    # Convert from Celsius to Fahrenheit
    fahrenheit = (temperature * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit: .2f}")
else:
    print("Invalid scale")
    print("Please enter 'F' for Fahrenheit or 'C' for 'Celsius'")