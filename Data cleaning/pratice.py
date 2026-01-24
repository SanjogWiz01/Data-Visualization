name1 = "  Ram Sharma  "
name2 = "sita khadka"
name3 = "Bishal Thapa"
name4 = "nepal is beautiful"

print("Original Strings:")
print(name1)
print(name2)
print(name3)
print(name4)

print("\n--- upper() ---")
print(name2.upper())
print(name4.upper())

print("\n--- lower() ---")
print(name3.lower())
print(name1.lower())

print("\n--- isupper() ---")
print("RAM".isupper())
print(name3.isupper())

print("\n--- islower() ---")
print("sita".islower())
print(name2.islower())

print("\n--- len() ---")
print("Length of name1:", len(name1))
print("Length of name3:", len(name3))

print("\n--- startswith() ---")
print(name3.startswith("Bishal"))
print(name2.startswith("sita"))
print(name4.startswith("Nepal"))

print("\n--- split() ---")
words1 = name3.split(" ")
words2 = name4.split(" ")
print(words1)
print(words2)

print("\n--- find() ---")
print("Index of 'Thapa' in name3:", name3.find("Thapa"))
print("Index of 'beautiful' in name4:", name4.find("beautiful"))
print("Index of 'Kathmandu' in name4:", name4.find("Kathmandu"))

print("\n--- strip() ---")
clean_name1 = name1.strip()
print("Before strip:", repr(name1))
print("After strip:", repr(clean_name1))

print("\n--- replace() ---")
new_sentence1 = name4.replace("beautiful", "amazing")
new_sentence2 = name3.replace("Thapa", "Gurung")
print(new_sentence1)
print(new_sentence2)

print("\n--- Combined Examples ---")
full_name = "  Hari Prasad Pokhrel  "
print("Original:", repr(full_name))

full_name = full_name.strip()
print("After strip:", full_name)

full_name_upper = full_name.upper()
print("Upper case:", full_name_upper)

full_name_lower = full_name.lower()
print("Lower case:", full_name_lower)

print("Starts with Hari:", full_name.startswith("Hari"))
print("Is upper:", full_name.isupper())
print("Is lower:", full_name.islower())
print("Length:", len(full_name))

parts = full_name.split(" ")
print("Split into parts:", parts)

index_prasad = full_name.find("Prasad")
print("Index of Prasad:", index_prasad)

new_name = full_name.replace("Pokhrel", "Adhikari")
print("After replace:", new_name)

print("\n--- Multiple Test Strings ---")
names = [
    "  Suman Karki  ",
    "Nisha Rai",
    "bikash lama",
    "ROHIT SHRESTHA"
]

for n in names:
    cleaned = n.strip()
    print("\nOriginal:", repr(n))
    print("Cleaned:", cleaned)
    print("Upper:", cleaned.upper())
    print("Lower:", cleaned.lower())
    print("Is Upper:", cleaned.isupper())
    print("Is Lower:", cleaned.islower())
    print("Length:", len(cleaned))
    print("Starts with S:", cleaned.startswith("S"))
    print("Split:", cleaned.split(" "))
    print("Find 'a':", cleaned.find("a"))
    print("Replace a with @:", cleaned.replace("a", "@"))

print("\nAll string operations completed successfully.")
