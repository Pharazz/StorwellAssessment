import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

# Importing Data into Numpy List
df = pd.read_csv(io.StringIO(uploaded['FuncData.csv'].decode('utf-8')), header = None)
npl = df.to_numpy()

# Looking for trends in data by seeing differences between values of A
diff = [0] * len(npl)
for i in range(0, len(npl) - 1):
  diff[i+1] =  npl[i+1,0] - npl[i,0]

print(diff)
print("Looking at the differences we find that for any change +/- 1 of A, B changes accordingly \nIndicating  a linear relationship")

# Split each string into its own column
# Look for unique characters
split_array = np.array([list(s) for s in npl[:,1]])

print("Unique characters in B:")
print(np.unique(split_array.flatten()))
print("Number of Unique Characters: ")
print(len(np.unique(split_array.flatten())))

# Proof of Base 62 over Base 61
print("Data sequence over 
print(npl[43])
print(npl[44])
# Only sequence of data where difference is exactly one character
# Base of number system must be a factor of this difference

print(npl[44,0]-npl[43,0])

print("61 is not a factor of 1054 therefore the encoding base must be 62")
print("62 is a factor of 1054, therefore the missing 5 must be part of the cipher key")

# Since we know data is linear and base 62 we use spreadsheet data and remainder division
# to assign 61 of the 62 characters the appropriate values in our key

# Initialize Key and Base62 trackers
KeySet= [None] * 62
Result = 0
Remainder = 0

# Hardcoded to work on datarange provided
for Set in npl:
  Result, Remainder = divmod(Set[0],62)
  KeySet[Remainder] = Set[1][2]
  Result, Remainder = divmod(Result,62)
  KeySet[Remainder] = Set[1][1]
  Result, Remainder = divmod(Result,62)
  KeySet[Remainder] = Set[1][0]

# Now we append the missing 5 to the remaining position
KeySet[KeySet.index(None)] = '5'

# Output key as a string
FullKey = ''.join(KeySet)
print(FullKey) #Key is: C7xicPMGvzAZyTNodmwnV5D3B6H0Oup8E21W9sqLQX4YjSeUhIRJgafFtrKlbk
