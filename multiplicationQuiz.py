#Multiplication quiz
#ABSWP CH 8
#06/15/2020 Racz
#
#Special methods used: Regexes, pyinputplus for timing an input/allowing correct answers, string formatting
# 
# Description: This program will pick two numbers randomly(n and m) and ask the user on screen what n x m is.
# To check the answer given, it uses regexes and pyinputplus to allow and block certain answers. Used as a good-looking if/else, the pyinputplus 
#  helps to also have a time limit for the user inputs.
#After 10 questions the quiz will output


import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    #Pick two random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (questionNumber,num1,num2)

    try:
        #Right answers are handled by the allowRegexes
        #Wrong answers are handled by blockRegexes, with a custom message.
        #pyip.inputStr(prompt, allowRegexes =['^%S$' %(num1 * num2)], \
        #            blockRegexes=[('.*','Incorrect!')],timeout = 8, limit = 3)
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                              blockRegexes=[('.*', 'Incorrect!')],
                              timeout=8, limit=3)
    except  pyip.TimeoutException:
        print('Out of Time!')
    except pyip.RetryLimitException:
        print('Out of Tries!')
    else:
        #This block rujns if no exceptions in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) #Brief pause to let user see result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
