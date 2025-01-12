from flask import Flask, request, render_template
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

# MongoDB configuration
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["flask_app_db"]
collection = db["requests"]

# Application metadata
MY_NAME = "Achref LOUSSAIEF DB"
PROJECT_NAME = "Challenge4"
VERSION = "V5"

@app.route("/")
def home():
    # Get client IP and current date
    client_ip = request.remote_addr
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert record into MongoDB
    collection.insert_one({"ip": client_ip, "date": current_date})

    # Fetch last 10 records
    records = list(collection.find().sort("_id", -1).limit(10))

    # Render the page
    return render_template("index.html", 
                           name=MY_NAME,
                           project=PROJECT_NAME,
                           version=VERSION,
                           hostname=os.getenv("HOSTNAME", "localhost"),
                           date=current_date,
                           records=records)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)