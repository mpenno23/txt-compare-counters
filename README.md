This script takes two .txt files and finds the difference in between one column from both files. It will retain the name of each row despite the difference operation.

For example:

File1.txt
apples-lost, 400
bananas-moldy, 600
potatos-squishy, 500

File2.txt
apples-lost, 550
bananas-moldy, 880
potatoes-squishy, 630

The script would take the values of each row of File2.txt and subtract them from the values of the rows of File1.txt. The name of the row and difference will be outputted to a file called "different.txt"

Example:
difference.txt
apples-lost, 50
Bananas-moldy, 280 
potatoes-squishy, 130


This script can be useful if one needs to compare how counters or variables have incremented overtime. 
