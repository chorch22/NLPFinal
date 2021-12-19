import os
import sys
import string
#lower case, get rid of punctuation and extra spaces

lowered = input().lower()

punct = "".join([char for char in lowered if char not in string.punctuation])

final = " ".join(punct.split())

print(final)

