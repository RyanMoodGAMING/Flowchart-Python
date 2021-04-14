# Authenticate's the password


'''
Name of Function: Authenticate
Parameters: user, password
Return Value: True/Fale
What it does: Authenticate's the password
'''
def Authenticate(user, password):
    us = ['dave', 'alice', 'bob']
    ps = ['adf32', 'woof2006', '!@34E$']
    z = 0
    correct = False
    while z < 3:
        if user == us[z]:
            if password == ps[z]:
                correct = True
        z = z + 1
    return correct
