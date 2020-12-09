"""
For IGCSE Computer Science course
"""

no_of_letters = 0
text_letters = []
text_decimal = []

print("")
print("~~~ Checksum Calculator ~~~")
text = input("Enter text: ")

for letters in text:
    text_letters.append(letters)

while len(text_letters) != no_of_letters:
    text_decimal.append(ord(text_letters[no_of_letters]))
    no_of_letters = no_of_letters + 1

decimal = (sum(text_decimal)) % 256
hexadecimal = hex(decimal)

print(f"The checksum is {decimal} or {hexadecimal}.")

# USEFUL NOTES
print("")
print("Useful Notes")
# 'ord("")' convert any character into a decimal (Base 10) number.
a_to_decimal = ord("A")
print(f"The letter 'a' converts to '{a_to_decimal}' in Base 10.")
# 'hex()' converts a decimal numbre into a hexadecimal number.
decimal_to_hex = hex(65)            # Can also write 'hex(a_to_decimal)'.
print(f"The decimal '65' converts to '{decimal_to_hex}' in hexadecimal.")
# 'int("")' converts a string with decimal places into a Base 10 number but if you use 'int("", )' then
# it will convert from the Base that you type into Base 10.
hex_to_decimal = int("0x41", 16)    # Can also write 'int(decimal_to_hex, 16)'
print(f"The hexadecimal '0x41' converts to '{hex_to_decimal}' in Base 10.")