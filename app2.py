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
    print( 'you are ' + f'{kg}' + 'kilo')# WE CAN SIMPLY USE A FORMATTED STRING f 'you are ...'
#WhileLoops
i=1
j=2
while i<=5:
    print('*' * i)
    print('*' * j)
    i=i+1
    j=j+2
print('done')
#Game 1
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
# Game 2
action=""
car_started=False
while True:
    action = input('>').lower().strip()
    if action == 'help':
        print(''' 
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif action == 'start':
        if car_started:
           print('car already started')
        else:
            car_started=True
            print('starting the car....')
    elif action == 'stop':
        if not car_started:
           print('car already stopped')
        else:
            car_started=False
            print('stopping the car....')
    elif action == 'quit':
        print('Exiting the program.')
        break # to make it quit, we used the break
    else:
        print('I do not understand.')
#For loops
for item in ['Hindi', 'kubra']:
    print(item)
for items in range(6,10, 2): #here 2 i s step
   print(items)# 10 is not included
prices=[10,20,30]
total = 0
for price in prices:
    total += price
print(f'total: {total}')
#Nested loop
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
# CHALLENGE
numbers=[5,2,5,2,2]
for num in numbers:
      print('*' * num )
# one solution, but with nested
numbers=[5,2,5,2,2]
for num in numbers:
    output=''
    for count in range (num):
      output += '*'
    print(output)
# print an L
numbers=[2,2,2,2,7]
for num in numbers:
    l = ''
    for count in range(num):
        l += '*'
    print(l)
#Lists
names=['kubra', 'sumru', 'sevilay']
names[0]='Kubra'
print(names[-1]) # the last
print(names[0:2])# they simply print the new list"""
#practice finding the largest number in the list
basket = [20, 35, 10, 69]
maxi = basket[0]  # Initialize maxi with the first element
for numbers in basket:
    if numbers > maxi:
        maxi = numbers  # Update maxi if the current number is greater
print(f'This is the max: {maxi}')
#more questions on list
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list_n=[]
for i in range (len(list1)):#or we can use for i1
        combined= list1[i]+list2[i]
        list_n.append(combined)
print(list_n)
#square of number
numbers = [1, 2, 3, 4, 5, 6, 7]
list_square=[]
for i in range (len(numbers)):
    square=numbers[i]*numbers[i]
    list_square.append(square)
print(list_square)
#concatenate two lists
list3= ["Hello ", "take "]
list4 = ["Dear", "Sir"]
list_new=[]
for i, j in zip(list3,list4):
    combin=i + j
    list_new.append(combin)
print(list_new)
#or
res=[i+j for i in list3 for j in list4]
print(res)
#remove empty set
["Mike", "Emma", "Kelly", "Brad"]
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)