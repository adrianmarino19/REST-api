#%%
import requests


def exercise_1(): 
    url = 'http://127.0.0.1:8080/warehouses'
    warehouses = requests.get(url)
    return warehouses.json()

def exercise_2(warehouse_id):
    url = f'http://127.0.0.1:8080/stock/{warehouse_id}'
    stock_wareId = requests.get(url)
    return stock_wareId.json()

def exercise_3(warehouse_id, product_id):
    url = f'http://127.0.0.1:8080/stock/{warehouse_id}/{product_id}'
    stock_prodId_wareId = requests.get(url)
    return stock_prodId_wareId.json()

def exercise_4(product_Id_sold):
    # Sale to create in the db
    sale = {'product_id': product_Id_sold}

    # Post the dictionary in JSON format to the right sales URL
    request = requests.post('http://127.0.0.1:8080/sales', json = sale)
    return request

def exercise_5():
    url = 'http://127.0.0.1:8080/products'
    products = requests.get(url)
    return products.json()

def exercise_6(product_id):
    url = f'http://127.0.0.1:8080/sales/{product_id}'
    sale_product = requests.get(url)
    return sale_product.json()
#%%
# Exercises tryouts
print('EXERCISE 1')
print(exercise_1())
print('\n')
print('EXERCISE 2')
print(exercise_2(2))
print('\n')
print('EXERCISE 3')
print(exercise_3(2,4))
print('\n')
print('EXERCISE 4')
print(exercise_4(5))
print('\n')
print('EXERCISE 5')
print(exercise_5())
print('\n')
print('EXERCISE 6')
print(exercise_6(5))
print('\n')


# %%
