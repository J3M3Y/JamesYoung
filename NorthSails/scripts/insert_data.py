
import sqlite3

def insert_countries(cursor):
    countries = [
        {'CountryName': 'Ireland'},
        {'CountryName': 'USA'},
        {'CountryName': 'Australia'},
        {'CountryName': 'Canada'},
        {'CountryName': 'New Zealand'},
        {'CountryName': 'United Kingdom'},
        {'CountryName': 'South Africa'},
        {'CountryName': 'Japan'},
        {'CountryName': 'Brazil'},
        {'CountryName': 'Germany'},
    ]
    cursor.executemany('''
    INSERT INTO Country (CountryName)
    VALUES (:CountryName)
    ''', countries)

def insert_sail_lofts(cursor):
    sail_lofts = [
        {'SailLoftName': 'Dublin Loft', 'Location': 'Dublin', 'CountryID': 1},
        {'SailLoftName': 'San Francisco Loft', 'Location': 'San Francisco', 'CountryID': 2},
        {'SailLoftName': 'Sydney Loft', 'Location': 'Sydney', 'CountryID': 3},
        {'SailLoftName': 'Vancouver Loft', 'Location': 'Vancouver', 'CountryID': 4},
        {'SailLoftName': 'Auckland Loft', 'Location': 'Auckland', 'CountryID': 5},
        {'SailLoftName': 'London Loft', 'Location': 'London', 'CountryID': 6},
        {'SailLoftName': 'Cape Town Loft', 'Location': 'Cape Town', 'CountryID': 7},
        {'SailLoftName': 'Tokyo Loft', 'Location': 'Tokyo', 'CountryID': 8},
        {'SailLoftName': 'Rio Loft', 'Location': 'Rio de Janeiro', 'CountryID': 9},
        {'SailLoftName': 'Hamburg Loft', 'Location': 'Hamburg', 'CountryID': 10},
    ]
    cursor.executemany('''
    INSERT INTO SailLoft (SailLoftName, Location, CountryID)
    VALUES (:SailLoftName, :Location, :CountryID)
    ''', sail_lofts)

def insert_job_roles(cursor):
    job_roles = [
        {'JobRoleName': 'Manager', 'Description': 'Oversees operations'},
        {'JobRoleName': 'Designer', 'Description': 'Designs sails'},
        {'JobRoleName': 'Salesperson', 'Description': 'Handles sales'},
        {'JobRoleName': 'Technician', 'Description': 'Handles technical maintenance'},
        {'JobRoleName': 'Logistics Coordinator', 'Description': 'Coordinates shipping and logistics'},
        {'JobRoleName': 'Customer Support', 'Description': 'Provides customer support and service'},
        {'JobRoleName': 'Quality Inspector', 'Description': 'Inspects the quality of the products'},
        {'JobRoleName': 'Production Manager', 'Description': 'Manages the production process'},
        {'JobRoleName': 'Warehouse Manager', 'Description': 'Manages warehouse operations'},
        {'JobRoleName': 'Procurement Officer', 'Description': 'Handles procurement and supplies'},
    ]
    cursor.executemany('''
    INSERT INTO JobRole (JobRoleName, Description)
    VALUES (:JobRoleName, :Description)
    ''', job_roles)

def insert_employees(cursor):
    employees = [
        {'FirstName': 'John', 'LastName': 'Doe', 'ContactInfo': 'john.doe@example.com', 'SailLoftID': 1, 'JobRoleID': 1},
        {'FirstName': 'Jane', 'LastName': 'Smith', 'ContactInfo': 'jane.smith@example.com', 'SailLoftID': 2, 'JobRoleID': 2},
        {'FirstName': 'Emily', 'LastName': 'Jones', 'ContactInfo': 'emily.jones@example.com', 'SailLoftID': 3, 'JobRoleID': 3},
        {'FirstName': 'Michael', 'LastName': 'Brown', 'ContactInfo': 'michael.brown@example.com', 'SailLoftID': 4, 'JobRoleID': 4},
        {'FirstName': 'Sarah', 'LastName': 'Davis', 'ContactInfo': 'sarah.davis@example.com', 'SailLoftID': 5, 'JobRoleID': 5},
        {'FirstName': 'Robert', 'LastName': 'Wilson', 'ContactInfo': 'robert.wilson@example.com', 'SailLoftID': 6, 'JobRoleID': 6},
        {'FirstName': 'Linda', 'LastName': 'Martinez', 'ContactInfo': 'linda.martinez@example.com', 'SailLoftID': 7, 'JobRoleID': 7},
        {'FirstName': 'David', 'LastName': 'Anderson', 'ContactInfo': 'david.anderson@example.com', 'SailLoftID': 8, 'JobRoleID': 8},
        {'FirstName': 'Susan', 'LastName': 'Taylor', 'ContactInfo': 'susan.taylor@example.com', 'SailLoftID': 9, 'JobRoleID': 9},
        {'FirstName': 'James', 'LastName': 'Thomas', 'ContactInfo': 'james.thomas@example.com', 'SailLoftID': 10, 'JobRoleID': 10},
    ]
    cursor.executemany('''
    INSERT INTO Employees (FirstName, LastName, ContactInfo, SailLoftID, JobRoleID)
    VALUES (:FirstName, :LastName, :ContactInfo, :SailLoftID, :JobRoleID)
    ''', employees)

