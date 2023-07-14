"""A basic example of default arguments"""
# This function prompts user for a number of times until retries < 0
def prompt_user(promptQ, retries=3, reminder='Please try again'):
    while True:
        ok = input(promptQ)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
    
prompt_user('Do you like Python?')
