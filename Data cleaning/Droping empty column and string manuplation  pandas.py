import pandas as pd
import numpy as np

data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Sanjog', 'Anil', 'Rita', 'Kiran', 'Sita', 'Hari', 'Gita', 'Ram', 'Shyam', 'Nina'],
    'Age': [19, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Gender': ['M', np.nan, 'F', 'M', np.nan, 'M', 'F', 'M', np.nan, 'F'],
    'Department': ['CEO', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [100000000, 25000, 40000, 32000, 28000, 35000, 37000, 31000, 29000, 33000]
}

df = pd.DataFrame(data)
df['City']=np.nan
print(df,'\n\n\n')
q=df.dropna(how='all',axis=0,inplace=True)
print(q,'\n\n\n\n\n')
# for only string
a=df.astype('string')
print(a,'\n\n\n\n')
# srting can be upper case and lower case at once time
print(df['Name'].str.lower())
print(df['Name'].str.upper())
# for strip
print(df['Name'].str.strip())
# more
# capitalize()    -> Converts first character to uppercase, rest to lowercase
# lower()         -> Converts all characters to lowercase
# upper()         -> Converts all characters to uppercase
# title()         -> Converts first character of each word to uppercase
# swapcase()      -> Swaps the case of each character
# strip()         -> Removes leading and trailing whitespaces
# lstrip()        -> Removes leading whitespaces
# rstrip()        -> Removes trailing whitespaces
# replace()       -> Replaces a substring with another substring
# split()         -> Splits the string into a list by a delimiter
# join()          -> Joins elements of a list into a string with a delimiter
# find()          -> Returns index of first occurrence of a substring (-1 if not found)
# rfind()         -> Returns index of last occurrence of a substring (-1 if not found)
# index()         -> Returns index of first occurrence of a substring (error if not found)
# rindex()        -> Returns index of last occurrence of a substring (error if not found)
# count()         -> Counts the occurrences of a substring
# startswith()    -> Returns True if string starts with specified substring
# endswith()      -> Returns True if string ends with specified substring
# isalpha()       -> Returns True if all characters are alphabetic
# isdigit()       -> Returns True if all characters are digits
# isalnum()       -> Returns True if all characters are alphanumeric
# isspace()       -> Returns True if all characters are whitespace
# len()           -> Returns the length of the string
# Original DataFrame column: df['Name']

print(df['Name'].str.capitalize(), '\n\n\n')   # Converts first character to uppercase, rest to lowercase

print(df['Name'].str.lower(), '\n\n\n')        # Converts all characters to lowercase

print(df['Name'].str.upper(), '\n\n\n')        # Converts all characters to uppercase

print(df['Name'].str.title(), '\n\n\n')        # Converts first character of each word to uppercase

print(df['Name'].str.swapcase(), '\n\n\n')     # Swaps the case of each character

print(df['Name'].str.strip(), '\n\n\n')        # Removes leading and trailing whitespaces

print(df['Name'].str.lstrip(), '\n\n\n')       # Removes leading whitespaces

print(df['Name'].str.rstrip(), '\n\n\n')       # Removes trailing whitespaces

print(df['Name'].str.replace('a', '@'), '\n\n\n')  # Replaces a substring with another substring

print(df['Name'].str.split(), '\n\n\n')        # Splits the string into a list by whitespace

print(df['Name'].str.join('-'), '\n\n\n')      # Joins characters of string using '-' as delimiter

print(df['Name'].str.find('a'), '\n\n\n')      # Returns index of first occurrence of 'a' (-1 if not found)

print(df['Name'].str.rfind('a'), '\n\n\n')     # Returns index of last occurrence of 'a' (-1 if not found)

print(df['Name'].str.count('a'), '\n\n\n')     # Counts the occurrences of 'a'

print(df['Name'].str.startswith('S'), '\n\n\n') # Returns True if string starts with 'S'

print(df['Name'].str.endswith('g'), '\n\n\n')   # Returns True if string ends with 'g'

print(df['Name'].str.isalpha(), '\n\n\n')      # Returns True if all characters are alphabetic

print(df['Name'].str.isdigit(), '\n\n\n')      # Returns True if all characters are digits

print(df['Name'].str.isalnum(), '\n\n\n')      # Returns True if all characters are alphanumeric

print(df['Name'].str.isspace(), '\n\n\n')      # Returns True if all characters are whitespace

print(df['Name'].str.len(), '\n\n\n')          # Returns the length of the string
