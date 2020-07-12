#SandwichMaker.py
#ABSWP Ch 8: End of Chapter Project
#
#Special Methods used: pyinputplus
#
#Description: Prompts the user for sandwich choices using pyinputplus method inputmenu. Afterwards prints out a string of their order with all selected items.
#
#

import pyinputplus as pyip

types_bread = ('wheat','white','sourdough')
types_protein = ('chicken','turkey','ham','tofu')
types_cheese = ('cheddar','swiss','mozzarella')
condiments = ('mayo','mustard', 'lettuce', 'tomato')
condimentList = []

bread = pyip.inputMenu(types_bread,prompt='What type of bread would you like?(wheat, white, sourdough)\n')
protein = pyip.inputMenu(types_protein,prompt='What type of protein? (chicken, turkey, ham, tofu)\n')
cheeseYa = pyip.inputYesNo('Would you like cheese? \n')

if cheeseYa == 'yes':
    cheese = pyip.inputMenu(types_cheese,'What type of cheese would you like? (cheddar, swiss, mozzarella)\n')

for condiment in condiments:
    toppings = pyip.inputYesNo('Would you like %s ? \n' % condiment)
    if toppings == 'yes':
        condimentList.append(condiment)

print('So your sandwich is a ' + protein + ' on ' + bread + ' with ' + cheese + ' and ' + ', '.join(condimentList) +'.')
