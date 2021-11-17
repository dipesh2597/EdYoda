module_name2 = "EMI Calculator in module"
second_variable2 = "Second variable"

def emi_calc2(price,tenure=12):
    print("module 2")
    emi = price/tenure
    return emi
    
def test_funct2():
    print("module 2 test")
    print("test")