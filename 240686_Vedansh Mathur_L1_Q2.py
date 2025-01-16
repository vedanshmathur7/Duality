# Create a program that counts the frequency of a given digit in a number. The program should work for multi-digit numbers and handle edge cases.

number =(input ("Enter the no. : "))
no = (input ("Enter the no. present in the given no., to find the frequency of : "))
frequency = 0
for i in number:
    if (i == no):
        frequency += 1

print (f"Frequency: {frequency}")