from flask import Flask, request, render_template
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

# Configuration
MONGO_URI = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client[os.getenv("MONGO_DB_NAME", "test_db")]
collection = db[os.getenv("MONGO_COLLECTION_NAME", "test_collection")]

# Application metadata
MY_NAME = "Achref LOUSSAIEf"
PROJECT_NAME = "Challenge3"
VERSION = "V13"

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
