def is_palindrome(phrase):
    phrase = phrase.lower().replace(" ", "")
    return phrase == phrase[::-1]

input_phrase = input("Enter a phrase: ")
if is_palindrome(input_phrase):
    print("The phrase is a palindrome")
else:
    print("The phrase is not a palindrome")
