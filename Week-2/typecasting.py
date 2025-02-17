# integer
age = 25
print(age)

# float
height = 1.75
print(height)

# typecasting

# float to int
decimal_number = 7.99
whole_number = int(decimal_number)
print(whole_number)

# let op dat de komma gewoon weggelaten wordt, dus afgerond naar beneden

# int to float
whole_number = 5
decimal_number = float(whole_number)
print(decimal_number)

# int en float naar string
age = 25
height = 1.75
age_str = str(age)
height_str = str(height)

print(age_str)
print(height_str)

# van string naar int en float
number_string = "45"
number_string_float = "45.6"
number = int(number_string)
number_float = float(number_string_float)
print(number)
print(number_float)

# user input en typecasting om te vermenigvuldigen
user_input = input("Enter a number: ")

# Convert the input to an integer for multiplication
user_number = int(user_input)

# Multiply the user input by 10
result = user_number * 10
print("Your number multiplied by 10 is:", result)

# Deden we geen typecasting dan kregen we een string concatenation
concatenated_result = user_input + "10"
print("Without conversion (string concatenation):", concatenated_result)