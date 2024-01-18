import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import io

df = pd.read_csv(io.StringIO(uploaded['FuncData.csv'].decode('utf-8')), header = None)
npl = df.to_numpy()

BASE62 = FullKey
#Uncomment if running first
# BASE62 = "C7xicPMGvzAZyTNodmwnV5D3B6H0Oup8E21W9sqLQX4YjSeUhIRJgafFtrKlbk"

#Answer to Q2 a)
def encode(num, alphabet=BASE62):
  # Basic encoding script for variable base
  # Optimized version from FindingKey.py
    if num == 0:
        return alphabet[0]
    arr = []
    arr_append = arr.append  # Extract bound-method for faster access.
    _divmod = divmod  # Access to locals is faster.
    base = len(alphabet)
    while num:
        num, rem = _divmod(num, base)
        arr_append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def decode(string, alphabet=BASE62):
  # Basic encoding script for variable base
  # Optimized version from FindingKey.py
    base = len(alphabet)
    strlen = len(string)
    num = 0
    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

#Function tests against entire dataset with prints
#Uncomment to test against
# for set in npl:
#   encoded = encode(set[0])
#   print(encoded, "=", set[1], "", encoded == set[1])

# for set in npl:
#   decoded = decode(set[1])
#   print(decoded, "=", set[0], "", decoded == set[0])

print("Question 2b")
print("f(30001) = ", encode(30001)) #GIF
print("f(55555) = ", encode(55555)) #NOi
print("f(77788) = ", encode(77788)) #VNQ

print("Question 2c")
print("The limitations of this function are only that A must be all real positive integers and that B represents unsigned values and also represents positive integer values")
print("The function is not approximated, it is encoding a decimal (base10) value into base62 with the base 62 character key being defined and decoded above")
print("So long as the function remains within these conditions the only overflow will come from the system decoding it")
