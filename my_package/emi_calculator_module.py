module_name1 = "EMI Calculator in module"
second_variable1 = "Second variable"

def emi_calc1(price,tenure=12):
    print("module 1")
    emi = price/tenure
    return emi
    
def test_funct1():
    print("module 1 test")
    print("test")