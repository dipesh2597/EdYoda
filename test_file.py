#directly import module
# import emi_calculator
#then use method/variable
# print(emi_calculator.module_name, emi_calculator.second_variable)

#import method or varibale from module
# from emi_calculator import module_name, second_variable
# print(emi_calc(48000,12))
# print(module_name, second_variable)


#import everything 
from emi_calculator import *
print("Line number 14",module_name, second_variable)
print("Line number 15",emi_calc(24000,12))
test_funct()