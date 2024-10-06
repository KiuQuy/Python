import string

text = string.ascii_lowercase
for char in text:
    for char1 in text:
        if (char == char1):
            pass
        else:
            print(char, char1, sep='')
            

            