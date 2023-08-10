# Imports
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from sqlalchemy.engine.row import RowMapping

# Create an app with flask
app = Flask(__name__)
# Open the 'store.db' database with sqlite
engine = create_engine("sqlite:///store.db")

def to_dict(row):
    """
    Convert rows or lists of rows to dictionaries of list or dictionaries respectively
    :param row: row to transform
    """
    if type(row) == RowMapping:
        return dict(row)
    elif type(row) == list:
        return [dict(row) for row in row]
    
# EXERCISE 1
@app.route('/warehouses')
def get_warehouses():
    """
    Endpoint in link 'http://127.0.0.1:8080/warehouses' to list all warehouses in JSON format
    """

    query = """
    SELECT *
    FROM warehouses
    """

    with engine.connect() as connection:
        result = connection.execute(query)
        warehouses = result.mappings().fetchall()

        return jsonify(to_dict(warehouses)), 201
    

# EXERCISE 2
@app.route('/stock/<int:warehouse_id>')
def get_stock(warehouse_id):
    """
    Endpoint in link 'http://127.0.0.1:8080/stock/<warehouse_id>' to list all the stock in warehouse id == warehouse_id in JSON format
    """

    query = f"""
    SELECT product_id, quantity
    FROM stock
    WHERE warehouse_id = {warehouse_id}
    
-- Combine results of first query with total quantity for warehouse
    UNION ALL
    
-- Select NULL as product_id, naming it 'TOTAL', and sum the total quantity for warehouse.
    SELECT 'TOTAL', SUM(quantity)
    FROM stock
    WHERE warehouse_id = {warehouse_id}
    """

    with engine.connect() as connection:
        result = connection.execute(query)
        stock = result.mappings().all()

        return jsonify(to_dict(stock)), 201


# EXERCISE 3
@app.route('/stock/<int:warehouse_id>/<int:product_id>')
def stock_wareID_prodID(warehouse_id, product_id):
    """
    Endpoint in link 'http://127.0.0.1:8080/stock/<warehouse_id>/<product_id>' to list all the stock of one particular product == product_id in warehouse id == warehouse_id in JSON format
    """

    query = f"""
    SELECT product_id, name, warehouse_id, quantity
    FROM stock
    JOIN products ON id = {product_id}
    WHERE product_id = {product_id} AND warehouse_id = {warehouse_id};
    """

    with engine.connect() as connection:
        result = connection.execute(query)
        stock = result.mappings().all()

        return jsonify(to_dict(stock)), 201


# EXERCISE 4
@app.route('/sales', methods=['POST'])
def create_sale():
    """
    Endpoint in link 'http://127.0.0.1:8080/sales' that with a post method is able to create a sale in the sales db
    """

    sale = request.get_json()

    query = f"""
    INSERT INTO sales (id, product_id)
    SELECT COALESCE(MAX(id), 0) + 1, {sale['product_id']} FROM sales;
    """

    with engine.connect() as connection:
        connection.execute(query)

        return jsonify(sale), 201

# EXERCISE 5
@app.route('/products')
def products():
    """
    Endpoint in link 'http://127.0.0.1:8080/products' to list all the products in a JSON format
    """

    query = f"""
    SELECT *
    FROM products
    """

    with engine.connect() as connection:
        result = connection.execute(query)
        products = result.mappings().fetchall()
        
        return jsonify(to_dict(products)), 201


# EXERCISE 6
@app.route('/sales/<int:product_id>')
def all_sales(product_id):
    """
    Endpoint in link 'http://127.0.0.1:8080/sales/<product_id>' to list all the sales of a particular product in a JSON format
    """

    query = f"""
        SELECT product_id AS id, name, price, COUNT(product_id) AS total_sales, (COUNT(product_id)*price) AS gross_sales
        FROM (sales LEFT JOIN products ON sales.product_id = products.id)
        WHERE product_id={product_id}
    """

    with engine.connect() as connection:
        result = connection.execute(query)
        products = result.mappings().fetchone()
        
        return jsonify(to_dict(products)), 201


# Run the app
app.run(debug=True, port=8080)


