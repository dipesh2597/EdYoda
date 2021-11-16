#directly import module
import my_package.emi_calculator_module # == from my_package impory emi_calculator_module
#then use method/variable
# print(emi_calculator.module_name, emi_calculator.second_variable)

#import method or varibale from module
# from emi_calculator import module_name, second_variable
# print(emi_calc(48000,12))
# print(module_name, second_variable)

# from my_package.emi_calculator_module import module_name, second_variable

#import everything 
from my_package import *

# from emi_calculator import *
print("Line number 14",emi_calculator_module.module_name1, emi_calculator_module.second_variable1)
print("Line number 15",emi_calculator_module.emi_calc1(24000,12))
emi_calculator_module.test_funct1()