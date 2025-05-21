import pyjokes

amount = input('Enter The Amount: ')
amount = int(amount)

for i in range(amount):
    joke = pyjokes.get_joke()
    if (joke):
        print(joke +' \n');
    else:
        print('Internet Problem')

# Single Line Comment - As You Can See '#' for a single line comment

"""
For Multi-line comment use triple double-cout or single cout 

So This is a multi-line comment
"""