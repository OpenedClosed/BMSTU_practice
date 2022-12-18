string = input()
help_string = input()
for word in string.split():
    if help_string.lower() in word.lower():
        print(word)