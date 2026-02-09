def right_justify(string):
    spaces = len('123456789_'*6) - len(string)
    print(' '*spaces+string)
right_justify('monty')
print('123456789_'*6)
