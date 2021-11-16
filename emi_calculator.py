module_name = "EMI Calculator in module"
second_variable = "Second variable"

def emi_calc(price,tenure=12):
    emi = price/tenure
    return emi
    
def test_funct():
    print("test")