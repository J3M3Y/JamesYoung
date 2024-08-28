<!DOCTYPE html>
<html> 
    <head>
        <title>Update Employee</title>
        <link type="text/css" href="/static/style.css" rel="stylesheet">
    </head>

    <body>
        <header>
            <p><a href="/queries">Return to the queries page</a></p>
        </header>

        <h1>Update Employee</h1>

        <form action="/update_employee/{{ employee['EmployeeID'] }}" method="POST">
            <label for="job_role_id">Job Role:</label>
            <select id="job_role_id" name="job_role_id" required>
                % for role in job_roles:
                <option value="{{ role['JobRoleID'] }}" % if role['JobRoleID'] == employee['JobRoleID']: selected % end>{{ role['JobRoleName'] }}</option>
                % end
            </select>

            <button type="submit">Update</button>
        </form>

        <footer>
            <p><a href="/queries">Return to the queries page</a></p>
        </footer>
    </body>
</html>
