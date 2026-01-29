from typing import List, Dict, Any

def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    sql = """SELECT customerName ,creditLimit
        from customers
        WHERE creditLimit < 10000 or creditLimit > 100000"""
    return sql

def get_orders_with_null_comments():
    """Return orders that have null comments."""
    sql = """SELECT orderNumber ,comments
            from orders
            WHERE comments IS null
            ORDER BY orderDate
            """
    return sql

def get_first_5_customers():
    """Return the first 5 customers."""
    sql = """SELECT customerName ,contactLastName ,contactFirstName
            FROM customers
            ORDER by contactLastName
            LIMIT 5"""
    return sql

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    sql = """SELECT SUM(amount) as sum , AVG(amount) as avg , MIN(amount) as min ,MAX(amount) as max
                from payments"""
    return sql

def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    sql = """SELECT employees.firstName ,employees.lastName ,offices.phone
            FROM employees
            INNER JOIN offices
            on employees.officeCode = offices.officeCode"""
    return sql

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    sql = """SELECT customers.customerName , orders.shippedDate
            FROM customers
            LEFT JOIN orders
            on customers.customerNumber = orders.customerNumber"""
    return sql

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    sql = """SELECT customers.customerName , sum(orderdetails.quantityOrdered) as sum
        FROM customers
        INNER JOIN orders
        ON customers.customerNumber = orders.customerNumber
        INNER JOIN orderdetails
        on orders.orderNumber = orderdetails.orderNumber
        GROUP BY orderdetails.orderNumber
        ORDER BY customers.customerName
        """
    return sql

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    sql = """SELECT customers.customerName , employees.firstName ,employees.lastName ,sum(payments.amount) as sum
FROM customers
INNER JOIN employees
ON customers.salesRepEmployeeNumber = employees.employeeNumber
INNER JOIN payments
ON customers.customerNumber = payments.customerNumber
where customers.contactFirstName like '%Mu%' or customers.contactFirstName LIKE '%ly%'
GROUP BY customers.customerName ,employees.firstName ,employees.lastName
ORDER BY sum DESC"""
    return sql




