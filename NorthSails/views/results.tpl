<!DOCTYPE html>
<html> 
    <head>
        <title>{{ title }}</title>
        <link type="text/css" href="/static/style.css" rel="stylesheet">
    </head>

    <body>
        <header>
            <p><a href="/">Return to the home page</a></p>
        </header>

        <h1>{{ title }}</h1>

        % if len(records) < 1:
        <p><strong>No records found</strong></p>
        % else:
        <table>
            <tr>
                % for field in records[0].keys():
                <th>{{ field }}</th>
                % end
                % if 'OrderID' in records[0].keys(): 
                <th>Edit</th>
                <th>Delete</th>
                % end
            </tr>
            % for record in records:
            <tr>
                % for field in record.keys():
                <td>{{ record[field] }}</td>
                % end
                % if 'OrderID' in record.keys(): 
                <td><a href="/edit_order/{{ record['OrderID'] }}">Edit</a></td>
                <td>
                    <form action="/delete_order/{{ record['OrderID'] }}" method="POST" style="display:inline;">
                        <button type="submit">Delete</button>
                    </form>
                </td>
                % end
            </tr>
            % end
        </table>
        % end

        <footer>
            <p><a href="/">Return to the home page</a></p>
        </footer>
    </body>
</html>
