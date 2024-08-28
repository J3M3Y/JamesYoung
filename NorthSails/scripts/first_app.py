
import sqlite3
import create_database as create_db
import insert_data as db_insert
from bottle import route, run, template, static_file, response, request, redirect, template

#Route for the homepage
@route('/')
def index():
    return template('index')

#Route to the queries
@route('/queries')
def queries():
    return template('queries.tpl')


#Route to create the database
@route('/create_database')
def create_database():
    create_db.create_empty_database('sail_loft.db')
    return template('database_create')



#Route to insert sample data
@route('/insert_data')
def insert_data():
    db_insert.insert_sample_data('sail_loft.db')
    return template('database_insert')



#Route to display all orders
@route('/orders')
def orders():
    conn = sqlite3.connect('sail_loft.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

#Fetch the data from the Orders table
    query = 'SELECT * FROM Orders'
    cursor.execute(query)
    result = cursor.fetchall()

    

    cursor.close()
    conn.close()

#Pass the data to the 'results.tpl' template
    return template('results', records=result, title='All Orders')


@route('/export_orders')
def export_orders():
#Connect to the database
    conn = sqlite3.connect('sail_loft.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    #Fetch all orders
    query = 'SELECT * FROM Orders'
    cursor.execute(query)
    result = cursor.fetchall()

    #Format the data as plain text
    file_content = "OrderID | OrderDate | DeliveryDate | Status | CustomerID | SailLoftID | EmployeeID\n"
    file_content += "-" * 80 + "\n"

    for row in result:
        line = f"{row['OrderID']} | {row['OrderDate']} | {row['DeliveryDate']} | {row['Status']} | {row['CustomerID']} | {row['SailLoftID']} | {row['EmployeeID']}\n"
        file_content += line

    cursor.close()
    conn.close()

    #Set the response headers to treat this as a downloadable file
    response.content_type = 'text/plain'
    response.headers['Content-Disposition'] = 'attachment; filename="orders.txt"'
    
    return file_content




#Creates a new order
@route('/new_order', method='GET')
def new_order_form():
    return template('new_order.tpl')

#Allows users to enter data into the table
@route('/new_order', method='POST')
def insert_order():
    order_date = request.forms.get('order_date')
    delivery_date = request.forms.get('delivery_date')
    status = request.forms.get('status')
    customer_id = request.forms.get('customer_id')
    sail_loft_id = request.forms.get('sail_loft_id')
    employee_id = request.forms.get('employee_id')

    conn = sqlite3.connect('sail_loft.db')
    cursor = conn.cursor()

    query = '''INSERT INTO Orders (OrderDate, DeliveryDate, Status, CustomerID, SailLoftID, EmployeeID)
               VALUES (?, ?, ?, ?, ?, ?)'''
    cursor.execute(query, (order_date, delivery_date, status, customer_id, sail_loft_id, employee_id))

    conn.commit()
    cursor.close()
    conn.close()

    redirect('/orders')


#Create Forms for updating records

@route('/edit_order/<order_id>', method='GET')
def edit_order_form(order_id):
    conn = sqlite3.connect('sail_loft.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = 'SELECT * FROM Orders WHERE OrderID = ?'
    cursor.execute(query, (order_id,))
    order = cursor.fetchone()

    cursor.close()
    conn.close()

    return template('edit_order.tpl', order=order)

@route('/edit_order/<order_id>', method='POST')
def update_order(order_id):
    order_date = request.forms.get('order_date')
    delivery_date = request.forms.get('delivery_date')
    status = request.forms.get('status')
    customer_id = request.forms.get('customer_id')
    sail_loft_id = request.forms.get('sail_loft_id')
    employee_id = request.forms.get('employee_id')

    conn = sqlite3.connect('sail_loft.db')
    cursor = conn.cursor()

    query = '''UPDATE Orders SET OrderDate = ?, DeliveryDate = ?, Status = ?, 
               CustomerID = ?, SailLoftID = ?, EmployeeID = ? WHERE OrderID = ?'''
    cursor.execute(query, (order_date, delivery_date, status, customer_id, sail_loft_id, employee_id, order_id))

    conn.commit()
    cursor.close()
    conn.close()

    redirect('/orders')




#A Route to display all sails
@route('/sails')
def sails():
    conn = sqlite3.connect('sail_loft.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = 'SELECT * FROM Sail'
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return template('results', records=result, title='All Sails')




# QUERIES
#0 Orders per Loft
@route('/orders_per_loft')
def orders_per_loft():
    conn = sqlite3.connect('sail_loft.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    #SQL query to count orders per sail loft
    query = '''
    SELECT SailLoft.SailLoftName, COUNT(Orders.OrderID) AS OrderCount
    FROM Orders
    JOIN SailLoft ON Orders.SailLoftID = SailLoft.SailLoftID
    GROUP BY SailLoft.SailLoftID
    ORDER BY OrderCount DESC
    '''
    cursor.execute(query)
    records = cursor.fetchall()

    conn.close()

    #Pass the results to the template
    return template('query_results.tpl', title='Orders per Sail Loft', records=records)


#1 Total number of orders
@route('/total_orders')
def total_orders():
    conn = sqlite3.connect('sail_loft.db')
    cursor = conn.cursor()

    query = 'SELECT COUNT(*) AS TotalOrders FROM Orders'
    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    return template('query_results.tpl', title='Total Number of Orders', result=f'Total Orders: {result[0]}')

#2 Average inventory level per Sail Loft
@route('/average_inventory')
def average_inventory():
    conn = sqlite3.connect('sail_loft.db')
    cursor = conn.cursor()

    query = 'SELECT AVG(InventoryLevel) AS AverageInventory FROM Sail'
    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    return template('query_results.tpl', title='Average Inventory Level', result=f'Average Inventory Level: {result[0]:.2f}')

#3 Minimum and Maximum Order dates
@route('/order_dates')
def order_dates():
    conn = sqlite3.connect('sail_loft.db')
    cursor = conn.cursor()

    query = 'SELECT MIN(OrderDate) AS FirstOrderDate, MAX(OrderDate) AS LastOrderDate FROM Orders'
    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    return template('query_results.tpl', title='Order Dates', result=f'First Order Date: {result[0]}, Last Order Date: {result[1]}')

#4 Orders count by status
@route('/orders_by_status')
def orders_by_status():
    conn = sqlite3.connect('sail_loft.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = 'SELECT Status, COUNT(*) AS StatusCount FROM Orders GROUP BY Status'
    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()

    return template('query_results.tpl', title='Orders by Status', records=result)

#5 Employees ordered by last name
@route('/employees_ordered')
def employees_ordered():
    conn = sqlite3.connect('sail_loft.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = 'SELECT * FROM Employees ORDER BY LastName ASC'
    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()

    return template('query_results.tpl', title='Employees Ordered by Last Name', records=result)

#6 Orders with Customer + Employee information
@route('/orders_with_info')
def orders_with_info():
    conn = sqlite3.connect('sail_loft.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = '''
    SELECT Orders.OrderID, Orders.OrderDate, Orders.Status, 
           Employees.FirstName || ' ' || Employees.LastName AS EmployeeName,
           SailLoft.SailLoftName
    FROM Orders
    JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
    JOIN SailLoft ON Orders.SailLoftID = SailLoft.SailLoftID
    '''
    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()

    return template('query_results.tpl', title='Orders with Employee and Sail Loft Info', records=result)

#7 Total Inventory by Sail Type
@route('/inventory_by_sail')
def inventory_by_sail():
    conn = sqlite3.connect('sail_loft.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = 'SELECT SailType, SUM(InventoryLevel) AS TotalInventory FROM Sail GROUP BY SailType'
    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()

    return template('query_results.tpl', title='Inventory by Sail Type', records=result)

#8 Insert a new sail
@route('/new_sail', method=['GET', 'POST'])
def new_sail():
    if request.method == 'POST':
        sail_type = request.forms.get('sail_type')
        size = request.forms.get('size')
        customization = request.forms.get('customization')
        inventory = int(request.forms.get('inventory'))

        conn = sqlite3.connect('sail_loft.db')
        cursor = conn.cursor()

        query = 'INSERT INTO Sail (SailType, Size, CustomizationOptions, InventoryLevel) VALUES (?, ?, ?, ?)'
        cursor.execute(query, (sail_type, size, customization, inventory))

        conn.commit()
        conn.close()

        redirect('/inventory_by_sail')
    else:
        return template('new_sail.tpl')

#9 Update an Existing Employee's job role
@route('/update_employee/<employee_id>', method=['GET', 'POST'])
def update_employee(employee_id):
    conn = sqlite3.connect('sail_loft.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if request.method == 'POST':
        job_role_id = int(request.forms.get('job_role_id'))

        query = 'UPDATE Employees SET JobRoleID = ? WHERE EmployeeID = ?'
        cursor.execute(query, (job_role_id, employee_id))

        conn.commit()
        conn.close()

        redirect('/employees_ordered')
    else:
        query = 'SELECT * FROM Employees WHERE EmployeeID = ?'
        cursor.execute(query, (employee_id,))
        employee = cursor.fetchone()

        query = 'SELECT * FROM JobRole'
        cursor.execute(query)
        job_roles = cursor.fetchall()

        conn.close()

        return template('update_employee.tpl', employee=employee, job_roles=job_roles)

#10 Delete an Order by ID
@route('/delete_order/<order_id>', method='POST')
def delete_order(order_id):
    conn = sqlite3.connect('sail_loft.db')
    cursor = conn.cursor()

    query = 'DELETE FROM Orders WHERE OrderID = ?'
    cursor.execute(query, (order_id,))

    conn.commit()
    conn.close()

    redirect('/orders_by_status')


#Route to serve static files
@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')


run(host='localhost', port=8080, debug=True, reloader=True)
