# Hello folks. Its a real-life based project, A very basic one made with the help of Random module in Python.

# Here you can generate a strong password for your neccessary files. :)

import string
import random

s1 = string.ascii_uppercase
s2 = string.punctuation
s3 = string.ascii_lowercase
s4 = string.digits

plen = int(input("Kindly enter the length of your password:\n"))

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
print("Your generated password is:")
print("".join(s[0:plen]))
