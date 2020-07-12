'''
ABSWP CH11
boxPrint.py
Racz 07/07/2020
Description: This program will print a box in the output. It is a test for 'raise Exception()'.
    This would be useful to stop a program if a user gives a valid input but does NOT crash the program.
    In it, the program 'knows' how to handle the exception.

'''


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <=2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol*width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
    
#Example Boxes Below
for sym,w,h in (('*', 4,4),('O',20,5),('x',1,3),('ZZ',3,3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err:
        print('An exception happened: ' + str(err))
