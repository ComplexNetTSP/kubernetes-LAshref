# app.py
from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Getting the current server hostname and date
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Information to display
    name = "Achref LOUSSAIEF"
    project_name = "My Flask Project"
    version = "V13"
    
    # Return HTML with all information
    return f"""
    <html>
        <body>
            <h1>Welcome to {project_name}!</h1>
            <p>Developed by: {name}</p>
            <p>Project Version: {version}</p>
            <p>Server Hostname: {hostname}</p>
            <p>Current Date: {current_date}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)