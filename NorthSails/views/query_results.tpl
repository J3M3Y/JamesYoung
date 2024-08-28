<!DOCTYPE html>
<html> 
    <head>
        <title>{{ title }}</title>
        <link type="text/css" href="/static/style.css" rel="stylesheet">
    </head>

    <body>
        <header>
            <p><a href="/queries">Return to the queries page</a></p>
        </header>

        <h1>{{ title }}</h1>

        % if 'result' in globals():
        <p><strong>{{ result }}</strong></p>
        % elif 'records' in globals() and len(records) > 0:
        <table>
            <tr>
                % for field in records[0].keys():
                <th>{{ field }}</th>
                % end
            </tr>
            % for record in records:
            <tr>
                % for field in record.keys():
                <td>{{ record[field] }}</td>
                % end
            </tr>
            % end
        </table>
        % else:
        <p><strong>No records found</strong></p>
        % end

        <footer>
            <p><a href="/queries">Return to the queries page</a></p>
        </footer>
    </body>
</html>
