import random
import string

# Define the characters to be used in the password
total = string.ascii_letters + string.digits + string.punctuation

# Set the length of the password
length = 16

# Generate a random password
password = "".join(random.sample(total, length))

# Print the generated password
print(password)
