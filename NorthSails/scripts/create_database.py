import sqlite3


def create_empty_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Creating the Country table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Country (
        CountryID INTEGER PRIMARY KEY AUTOINCREMENT,
        CountryName VARCHAR(100) NOT NULL
    )
    ''')

    # Creating the SailLoft table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SailLoft (
        SailLoftID INTEGER PRIMARY KEY AUTOINCREMENT,
        SailLoftName VARCHAR(100) NOT NULL,
        Location VARCHAR(100) NOT NULL,
        CountryID INTEGER NOT NULL,
        FOREIGN KEY (CountryID) REFERENCES Country(CountryID)
    )
    ''')

    # Creating the Employees table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR(50) NOT NULL,
        ContactInfo VARCHAR(100),
        SailLoftID INTEGER NOT NULL,
        JobRoleID INTEGER NOT NULL,
        FOREIGN KEY (SailLoftID) REFERENCES SailLoft(SailLoftID),
        FOREIGN KEY (JobRoleID) REFERENCES JobRole(JobRoleID)
    )
    ''')

    # Creating the JobRole table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS JobRole (
        JobRoleID INTEGER PRIMARY KEY AUTOINCREMENT,
        JobRoleName VARCHAR(50) NOT NULL,
        Description TEXT
    )
    ''')

    # Creating the Sail table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sail (
        SailID INTEGER PRIMARY KEY AUTOINCREMENT,
        SailType VARCHAR(50) NOT NULL,
        Size VARCHAR(20) NOT NULL,
        CustomizationOptions TEXT,
        InventoryLevel INTEGER
    )
    ''')

    # Creating the Orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
        OrderDate DATETIME NOT NULL,
        DeliveryDate DATETIME,
        Status VARCHAR(20),
        CustomerID INTEGER NOT NULL,
        SailLoftID INTEGER NOT NULL,
        EmployeeID INTEGER NOT NULL,
        FOREIGN KEY (CustomerID) REFERENCES CustomizationDesigns(CustomerID),
        FOREIGN KEY (SailLoftID) REFERENCES SailLoft(SailLoftID),
        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
    )
    ''')

    # Creating the OrderLines table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS OrderLines (
        OrderLineID INTEGER PRIMARY KEY AUTOINCREMENT,
        OrderID INTEGER NOT NULL,
        SailID INTEGER NOT NULL,
        Quantity INTEGER NOT NULL,
        Measurements TEXT,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (SailID) REFERENCES Sail(SailID)
    )
    ''')

    # Creating the Feedback tabel
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Feedback (
        FeedbackID INTEGER PRIMARY KEY AUTOINCREMENT,
        Rating INTEGER NOT NULL,
        Comments TEXT,
        CustomerID INTEGER NOT NULL,
        OrderID INTEGER NOT NULL,
        FOREIGN KEY (CustomerID) REFERENCES CustomizationDesigns(CustomerID),
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
    )
    ''')

    # Creating the CustomizationDesigns table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CustomizationDesigns (
        DesignID INTEGER PRIMARY KEY AUTOINCREMENT,
        DesignDetails TEXT,
        CustomerID INTEGER NOT NULL,
        SailID INTEGER NOT NULL,
        FOREIGN KEY (CustomerID) REFERENCES Orders(CustomerID),
        FOREIGN KEY (SailID) REFERENCES Sail(SailID)
    )
    ''')

  
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    create_empty_database('sail_loft.db')
