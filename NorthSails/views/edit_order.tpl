<!DOCTYPE html>
<html> 
<head>
    <title>Edit Order</title>
    <link type="text/css" href="/static/style.css" rel="stylesheet">
</head>
<body>
    <header>
        <p><a href="/">Return to the home page</a></p>
    </header>

    <h1>Edit Order</h1>

    <form action="/edit_order/{{ order['OrderID'] }}" method="POST">
        <label for="order_date">Order Date:</label>
        <input type="text" id="order_date" name="order_date" value="{{ order['OrderDate'] }}" required>

        <label for="delivery_date">Delivery Date:</label>
        <input type="text" id="delivery_date" name="delivery_date" value="{{ order['DeliveryDate'] }}" required>

        <label for="status">Status:</label>
        <input type="text" id="status" name="status" value="{{ order['Status'] }}" required>

        <label for="customer_id">Customer ID:</label>
        <input type="number" id="customer_id" name="customer_id" value="{{ order['CustomerID'] }}" required>

        <label for="sail_loft_id">Sail Loft ID:</label>
        <input type="number" id="sail_loft_id" name="sail_loft_id" value="{{ order['SailLoftID'] }}" required>

        <label for="employee_id">Employee ID:</label>
        <input type="number" id="employee_id" name="employee_id" value="{{ order['EmployeeID'] }}" required>

        <button type="submit">Update Order</button>
    </form>

    <footer>
        <p><a href="/orders">View Orders</a></p>
    </footer>
</body>
</html>