def insert_sails(cursor):
    sails = [
        {'SailType': 'Main Sail', 'Size': 'Large', 'CustomizationOptions': 'Sponsor Logo', 'InventoryLevel': 10},
        {'SailType': 'Jib', 'Size': 'Medium', 'CustomizationOptions': 'Solid Colour', 'InventoryLevel': 5},
        {'SailType': 'Spinnaker', 'Size': 'Large', 'CustomizationOptions': 'Custom Design 3', 'InventoryLevel': 7},
        {'SailType': 'Genoa', 'Size': 'Small', 'CustomizationOptions': 'Solid Colour', 'InventoryLevel': 12},
        {'SailType': 'Storm Jib', 'Size': 'Small', 'CustomizationOptions': 'Sponsor Logo', 'InventoryLevel': 8},
        {'SailType': 'Drifter', 'Size': 'Medium', 'CustomizationOptions': 'Sponsor Logo', 'InventoryLevel': 15},
        {'SailType': 'Code Zero', 'Size': 'Large', 'CustomizationOptions': 'Double Striped', 'InventoryLevel': 4},
        {'SailType': 'Topper', 'Size': 'Small', 'CustomizationOptions': 'Sponsor Logo', 'InventoryLevel': 9},
        {'SailType': 'Cruising', 'Size': 'Large', 'CustomizationOptions': 'Solid Colour', 'InventoryLevel': 11},
        {'SailType': 'Racing', 'Size': 'Medium', 'CustomizationOptions': 'Solid Colour', 'InventoryLevel': 6},
    ]
    cursor.executemany('''
    INSERT INTO Sail (SailType, Size, CustomizationOptions, InventoryLevel)
    VALUES (:SailType, :Size, :CustomizationOptions, :InventoryLevel)
    ''', sails)

def insert_orders(cursor):
    orders = [
        {'OrderDate': '2022-08-01 10:30:00', 'DeliveryDate': '2022-08-10 14:00:00', 'Status': 'Shipped', 'CustomerID': 1, 'SailLoftID': 1, 'EmployeeID': 1},
        {'OrderDate': '2022-08-02 11:45:00', 'DeliveryDate': '2022-08-15 16:30:00', 'Status': 'Processing', 'CustomerID': 2, 'SailLoftID': 2, 'EmployeeID': 2},
        {'OrderDate': '2020-08-03 09:20:00', 'DeliveryDate': '2020-08-20 12:45:00', 'Status': 'Delivered', 'CustomerID': 3, 'SailLoftID': 3, 'EmployeeID': 3},
        {'OrderDate': '2021-08-04 13:15:00', 'DeliveryDate': '2021-08-25 17:00:00', 'Status': 'Shipped', 'CustomerID': 4, 'SailLoftID': 4, 'EmployeeID': 4},
        {'OrderDate': '2024-08-05 08:50:00', 'DeliveryDate': '2024-08-30 15:10:00', 'Status': 'Processing', 'CustomerID': 5, 'SailLoftID': 5, 'EmployeeID': 5},
        {'OrderDate': '2023-08-06 14:40:00', 'DeliveryDate': '2023-09-05 10:20:00', 'Status': 'Delivered', 'CustomerID': 6, 'SailLoftID': 6, 'EmployeeID': 6},
        {'OrderDate': '2022-08-07 09:00:00', 'DeliveryDate': '2022-09-10 18:00:00', 'Status': 'Shipped', 'CustomerID': 7, 'SailLoftID': 7, 'EmployeeID': 7},
        {'OrderDate': '2018-08-08 10:25:00', 'DeliveryDate': '2018-09-15 11:30:00', 'Status': 'Processing', 'CustomerID': 8, 'SailLoftID': 8, 'EmployeeID': 8},
        {'OrderDate': '2020-08-09 07:55:00', 'DeliveryDate': '2020-09-20 16:45:00', 'Status': 'Delivered', 'CustomerID': 9, 'SailLoftID': 9, 'EmployeeID': 9},
        {'OrderDate': '2024-08-10 12:30:00', 'DeliveryDate': '2024-09-25 13:50:00', 'Status': 'Shipped', 'CustomerID': 10, 'SailLoftID': 10, 'EmployeeID': 10},
    ]

    cursor.executemany('''
    INSERT INTO Orders (OrderDate, DeliveryDate, Status, CustomerID, SailLoftID, EmployeeID)
    VALUES (:OrderDate, :DeliveryDate, :Status, :CustomerID, :SailLoftID, :EmployeeID)
    ''', orders)
   

