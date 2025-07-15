def convert(words):
    if ":)" in words:
        words = words.replace(":)", "🙂")
    if ":(" in words:
        words = words.replace(":(", "🙁") 
    return words

user_word = input("Enter words: ")
conversion = convert(user_word)
print(conversion)       