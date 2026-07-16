# palindrome_checker.py

import re

def is_palindrome(s):
    # Remove space, punctuation, make all lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

def main():
    s = input("Enter text: ")
    if is_palindrome(s):
        print("Palindrome")
    else:
        print("Not palindrome")

if __name__ == "__main__":
    main()
