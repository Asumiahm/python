""" weightp=input( 'how much you weigh? ')
weightk= 0.45* int(weightp)
print(weightk)
by=input('what is your birth year:')
#age=2024-by # error since int-str
age = 2024-int(by) # it coverts it to int
print(age) # it can not concatenate string with int
name=input('what is your name? ')
color=input('what color do you like? ')
print(name + ' likes ' + color)
course=''' how are you doing  
i wish you a happy life'''
"""
sheet='hello test'

print(sheet[0])
print(sheet[0:5])# the 5 is not included
print(sheet[:])

