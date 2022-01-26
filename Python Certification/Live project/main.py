"""
a data file is given to you containing data like json structure
[
  {"name": "iphone11","price":  55000},
  {"name": "iphone11 Pro","price":  65000},
  {"name": "iphone11 Pro Max","price":  85000},
  {"name": "iphone12 mini","price":  65000},
  {"name": "iphone12","price":  75000},
  {"name": "iphone12 Pro","price":  85000},
  {"name": "iphone12 Pro Max","price":  95000},
  {"name": "iphone13","price":  85000},
  {"name": "iphone13 Pro","price":  95000},
  {"name": "iphone13 Pro Max","price":  105000},
],
 You have to create a add_product method which will add the product for a store class
 with product id

 Create search_product_by_name method
"""
import json

class Store:

	def __init__(self, store_name):
		self.name = store_name
		self.products = []

	def add_products(self):
		file = open('data.json', 'r')
		products_list = json.load(file)
		file.close()
		product_id = 0
		for product in products_list:
			product_id+=1
			product_data = {"id": product_id, "name": product["name"], "price": product["price"]}
			self.products.append(product_data)
		return self.products

	def search_product_by_name(self):
		search_name = input("Please Enter product name: ")
		for product in self.products:
			if product['name'] == search_name:
				return product
		else:
			return f"Product by name {search_name} does not available"

store = Store("Apple Store")
print(store.add_products())
print("Searching in the store for iphone11: ")
print(store.search_product_by_name())
print("Searching in the store for iphone15: ")
print(store.search_product_by_name())
