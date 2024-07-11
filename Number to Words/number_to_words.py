def number_to_words(num):
    units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return ' '.join(units[int(digit)] for digit in str(num))

number = int(input("Enter a number: "))
print(f"Number in words: {number_to_words(number)}")