def insert_order_lines(cursor):
    order_lines = [
        {'OrderID': 1, 'SailID': 1, 'Quantity': 2, 'Measurements': 'Measurements 1'},
        {'OrderID': 2, 'SailID': 2, 'Quantity': 1, 'Measurements': 'Measurements 2'},
        {'OrderID': 3, 'SailID': 3, 'Quantity': 3, 'Measurements': 'Measurements 3'},
        {'OrderID': 4, 'SailID': 4, 'Quantity': 1, 'Measurements': 'Measurements 4'},
        {'OrderID': 5, 'SailID': 5, 'Quantity': 2, 'Measurements': 'Measurements 5'},
        {'OrderID': 6, 'SailID': 6, 'Quantity': 1, 'Measurements': 'Measurements 6'},
        {'OrderID': 7, 'SailID': 7, 'Quantity': 3, 'Measurements': 'Measurements 7'},
        {'OrderID': 8, 'SailID': 8, 'Quantity': 2, 'Measurements': 'Measurements 8'},
        {'OrderID': 9, 'SailID': 9, 'Quantity': 1, 'Measurements': 'Measurements 9'},
        {'OrderID': 10, 'SailID': 10, 'Quantity': 2, 'Measurements': 'Measurements 10'},
    ]
    cursor.executemany('''
    INSERT INTO OrderLines (OrderID, SailID, Quantity, Measurements)
    VALUES (:OrderID, :SailID, :Quantity, :Measurements)
    ''', order_lines)

def insert_feedback(cursor):
    feedback = [
        {'Rating': 5, 'Comments': 'Excellent quality!', 'CustomerID': 1, 'OrderID': 1},
        {'Rating': 4, 'Comments': 'Good, but took too long.', 'CustomerID': 2, 'OrderID': 2},
        {'Rating': 3, 'Comments': 'Average service.', 'CustomerID': 3, 'OrderID': 3},
        {'Rating': 5, 'Comments': 'Highly recommended!', 'CustomerID': 4, 'OrderID': 4},
        {'Rating': 4, 'Comments': 'Satisfied with the product.', 'CustomerID': 5, 'OrderID': 5},
        {'Rating': 2, 'Comments': 'Could be better.', 'CustomerID': 6, 'OrderID': 6},
        {'Rating': 3, 'Comments': 'Okay experience.', 'CustomerID': 7, 'OrderID': 7},
        {'Rating': 4, 'Comments': 'Will order again.', 'CustomerID': 8, 'OrderID': 8},
        {'Rating': 5, 'Comments': 'Top notch!', 'CustomerID': 9, 'OrderID': 9},
        {'Rating': 4, 'Comments': 'Good, but room for improvement.', 'CustomerID': 10, 'OrderID': 10},
    ]
    cursor.executemany('''
    INSERT INTO Feedback (Rating, Comments, CustomerID, OrderID)
    VALUES (:Rating, :Comments, :CustomerID, :OrderID)
    ''', feedback)

def insert_customization_designs(cursor):
    customization_designs = [
        {'DesignDetails': 'Matte', 'CustomerID': 1, 'SailID': 1},
        {'DesignDetails': 'Neon Reflective', 'CustomerID': 2, 'SailID': 2},
        {'DesignDetails': 'Half Colour', 'CustomerID': 3, 'SailID': 3},
        {'DesignDetails': 'Solid Colour', 'CustomerID': 4, 'SailID': 4},
        {'DesignDetails': 'Sponsor Logo', 'CustomerID': 5, 'SailID': 5},
        {'DesignDetails': 'Triangles', 'CustomerID': 6, 'SailID': 6},
        {'DesignDetails': 'Double Striped', 'CustomerID': 7, 'SailID': 7},
        {'DesignDetails': 'Stripes', 'CustomerID': 8, 'SailID': 8},
        {'DesignDetails': 'Blue Edges', 'CustomerID': 9, 'SailID': 9},
        {'DesignDetails': 'Red Edges', 'CustomerID': 10, 'SailID': 10},
    ]
    cursor.executemany('''
    INSERT INTO CustomizationDesigns (DesignDetails, CustomerID, SailID)
    VALUES (:DesignDetails, :CustomerID, :SailID)
    ''', customization_designs)

def insert_sample_data(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

#Insert data into each table
    insert_countries(cursor)
    insert_sail_lofts(cursor)
    insert_job_roles(cursor)
    insert_employees(cursor)
    insert_sails(cursor)
    insert_orders(cursor)
    insert_order_lines(cursor)
    insert_feedback(cursor)
    insert_customization_designs(cursor)

#Committing the changes and closing the connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_sample_data('sail_loft.db')
