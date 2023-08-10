# REST-API Assignment

<!-- vscode-markdown-toc -->
* 1. [Exercises](#Exercises)
	* 1.1. [Exercise 1](#Exercise1)
	* 1.2. [Exercise 2](#Exercise2)
	* 1.3. [Exercise 3](#Exercise3)
	* 1.4. [Exercise 4](#Exercise4)
	* 1.5. [Exercise 5](#Exercise5)
	* 1.6. [Exercise 6](#Exercise6)
	* 1.7. [Exercise 7](#Exercise7)
* 2. [Grading](#Grading)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

The goal for this assignment is to create a REST API for an ecommerce platform.

The database already exists in the project, you don't need to change its schema,
you'll just need to `SELECT`, `INSERT`, `UPDATE`, and `DELETE` from it.



##  1. <a name='Exercises'></a>Exercises

###  1.1. <a name='Exercise1'></a>Exercise 1

Create an endpoint in the API (`api.py`) to list all warehouses.  It should return a JSON list.

###  1.2. <a name='Exercise2'></a>Exercise 2

Create an endpoint in the API to show the stock of all products in a particular warehouse.

###  1.3. <a name='Exercise3'></a>Exercise 3

Create an endpoint in the API to show the stock of one particular products in a particular warehouse.

###  1.4. <a name='Exercise4'></a>Exercise 4

Create an endpoint in the API to create a sale.

###  1.5. <a name='Exercise5'></a>Exercise 5

Create an endpoint in the API to list all products.

###  1.6. <a name='Exercise6'></a>Exercise 6

Create an endpoint in the API to return all sales by a particular product.  This
endpoint should return a JSON object with  the following shape:

```json
{
    "id": int,
    "name": string,
    "price": float,
    "total_sales": int,
    "gross_sales": float # this should be the sum of all sales
}
```

###  1.7. <a name='Exercise7'></a>Exercise 7

Create a function in `client.py` for each one of the previous exercises, calling
the respective endpoint in the REST API.

##  2. <a name='Grading'></a>Grading

| **section**      | **grade**     |
|--------------|-----------|
| Exercises 1-5 | 1.5 point|
| Exercise 6 | 1.5 points |
| Exercise 7 | 1.5 points |
| Overall quality* | 2 points |

Max possible points: 10

*: Here, I'll be grading that:
1. endpoints return relevant statuscodes
2. endpoints react to relevant HTTP methods
3. code quality as always (DRY, code works, etc.)
