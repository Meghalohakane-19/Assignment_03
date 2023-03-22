# Calculate the Upper and The lower Case

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# Sample String : 'The quick Brow Fox'
# Expected Output :

# No. of Upper case characters : 3
# No. of Lower case Characters : 12

s = input("Enter the string :")
def substring(s):
    x = 0
    y = 0
    for i in s :
        if i >='a' and i<='z':
           x +=1
        if i >='A' and i<='Z':
           y += 1

    print("No. of upper_case characters : ",y)
    print("No. of lower_case characters: ",x)

substring(s)

# substring = 'The quick Brow Fox'
# substring.isupper() 
# print("isupper:",substring)