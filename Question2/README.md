Q2) Below is a link to a spreadsheet with two columns A and B such that:
A is the input
B is the output

Based on the spreadsheet, there exist a function such as  f that relates A to B which is:

Bi = f(Ai)
Where i is the row number of the spreadsheet.
For example:
	
For row i = 1: 				 f(15840) = cGp
For row i = 2:				f(16465) = cmW
For row i = 3:				f(17941) = cX3

Embedded Software Engineer Quiz Resource


Q2 a) First task is to find function f(Ai) using these sets of points in the spreadsheet.

Q2 b) Once the f(Ai) is found, what would be the output for the following inputs?
f(30001) = ?
f(55555) = ?
f(77788) = ?

Q2 c) What is the upper limit or maximum range of this function before there will be collisions or overflow? 

Q2 d) The first three parts are mostly mathematical and once you find the solution, you realize you need your programming skills to solve these questions completely.
Therefore, please share any code that you write in the process of solving the above problems.

Hint 1: One must have a good idea about the domain and the range of the function f.
Hint 2: There are patterns within the spreadsheet that can help you find the function f.


Steps taken in solution:

Step 1: Identify differential behavior of A and B

    1.1: Take differences of every 2 samples in A and correlate them to changes in B.
     
    1.2: Identify relationship as proportional change in least signifant character of B everytime A changed by +/-1
     
    1.3: Treat relationship as linear

Step 2: Identify how many characters in number system

    2.1: Split strings in B into individual characters
    
    2.2: Flatten list and identify all unique characters and number of unique characters

Step 3: Investigate possibility of missing characters in dataset

    3.1: After finding 61 unique characters almost completing alphanumeric set, we investigate data for indication of a 62nd character
   
    3.2: Seeing that between i = 43 and i = 44 , B(43) = Tx2 and B(44) = Tn2 respectively we see that only the second char has changed
   
    3.3: From this we take the difference of A(44) and A(43) and identify that this difference must be a multiple of the number system base.
    A(44) - A(43) = 1054 which is a multiple of 62, but not 61, therefore B must be in Base62.

Step 4: Find encryption key
   
    4.1: From the data it is clear that the key does not follow conventional aphanumeric sequence
   
    4.2: We take all values of A and use remainder division to identify the value of each individual character
    and save that char in a List of size 62 indexed by the appropriate character value found
   
    4.3: We do this until we go through the entire dataset
   
    4.4: Finally since we know we are missing one character from 3.1 we assign the final character to '5' the only missing character in alphanumeric

Step 5: Program the encoding
   
    5.1: After finding the key which is C7xicPMGvzAZyTNodmwnV5D3B6H0Oup8E21W9sqLQX4YjSeUhIRJgafFtrKlbk we Base62 encode values of A with it
   
    5.2: Test against the entire dataset to verify the function and then find the values requested.

 Step 6: Answer the questions
   
    6.1: The answer to 2a) is written in the script but to reiterate,
    f(Ai) = BASE62(Ai, EncryptionKey = C7xicPMGvzAZyTNodmwnV5D3B6H0Oup8E21W9sqLQX4YjSeUhIRJgafFtrKlbk)
   
    6.2: The answer to 2b) is f(30001) = GIF , f(55555) = NOi , f(77788) = VNQ
   
    6.3: The answer to 2c) A must be all real positive integers and B must be unsigned alphanumeric characters
    without symbols, so long as this is maintained there should not be collisions or overflow

Signed: Faraz Jamil
