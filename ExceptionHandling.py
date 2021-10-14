#1
'''Write a function to compute 5/0 and use try/except to catch the exceptions.'''
def _exception_():
    try:
        5/0
    except Exception as e:
        print(e)
_exception_()

#2
'''Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].'''

subjects = ["Americans ","Indians"]
verbs = ["play","watch"]
objects = ["Baseball","Cricket"]

for sub in subjects:
    for ver in verbs:
        for obj in objects:
            print(sub,ver,obj)