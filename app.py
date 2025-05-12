from flask import Flask, render_template_string, request
import sqlite3
import os

app = Flask(__name__)

# Define database path
db_path = 'employees.db'

# If DB doesn't exist, create it from the SQL file
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    with open("company_employees.sql", "r") as f:
        cursor.executescript(f.read())
    # Add indexes to optimize search
    cursor.executescript("""
        CREATE INDEX IF NOT EXISTS idx_first_name ON employees(first_name);
        CREATE INDEX IF NOT EXISTS idx_last_name ON employees(last_name);
        CREATE INDEX IF NOT EXISTS idx_department ON employees(department);
    """)
    conn.commit()
    conn.close()

# HTML template with search and table display
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Employee Directory</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
        input[type=text] { padding: 6px; width: 200px; }
        button { padding: 6px 12px; }
    </style>
</head>
<body>
    <h1>Employee Directory</h1>
    <form method="get">
        <input type="text" name="query" placeholder="Search by name or department" value="{{ query }}">
        <button type="submit">Search</button>
    </form>
    <table>
        <thead>
            <tr>
                <th>Name</th><th>Email</th><th>Job Title</th><th>Department</th><th>Status</th>
            </tr>
        </thead>
        <tbody>
            {% for emp in employees %}
            <tr>
                <td>{{ emp[1] }} {{ emp[2] }}</td>
                <td>{{ emp[3] }}</td>
                <td>{{ emp[5] }}</td>
                <td>{{ emp[6] }}</td>
                <td>{{ emp[10] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

@app.route("/")
def index():
    query = request.args.get("query", "").strip()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if query:
        cursor.execute("""
            SELECT * FROM employees
            WHERE first_name LIKE ? OR last_name LIKE ? OR department LIKE ?
        """, (f"%{query}%", f"%{query}%", f"%{query}%"))
    else:
        cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, employees=employees, query=query)

if __name__ == "__main__":
    app.run(debug=True)
