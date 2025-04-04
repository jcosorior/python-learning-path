# indexing = accessing elements of a sequence using 
#            [start : end : step] the ending index is exclusive the start index is inclusive
# steo we can access the characters in a string by a given step, we can count by twos or by threes
#credit_number = "1234-5678-9012-3456"

#print(credit_number[4])
#print(credit_number[0:4])
#print(credit_number[:4])
#print(credit_number[5:9])

#print(credit_number[5:]) #if you need everything up to the end of the string you don`t need to list an ending index just be sure to add that colon
#print(credit_number[-3]) #you can use negative index to, it goes from te end of the string to the begining of the string


#print(credit_number[::2]) #step example [start:end:step], here we put it blank spaces, so python it has to count everything from the begginning of the sting to the end, and the step would be 2
                          # that would print every second character within our string  (starting from the character position 0 )

# Let`s create a program to get the last 4 four digits of a credit card number

credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(last_digits)

#lets reverse the characters of the string 
credit_number2 = "1234-5678-9012-3456"
credit_number2 = credit_number2[::-1]
print(credit_number2)