a = input("enter value of a: ")
b = input("enter value of b: ")

# breakpoint()

def add(num1,num2):
	print("inside the function")
	return int(num1)+int(num2)
result = add(a,b)
print(result)