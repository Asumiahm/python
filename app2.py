""" weight_p=input( 'how much you weigh? ')
weight_k= 0.45* int(weight_p)
print(weight_k)
by=input('what is your birth year:')
#age=2024-by # error since int-str
age = 2024-int(by) # it coverts it to int
print(age) # it can not concatenate string with int
name=input('what is your name? ')
color=input('what color do you like? ')
print(name + ' likes ' + color)
course=''' how are you doing  
I wish you a happy life'''

sheet='hello test'

print(sheet[0])
print(sheet[0:5])# the 5 is not included
print(sheet[:])
first='john'
last='smith'
print(first + ' [' + last + '] '  +' is a coder')# the longer way
msg=f'{first} [{last}] is a coder' #formated string use {} to dynamically insert values to string
print(msg)
print(len(first))
#IF
price=1000000
is_good_credit=True
if is_good_credit:
    down_pay= 0.1 * price
else:
    down_pay=0.2 * price
print(f'${down_pay}')
#LOGIC
is_smart=True
is_girl=False
if is_smart and is_girl:
    print('I know her')
elif is_smart and not is_girl:
    print('I really do not know her')
#COMPARISION
# practice
name=input('What is your name:')
print('my name is :' + name)
length=len(name)
if length < 3:
    print('name must be at least 3 chars long')
elif length > 50:
    print('name can be a maximum of 50 chars')
else:
  print('name looks good!')
#practice for all
weight=input('weight:')# HERE WE CAN MAKE INT(INPUT)
choice=input('(L)bs or (k)g:')
if choice.lower() == 'l':
    lbs = int(weight) / 10
    print('you are' + f'{lbs}' +'lbs')
elif choice== 'k':
    kg = int(weight) - 50
    print( 'you are ' + f'{kg}' + 'kilo')# WE CAN SIMPLY USE A FORMATTED STRING f 'you are ...' """
#WhileLoops
i=1
j=2
while i<=5:
    print('*' * i)
    print('*' * j)
    i=i+1
    j=j+2
print('done')
#Game
numb = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('your guess: '))
    guess_count += 1
    if guess == numb:
        print('You won!')
        break
    elif guess < numb and guess_count < guess_limit:
        print('It\'s higher, try again')
    elif guess > numb and guess_count < guess_limit:
        print('It\'s lower, try again')
else:
    if guess != numb:
        print('You failed')
#game 3
