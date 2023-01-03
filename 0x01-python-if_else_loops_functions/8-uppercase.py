#!/usr/bin/python3
def uppercase(str):
    # Initialize an empty result string
    result = ""
    for c in str:
        # If the character is a lowercase letter, convert it to uppercase
        if ord(c) >= 97 and ord(c) <= 122:
            result += chr(ord(c) - 32)
        # Otherwise, just append the character to the result
        else:
            result += c
    # Print the result and add a new line
    print("{}\n".format(result))
