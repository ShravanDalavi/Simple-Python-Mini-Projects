def count_words(text):
    words = text.split()
    return len(words)

def word_count_tool():
    text = input("Enter some text: ")
    word_count = count_words(text)
    print(f"Word count: {word_count}")

word_count_tool()