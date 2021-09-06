print("This is the blood_database.py module")
print("It's name is {}".format(__name__))

import blood_calculator
#import interface as i
#from interface import check_HDL
#from interface import *                 # * means load everything from interface. This is generally bad form

answer1 = blood_calculator.check_HDL(55)
print("The analysis of 55 HDL is {}".format(answer1))

answer2 = blood_calculator.check_LDL(200)
print("The analysis of 200 LDL is {}".format(answer2))