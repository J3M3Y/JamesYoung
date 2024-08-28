<!DOCTYPE html>
<html> 
    <head>
        <title>Add New Sail</title>
        <link type="text/css" href="/static/style.css" rel="stylesheet">
    </head>

    <body>
        <header>
            <p><a href="/queries">Return to the queries page</a></p>
        </header>

        <h1>Add New Sail</h1>

        <form action="/new_sail" method="POST">
            <label for="sail_type">Sail Type:</label>
            <input type="text" id="sail_type" name="sail_type" required>

            <label for="size">Size:</label>
            <input type="text" id="size" name="size" required>

            <label for="customization">Customization Options:</label>
            <input type="text" id="customization" name="customization">

            <label for="inventory">Inventory Level:</label>
            <input type="number" id="inventory" name="inventory" required>

            <button type="submit">Add Sail</button>
        </form>

        <footer>
            <p><a href="/queries">Return to the queries page</a></p>
        </footer>
    </body>
</html>

