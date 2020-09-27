first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

print("eggs")
print("\teegs")
print("\n\teegs")
print("\neegs")
print("spam\neggs\nspam and eggs\neggs and spam and spam and eggs. By the way, back slash t doesn't work without being on a new line")

print("Languages:\nPython\nC\nJavaScript")

# Python can look for extra whitespace on the right
# and the left sides of a string. To ensure that
# no whitespace exists at the right end of a string,
# use the rstrip() method (p22):
favorite_language = 'python '
favorite_language
favorite_language.rstrip()
favorite_language

