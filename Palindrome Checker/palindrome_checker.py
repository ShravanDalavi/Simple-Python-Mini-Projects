def is_palindrome(word):
    return word == word[::-1]

def palindrome_checker():
    word = input("Enter a word: ")
    
    if is_palindrome(word):
        print(f"'{word}' is a palindrome!")
    else:
        print(f"'{word}' is not a palindrome.")

palindrome_checker()
