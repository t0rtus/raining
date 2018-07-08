# this program asks questions to find out whether to go outside
import random # include library to randomize rain occurrence

print('Hello! Will you go outside today?')

answer = '' # define blank answer string

while answer != 'y' and answer != 'n': # maintain loop unless answer is y or n
    print('Is it raining? (y/n)')
    answer = input()
    if answer != 'y' and answer != 'n':
        print('Please answer with "y" or "n".')

if answer == 'n': # no rain
    print('Going outside.') # end of program
elif answer == 'y':
    answer = '' # blank answer string
    rain = 1 # define int rain as 1 (true)
    while answer != 'y' and answer != 'n': # maintain loop unless answer is y/n
        print('Have you got an umbrella? (y/n)')
        answer = input()
    if answer != 'y' and answer != 'n':
        print('Please answer with "y" or "n".')

    if answer == 'y': # means to deal with rain
        print('Going outside.') # end of program
    elif answer == 'n':
        answer = '' # blank answer string
        while answer != 'n' and rain == 1: # maintain loop whilst rain is 1 and unless answer is n
            print('Wait a while?')
            answer = input()
            rain = random.randint(0, 1) # assign rain random value of 0 or 1
            if answer != 'y' and answer != 'n':
                print('Please answer with "y" or "n".')
            elif answer != 'n' and rain == 0: # if answer isn't n and rain is 0
                print('It has stopped raining.')
            elif rain == 1:
                print('It is still raining.')
                
        if answer == 'n':
            print('Staying inside today.')
        else:
            print('Going outside.')
