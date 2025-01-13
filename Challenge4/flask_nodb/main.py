from flask import Flask, render_template_string, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Variables for rendering
    my_name = "Achref LOUSSAIEF"
    project_name = "My Kubernetes Project"
    version = "V4"
    hostname=os.getenv("HOSTNAME", "localhost")
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get client IP address
    client_ip = request.remote_addr

    # HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ project_name }} - Home</title>
    </head>
    <body>
        <h1>Welcome to {{ project_name }}!</h1>
        <p><strong>Your Name:</strong> {{ your_name }}</p>
        <p><strong>Project Name:</strong> {{ project_name }}</p>
        <p><strong>Version:</strong> {{ version }}</p>
        <p><strong>Server Hostname:</strong> {{ hostname }}</p>
        <p><strong>Current Date:</strong> {{ current_date }}</p>
        <p><strong>Note:</strong> This application is not connected to a database.</p>
    </body>
    </html>
    """

    return render_template_string(
        html_content,
        your_name=my_name,
        project_name=project_name,
        version=version,
        hostname=hostname,
        current_date=current_date
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)