# PRINT ORIGINAL MESSAGE:

print (original)

#ACTUAL SOLUTION TO THE PROBLEM

original = str(input("Enter a string to hide in uppercase: "))

secret= ""

for char in original:

    secret += str(ord(char))

print("secret message: ", secret)

original = ''

for i in range(0, len(secret)-1,2):
    charcode = secret[i] + secret[i+1]

original += chr(int(charcode))

print("Actual_MESSAGE : ", original)

