'''
factorialLog.py
ABSWP CH 11 
Racz 07/07/2020

Description: This program calculates the factorial of a number but implements logging to show its use.
    We put in 'logging.debug()' when we want to print log information.

'''

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s \
-  %(message)s')

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n+1):
        total *= i
        logging.debug('i is ' + str(i) + ' , total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
