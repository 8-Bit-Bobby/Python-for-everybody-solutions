# Write a program to prompt for a score between 0.0 and 1.0. If the number is out of range, print an error message.
# If the score is between 0.0 and 1.0, print out the grade using table in book.

try:
    score = float(input('Enter score: '))
except:
    print('Bad score')
    quit()
    
if score >= 1.0:
    print('Bad score')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')

    
    
